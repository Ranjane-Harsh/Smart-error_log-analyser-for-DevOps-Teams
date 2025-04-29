import re
import os

file_path = r"D:\Coding\Vs code\Projects\Smart Error Log Analyser For DevOps Teams\test2.txt"

def read_log_file(path):
    if not os.path.exists(path):
        print(f"Error: File not found at {path}")
        return []
    
    with open(path, "r") as file:
        lines = file.readlines()
        cleaned_strings = [line.strip() for line in lines]

        return cleaned_strings

cleaned_strings = read_log_file(file_path)
print(cleaned_strings)


def extract_error_lines(cleaned_lines):
    error_lines = [line for line in cleaned_lines if '[ERROR]' in line or '[WARNING]' in line]
    return error_lines

error_lines = extract_error_lines(cleaned_strings)
print(error_lines)


def normalize_error_lines(error_lines):
    cleaned_lines = []
    for line in error_lines:
        cleaned_line = re.sub(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}|ID:\s*\d+', '', line)
        cleaned_lines.append(cleaned_line)
    return cleaned_lines

cleaned_lines = normalize_error_lines(error_lines)
print(cleaned_lines)