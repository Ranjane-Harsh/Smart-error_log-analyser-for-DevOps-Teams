from collections import defaultdict

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
