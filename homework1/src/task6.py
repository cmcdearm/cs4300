import re 



def count_words(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    # Return the number of words in text
    return len(re.findall(r'\b\w+\b', text))