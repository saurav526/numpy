# Python Logging Module Example

import logging

# Configure logging
logging.basicConfig(
    filename='app.log',          # Log file name
    level=logging.DEBUG,         # Logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Logging messages
logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING message")
logging.error("This is an ERROR message")
logging.critical("This is a CRITICAL message")

print("Logs have been written to app.log")