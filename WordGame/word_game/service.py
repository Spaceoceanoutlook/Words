def open_words():
    with open('word_game/DB.txt', 'r', encoding='utf-8') as f:
        return [line[:-1] for line in f.readlines()]


def add_word(arr):
    with open('word_game/DB.txt', 'a', encoding='utf-8') as file:
        for word in arr:
            if word not in all_comp_words:
                file.writelines(word)
                file.write('\n')


all_comp_words = open_words()
