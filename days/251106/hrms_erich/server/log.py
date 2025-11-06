import logging 
# configure the app log  
logging.basicConfig(
    filename = "employee_app_logs.log",
    level = logging.INFO,
    format = "%(asctime)s [%(levelname)s] %(message)s"
)