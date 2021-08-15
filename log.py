import logging
import coloredlogs
import os

os.environ['COLOREDLOGS_LOG_FORMAT'] ='%(asctime)s.%(msecs)03d %(name)s - %(message)s'
os.environ['COLOREDLOGS_DATE_FORMAT'] ='%H:%M:%S'

coloredlogs.install(level='DEBUG')

def logname(name='SynerMychaSim'):
    return logging.getLogger(name)