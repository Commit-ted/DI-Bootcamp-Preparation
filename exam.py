from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------
from utils import unzip_with_7z
import string

# Try all combinations of two lowercase letters
for first_letter in string.ascii_lowercase:
    for second_letter in string.ascii_lowercase:
        find_me = first_letter + second_letter
        secret_password = find_me + 'bcmpda'
        
        # Try to unzip the file with the current password
        if unzip_with_7z(zip_file_path, dest_path, secret_password):
            print(f"Password found: {secret_password}")
            break
    else:
        continue
    break
