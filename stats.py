def count_words (text):
    words = text.split()
    return len(words)

def count_characters (text):
    character_dict = {}
    for character in text:
        character.lower()
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict
