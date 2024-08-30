# import itertools
# import string
# import pikepdf
# import time

# known_part = "UMES35"
# possible_chars = string.ascii_uppercase + string.digits
# pdf_file_path = "umeshpay.pdf"
# output_file_path = "output.txt"

# def log_to_file(message):
#     with open(output_file_path, "a") as file:
#         file.write(message + "\n")

# start_time = time.time()
# start_message = f"Script started at {time.strftime('%Y-%m-%d %H:%M:%S')}"
# log_to_file(start_message)

# def check_password_on_pdf(pdf_path, password):
#     try:
#         with pikepdf.open(pdf_path, password=password) as pdf:
#             return True
#     except pikepdf.PasswordError:
#         return False
#     except Exception as e:
#         error_message = f"An error occurred: {e}"
#         log_to_file(error_message)
#         return False

# for combination in itertools.product(possible_chars, repeat=2):
#     password = known_part + ''.join(combination)
#     if check_password_on_pdf(pdf_file_path, password):
#         time_taken = time.time() - start_time
#         success_message = f"Password found: {password}. Time taken: {time_taken:.2f} seconds."
#         log_to_file(success_message)
#         # print(success_message)
#         break
# else:
#     log_to_file("Password not found.")
#     # print("Password not found.")

# time_taken = time.time() - start_time
# final_message = f"Script completed. Total time taken: {time_taken:.2f} seconds."
# log_to_file(final_message)
# # print(final_message)




import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    r = requests.get('https://weather.talkpython.fm/api/weather/?city=Berlin&country=DE')
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        logger.info(f'Weather in Berlin: {temperature}')