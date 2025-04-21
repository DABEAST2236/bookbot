def count_words (text):
    words = text.split()
    return len(words)

def count_characters (text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_count(char_count):
    sorted_char_list = []
    for char, count in char_count.items():
        char_dict = {"character": char, "count": count}
        sorted_char_list.append(char_dict)
    def sort_on(dict):
        return dict["count"]
    sorted_char_list.sort(key=sort_on, reverse=True)
    return sorted_char_list