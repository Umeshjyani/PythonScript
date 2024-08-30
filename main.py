import itertools
import string
import pikepdf
import time

known_part = "VIKA"
possible_chars = string.ascii_uppercase + string.digits
pdf_file_path = "not2.pdf"
output_file_path = "output.txt"

def log_to_file(message):
    with open(output_file_path, "a") as file:
        file.write(message + "\n")

start_time = time.time()
start_message = f"Script started at {time.strftime('%Y-%m-%d %H:%M:%S')}"
log_to_file(start_message)

def check_password_on_pdf(pdf_path, password):
    try:
        with pikepdf.open(pdf_path, password=password) as pdf:
            return True
    except pikepdf.PasswordError:
        return False
    except Exception as e:
        error_message = f"An error occurred: {e}"
        log_to_file(error_message)
        return False

for combination in itertools.product(possible_chars, repeat=4):
    password = known_part + ''.join(combination)
    if check_password_on_pdf(pdf_file_path, password):
        time_taken = time.time() - start_time
        success_message = f"Password found: {password}. Time taken: {time_taken:.2f} seconds."
        log_to_file(success_message)
        print(success_message)
        break
else:
    log_to_file("Password not found.")
    print("Password not found.")

time_taken = time.time() - start_time
final_message = f"Script completed. Total time taken: {time_taken:.2f} seconds."
log_to_file(final_message)
print(final_message)
