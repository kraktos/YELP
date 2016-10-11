# Reads and loads the necessary system parameters
import ConfigParser

section='default'
config = ConfigParser.ConfigParser()
config.read('CONFIG.ini')

# general settings
data_path = config.get(section, 'data_path')