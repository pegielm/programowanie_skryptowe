def first_character(text):
    return text[0]
def first_two_characters(text):
    if len(text) < 2:
        return ""
    return text[:2]
def all_characters_except_first_two(text):
    if len(text) < 2:
        return ""
    return text[2:]
def penultimate_character(text):
    if len(text) < 2:
        return ""
    return text[-2]
def last_three_characters(text):
    if len(text) < 3:
        return ""
    return text[-3:]
def all_characters_in_even_positions(text):
    if len(text) < 2:
        return text
    return text[::2]
def merge_characters_and_duplicate(text):
    resoult = ""
    if len(text)<2:
        return ""
    for i in range(len(text)):
        resoult += first_character(text)+penultimate_character(text)
    return resoult

