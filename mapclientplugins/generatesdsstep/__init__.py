
"""
MAP Client Plugin - Generated from MAP Client v0.18.0
"""

__version__ = '0.1.0'
__author__ = 'Kay Wang'
__stepname__ = 'generatesds'
__location__ = 'https://github.com/mapclient-plugins/mapclientplugins.generatesds'

# import class that derives itself from the step mountpoint.
from mapclientplugins.generatesdsstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc