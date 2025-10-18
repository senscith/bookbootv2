def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_char_dict_to_list(count_characters):
    sorted_list = []
    for ch in count_characters:
        sorted_list.append({"char": ch, "num": count_characters[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
