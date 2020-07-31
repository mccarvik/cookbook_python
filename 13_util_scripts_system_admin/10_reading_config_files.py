from configparser import ConfigParser
cfg = ConfigParser()
print(cfg.read('config.ini'))
print(cfg.sections())
print(cfg.get('installation','library'))
print(cfg.getboolean('debug','log_errors'))
print(cfg.getint('server','port'))
print(cfg.getint('server','nworkers'))
print(cfg.get('server','signature'))

# can modify config file and write it back
cfg.set('server','port','9000')
cfg.set('debug','log_errors','False')
import sys
cfg.write(sys.stdout)

# names are case insensitive
cfg.get('installation','PREFIX')
cfg.get('installation','prefix')

# Previously read configuration
cfg.get('installation', 'prefix')

# Merge in user-specific configuration
import os
print(cfg.read(os.path.expanduser('~/.config.ini'))
print(cfg.get('installation', 'prefix'))
print(cfg.get('installation', 'library'))
print(cfg.getboolean('debug', 'log_errors'))
print(cfg.get('installation','library'))
cfg.set('installation','prefix','/tmp/dir')
print(cfg.get('installation','library'))
