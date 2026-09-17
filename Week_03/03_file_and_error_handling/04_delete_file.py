
import os

file_path = r"E:\python\Week_03\03_file_and_error_handling\data.txt"

# if os.path.exists(file_path):
#     os.remove(file_path)
#     print("File deleted successfully.")
# else:
#     ("File doesn't exist.")

# <------------------ Second way ------------------>
from pathlib import Path

file_path = Path(__file__).parent / "data.txt"

if file_path.exists():
    Path.unlink(file_path)
    print("File deleted successfully.")
else:
    ("File doesn't exist.")
