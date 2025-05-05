import re
import os

def read_log_file(path):
    if not os.path.exists(path):
        print(f"Error: File not found at {path}")
        return []
    
    with open(path, "r") as file:
        lines = file.readlines()
        log_lines = [line.strip() for line in lines]

        return log_lines


def extract_error_lines(cleaned_strings):
    error_lines = [line for line in cleaned_strings if '[ERROR]' in line or '[WARNING]' in line]
    return error_lines


def normalize_error_lines(error_lines):
    cleaned_lines = []
    for line in error_lines:
        cleaned_line = re.sub(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}|ID:\s*\d+|\/[\w\/\.-]+|\\b\\d+\\b|\d+s?|[^\w\s]', '', line)
        cleaned_lines.append(cleaned_line.strip())
    return cleaned_lines

