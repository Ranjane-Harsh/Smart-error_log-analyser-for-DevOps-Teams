import re
import os

file_path = r"D:\Coding\Vs code\Projects\Smart Error Log Analyser For DevOps Teams\test_Main.txt"

def read_log_file(path):
    if not os.path.exists(path):
        print(f"Error: File not found at {path}")
        return []
    
    with open(path, "r") as file:
        lines = file.readlines()
        cleaned_strings = [line.strip() for line in lines]

        return cleaned_strings

cleaned_strings = read_log_file(file_path)
print("This is the list of Cleaned strings which are striped off whitespaces: ")
print(cleaned_strings)


def extract_error_lines(cleaned_strings):
    error_lines = [line for line in cleaned_strings if '[ERROR]' in line or '[WARNING]' in line]
    return error_lines

error_lines = extract_error_lines(cleaned_strings)
print("This is a list of error lines: ")
print(error_lines)


def normalize_error_lines(error_lines):
    cleaned_lines = []
    for line in error_lines:
        cleaned_line = re.sub(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}|ID:\s*\d+|\/[\w\/\.-]+|\\b\\d+\\b|\d+s?|[^\w\s]', '', line)
        cleaned_lines.append(cleaned_line.strip())
    return cleaned_lines

cleaned_lines = normalize_error_lines(error_lines)
print("This is a list of error lines without the timestamps and ID's")
print(cleaned_lines)