
import logging

def main():
    # Configure the logging system
    logging.basicConfig(
            filename='app.log',
            level=logging.ERROR
        )
 
    # Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'
    
    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

if __name__ == '__main__':
    main()

# change the output level
logging.basicConfig(
         filename='app.log',
         level=logging.WARNING,
         format='%(levelname)s:%(asctime)s:%(message)s')


import logging
import logging.config

# get the logging config from a config file
def main():
    # Configure the logging system
    logging.config.fileConfig('logconfig.ini')

# will send messages to std output
logging.basicConfig(level=logging.INFO)
# basicConfig can only be called once in you program
# if you want to call it again do this top get root logger
logging.getLogger().level = logging.DEBUG