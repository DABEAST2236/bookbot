from stats import count_words
from stats import count_characters
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text
    
def main():
    filepath = './books/frankenstein.txt'
    text = get_book_text(filepath)
    print(f"{count_words(text)} words found in the document")
    print(f"{character_dict} characters found in the document")

main()