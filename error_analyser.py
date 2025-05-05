import argparse
from utils import read_log_file, extract_error_lines, normalize_error_lines
from log_processor import cluster_error
from report_writer import write_txt_report

def parse_arguments():
    parser = argparse.ArgumentParser(description="Smart Error Log Analyser CLI")
    parser.add_argument('--input',required=True,help="Path to Input Log file")
    parser.add_argument('--output',required=True,help="Path to Output Report file")
    args = parser.parse_args()
    return args 

def main():

    try:
        args = parse_arguments()
        input_file_path = args.input
        output_file_path = args.output

        log_lines = read_log_file(input_file_path)
        '''print("This is the list of Cleaned strings which are striped off whitespaces: ")
        print(log_lines)'''

        error_lines = extract_error_lines(log_lines)
        '''print("This is a list of error lines: ")
        print(error_lines)'''

        cleaned_lines = normalize_error_lines(error_lines)
        '''print("This is a list of error lines without the timestamps and ID's")
        print(cleaned_lines)'''

        clusters = cluster_error(cleaned_lines)
        '''print("These is the dict of clusters: ")
        print(clusters)'''

        for fingerprint, logs in clusters.items():
            print(f"\nFINGERPRINT: {' '.join(fingerprint)}")
            for log in logs:
                print(f"  - {log}")

        write_txt_report(output_file_path, clusters)
        print(f"\n✅ Report successfully written to: {args.output}")

    except FileNotFoundError as fnf_err:
        print(f"❌ File Error: {fnf_err}")

    except PermissionError as perm_err:
        print(f"❌ Permission Error: {perm_err}")

    return

if __name__ == "__main__":
    main()