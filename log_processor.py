from utils import normalize_error_lines, read_log_file, extract_error_lines, cleaned_lines, error_lines
from collections import defaultdict

print("These are the cleaned lines with no timestamps or IDs: ")
print(cleaned_lines)

def generate_error_fingerprint(line):
    stopwords = ['the', 'to', 'could', 'not', 'at', 'in', 'on', 'is', 'of', 'from', 'and']
    fingerprint = []
    tokens = line.split()
    fingerprint.extend([word for word in tokens if word.lower() not in stopwords])
    return fingerprint


def cluster_error(cleaned_lines):
    clusters = defaultdict(list)
    for line in cleaned_lines:
        fingerprint = generate_error_fingerprint(line)
        clusters[tuple(fingerprint)].append(line)
    return clusters

clusters = cluster_error(cleaned_lines)
print(clusters)

for fingerprint, logs in clusters.items():
    print(f"\nFINGERPRINT: {' '.join(fingerprint)}")
    for log in logs:
        print(f"  - {log}")