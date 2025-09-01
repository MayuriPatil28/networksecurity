import sys
from networksecurity.logging.logger import logger   # ✅ imports the logger object

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        _, _, exc_tb = error_detail.exc_info()
        self.error_message = (
            f"Error occured in python script name [{exc_tb.tb_frame.f_code.co_filename}] "
            f"line number [{exc_tb.tb_lineno}] error message [{str(error_message)}]"
        )

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        logger.info("Enter the try block")   # ✅ now works
        x = 1 / 0   # Force error
    except Exception as e:
        logger.error("An exception occurred", exc_info=True)
        raise NetworkSecurityException(e, sys)
