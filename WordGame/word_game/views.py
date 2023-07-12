from django.shortcuts import render, redirect
from .service import all_comp_words, add_word


my_words = []
comp_words = []
LONG_WORD = ''


def check_user_words(my_arr, comp_arr):
    text = f'Количество твоих слов: {len(my_arr)}, компьютера: {len(comp_arr)}. '
    if len(my_arr) > len(comp_arr):
        return f'{text} Вы победили!'
    elif len(my_arr) < len(comp_arr):
        return f'{text} Вы проиграли!'
    else:
        return f'{text} Ничья!'


def main(request):
    global LONG_WORD
    if request.method == 'POST':
        LONG_WORD = request.POST.get('long_word')
        return redirect('game')
    return render(request, 'word_game/main.html')


def search_words(arr):
    for word in arr:
        for symbol in word:
            if symbol in LONG_WORD and LONG_WORD.count(symbol) >= word.count(symbol):
                pass
            else:
                break
        else:
            comp_words.append(word)
    if len(comp_words) == 0:
        return 'Я не составил ни одного слова'
    return f"{', '.join(comp_words)}"


def game(request):
    if request.method == 'POST' and 'add' in request.POST:
        word = request.POST.get('word')
        my_words.append(word)
        return redirect('game')
    if request.method == 'POST' and 'check' in request.POST:
        result_search_words = search_words(all_comp_words)
        result_check = check_user_words(my_words, comp_words)
        string_my_words = ', '.join(my_words)
        add_word(my_words)
        context = {'result_search_words': result_search_words, 'result_check': result_check,
                   'string_my_words': string_my_words, 'LONG_WORD': LONG_WORD}
        return render(request, 'word_game/check.html', context=context)
    else:
        context = {'my_word': my_words, 'LONG_WORD': LONG_WORD}
        return render(request, 'word_game/game.html', context=context)

