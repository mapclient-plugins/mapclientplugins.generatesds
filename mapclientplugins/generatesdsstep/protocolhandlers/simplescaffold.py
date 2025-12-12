import json
import logging
import os
import shutil

from mapclient.core.workflow.workflowscene import determine_connections, create_from, get_step_name_from_identifier
from mapclient.core.utils import copy_step_additional_config_files, get_steps_additional_config_files, create_configured_step

from mapclientplugins.generatesdsstep.definitions import SCAFFOLD_INFO_FILE

logger = logging.getLogger(__name__)


def _update_step_index_map(step_index_map, step_name, value_index, index):
    value = step_index_map.get(step_name, [-1, -1])
    value[value_index] = index
    step_index_map[step_name] = value


def run_protocol(model, inputs, output_dir):
    wm = model.workflowManager()

    # matched_config_files = []
    step_index_map = {}
    original_data_gathered = False
    original_index_step_map = {}
    original_connections = {}
    workflow_data = {}
    workflow_provenance_file = output_dir
    required_steps = []
    # Remove the target directory, we don't want to do anything about that here.
    inputs.pop(0)
    for i in inputs:
        if i['type'] == 'identifier_file':
            source_configuration_dir = os.path.dirname(i['value'])
            target_configuration_dir = os.path.join(output_dir, i['destination'])
            step_configuration_filename = os.path.basename(i['value'])

            wf = wm.load_workflow_virtually(source_configuration_dir)

            shutil.copy(i['value'], target_configuration_dir)

            step_identifier, configuration_ext = os.path.splitext(step_configuration_filename)
            step_name = get_step_name_from_identifier(wf, step_identifier)
            _update_step_index_map(step_index_map, step_identifier, 1, len(required_steps))
            required_steps.append((step_name, step_identifier))

            with open(i['value']) as f:
                config = f.read()

            step = create_configured_step(step_identifier, step_name, config, source_configuration_dir)

            if not original_data_gathered:
                wf.beginGroup('nodes')
                node_count = wf.beginReadArray('nodelist')
                for node_index in range(node_count):
                    wf.setArrayIndex(node_index)
                    # name = wf.value('name')
                    identifier = wf.value('identifier')
                    original_index_step_map[node_index] = identifier
                    connections = determine_connections(wf, node_index)
                    original_connections[node_index] = connections
                    _update_step_index_map(step_index_map, identifier, 0, node_index)

                wf.endArray()
                wf.endGroup()
                original_data_gathered = True

            workflow_data[step_identifier] = {
                "config": step_configuration_filename,
                "internal": get_steps_additional_config_files(step),
            }
            if step.getName() == "Argon Scene Exporter":
                try:
                    config_data = json.loads(step.serialize())
                    for expected_key in ["outputDir", "previous_location", "exportType"]:
                        if expected_key not in config_data:
                            logger.warning(
                                f"Configuration file for {step_configuration_filename} does not follow expected standard.")
                    if "outputDir" in config_data:
                        config_data["outputDir"] = "../derivative"
                    if "previous_location" in config_data:
                        config_data["previous_location"] = "."

                    with open(os.path.join(target_configuration_dir, step_configuration_filename), "w") as f:
                        json.dump(config_data, f, default=lambda o: o.__dict__, sort_keys=True, indent=4)

                except json.JSONDecodeError:
                    logging.warning(f"Configuration file for {step_configuration_filename} is not JSON decodable.")

            copy_step_additional_config_files(step, source_configuration_dir, target_configuration_dir)
        elif i['type'] == 'directory':
            src = i['value']
            dst = os.path.join(output_dir, i['destination'])
            os.makedirs(dst, exist_ok=True)
            names = os.listdir(src)
            for name in names:
                src_name = os.path.join(src, name)
                dst_name = os.path.join(dst, name)
                if os.path.isfile(src_name):
                    shutil.copy2(src_name, dst_name)
        elif i['type'] == 'dict':
            workflow_provenance_file = os.path.join(output_dir, i['destination'])
            with open(workflow_provenance_file, 'w') as f:
                json.dump(i['value'], f)

    new_connections = []
    for required_step in required_steps:
        required_identifier = required_step[1]
        old_index, new_index = step_index_map[required_identifier]
        step_connections = []
        for connection in original_connections[old_index]:
            new_connection_start = step_index_map[original_index_step_map[connection[0]]][1]
            new_connection_end = step_index_map[original_index_step_map[connection[2]]][1]
            if new_connection_end != -1:
                new_connection = (new_connection_start, connection[1], new_connection_end, connection[3], False)
                step_connections.append(new_connection)

        new_connections.append(step_connections)

    workflow_location = os.path.join(output_dir, 'primary')
    wf = wm.create_empty_workflow(workflow_location)
    create_from(wf, required_steps, new_connections, workflow_location)
    scaffold_info = {
        'id': 'scaffold-info-using-map-client-workflow',
        'version': '1.0.0',
        'mapping-tools-workflow-file': os.path.relpath(wf.fileName(), workflow_location),
        'mapping-tools-provenance-file': os.path.relpath(workflow_provenance_file, workflow_location),
        'settings-files': workflow_data,
    }
    with open(os.path.join(output_dir, 'primary', SCAFFOLD_INFO_FILE), 'w') as f:
        json.dump(scaffold_info, f, default=lambda o: o.__dict__, sort_keys=True, indent=2)
