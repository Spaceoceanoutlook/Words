from .models import Word, Save


def open_words():
    words = []
    for i in Word.objects.all():
        words.append(i.word)
    return words


def add_word(arr: list):
    for word in arr:
        if word not in all_comp_words:
            Word.objects.create(word=word)


def check_user_words(my_arr: list, comp_arr: list):
    text = f'Количество ваших слов: {len(my_arr)}, компьютера: {len(comp_arr)}. '
    if len(my_arr) > len(comp_arr):
        return f'{text} Вы победили!'
    elif len(my_arr) < len(comp_arr):
        return f'{text} Вы проиграли!'
    else:
        return f'{text} Ничья!'


def search_words(arr: list, value: str):
    for word in arr:
        if word.lower() == value.lower():
            continue
        for symbol in word:
            if symbol in value.lower() and value.lower().count(symbol) >= word.count(symbol):
                pass
            else:
                break
        else:
            comp_words.append(word)
    return comp_words


def my_words_list_add(word: str, param: str | None):
    if param is None:
        if word.lower() not in my_words:
            my_words.append(word)
        else:
            return 'Такое слово уже есть'
    return None


def check_my_word(word: str, value: str):
    for symbol in word:
        if symbol in value.lower() and value.lower().count(symbol) >= word.count(symbol):
            pass
        else:
            return 'Такое слово составить нельзя'
    return None


def my_words_list_cancel():
    del my_words[-1]


def count_words():
    return f'Количество ваших слов: {len(my_words)}'


def open_records():
    game_info = []
    for i in Save.objects.all():
        game_info.append(i)
    return game_info


def save_this_game(value: str, user: int, comp: int):
    Save.objects.create(long_word=value, player_points=user, comp_points=comp)


class SaveLongWord:
    LONG_WORD = None

    @classmethod
    def __init__(cls, word: str):
        cls.LONG_WORD = word.capitalize()


def delete_seved_game(param: int):
    Save.objects.filter(pk=param).delete()


all_comp_words = open_words()
comp_words = []
my_words = []
