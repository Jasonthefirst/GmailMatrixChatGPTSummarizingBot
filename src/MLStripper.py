import re
from bs4 import BeautifulSoup

def clean_html(text):
    # Remove URLs
    text = BeautifulSoup(text, "lxml").text

    text = BeautifulSoup(text, "html.parser").text

    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    # Remove character chains longer than 25
    text = re.sub(r'\b\w{25,}\b', '', text)
    # Remove all non-word characters (everything except numbers, letters, dots, and newlines)
    text = re.sub(r"[^\w\s.]", '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r' +', ' ', text)
    return text