# logger.py
import logging
import colorlog

def app_logger():    
    # Create a logger
    logger = logging.getLogger("app_logger")
    
    # Set the default log level
    logger.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(module)s - Line %(lineno)d - %(message)s')

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Set up color formatter for the console output
    color_formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s - %(levelname)s - %(filename)s - %(module)s - Line %(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'white',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'magenta'
        }
    )
    console_handler.setFormatter(color_formatter)
    # Add handlers to the logger
    logger.addHandler(console_handler)

    return logger


app_logger = app_logger()