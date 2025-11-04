import logging 

# setup 
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format = '%(asctime)s [%(levelname)s] %(message)s'
)