"""
Setup logging module
Log to stdout to let Heroku capture the logs
"""
import logging
import sys

logging.basicConfig(
    level=logging.WARNING,  
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]  
)
