from stats import count_words
from stats import count_characters
from stats import sort_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text
    
def main():
    filepath = './books/frankenstein.txt'
    text = get_book_text(filepath)
    word_count = count_words(text)
    char_count = count_characters(text)
    sorted_char = sort_char_count(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("---------------Word Count---------------")
    print(f"Found {word_count} total words")
    print("---------------Character Count---------------")

    for char_dict in sorted_char:
        char = char_dict["character"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("================END===================")


main()