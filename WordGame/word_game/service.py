def open_words():
    with open('word_game/DB.txt', 'r', encoding='utf-8') as f:
        return [line[:-1] for line in f.readlines()]


def add_word(arr: list):
    with open('word_game/DB.txt', 'a', encoding='utf-8') as file:
        for word in arr:
            if word not in all_comp_words:
                file.writelines(word)
                file.write('\n')


def check_user_words(my_arr: list, comp_arr: list):
    text = f'Количество твоих слов: {len(my_arr)}, компьютера: {len(comp_arr)}. '
    if len(my_arr) > len(comp_arr):
        return f'{text} Вы победили!'
    elif len(my_arr) < len(comp_arr):
        return f'{text} Вы проиграли!'
    else:
        return f'{text} Ничья!'


def search_words(arr: list, value: str):
    for word in arr:
        for symbol in word:
            if symbol in value.lower() and value.lower().count(symbol) >= word.count(symbol):
                pass
            else:
                break
        else:
            comp_words.append(word)
    if len(comp_words) == 0:
        return ['Я', 'не', 'составил', 'ни', 'одного', 'слова']
    return comp_words


def my_words_list_add(word: str):
    if word.lower() not in my_words:
        my_words.append(word)
    else:
        return 'Такое слово уже есть'
    return None


def my_words_list_cancel():
    del my_words[-1]


def open_records():
    with open('word_game/records.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        if data:
            user, comp = data
            return int(user), int(comp)
        return 0, 0


def save_records(user: int, comp: int, value: str):
    with open('word_game/records.txt', 'w', encoding='utf-8') as f:
        if len(my_words) > user:
            save_long_word(value)
            f.write(str(len(my_words)))
            f.write('\n')
        else:
            f.write(str(user))
            f.write('\n')
        if len(comp_words) > comp:
            f.write(str(len(comp_words)))
        else:
            f.write(str(comp))


def save_long_word(long_word: str):
    with open('word_game/long_word.txt', 'w', encoding='utf-8') as f:
        f.write(long_word)


def open_long_word():
    with open('word_game/long_word.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        return ''.join(data)


class SaveLongWord:
    LONG_WORD = None

    @classmethod
    def __init__(cls, word: str):
        cls.LONG_WORD = word.capitalize()


all_comp_words = open_words()
comp_words = []
my_words = []


