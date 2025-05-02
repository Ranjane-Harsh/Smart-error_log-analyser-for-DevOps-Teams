from utils import normalize_error_lines
from utils import error_lines

cleaned_lines = normalize_error_lines(error_lines)

def generate_error_fingerprint(cleaned_lines):
    tokens = [line.split() for line in cleaned_lines]
    #print("These are the tokens formed :")
    #print(tokens)
    stopwords = ['the', 'to', 'could', 'not', 'at', 'in', 'on', 'is', 'of', 'from', 'and']
    filtered_words = [word for line in tokens for word in line if word.lower() not in stopwords]
    return filtered_words

filtered_words = generate_error_fingerprint(cleaned_lines)
print(filtered_words)