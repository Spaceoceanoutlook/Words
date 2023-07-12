from django.shortcuts import render, redirect
from .service import all_comp_words, add_word, check_user_words, search_words, \
    comp_words, my_words_list, my_words


LONG_WORD = ''


def main(request):
    global LONG_WORD
    if request.method == 'POST':
        LONG_WORD = request.POST.get('long_word')
        return redirect('game')
    return render(request, 'word_game/main.html')


def game(request):
    if request.method == 'POST' and 'add' in request.POST:
        word = request.POST.get('word')
        my_words_list(word)
        return redirect('game')
    if request.method == 'POST' and 'check' in request.POST:
        result_search_words = search_words(all_comp_words, LONG_WORD)
        result_check = check_user_words(my_words, comp_words)
        string_my_words = ', '.join(my_words)
        add_word(my_words)
        context = {'result_search_words': result_search_words, 'result_check': result_check,
                   'string_my_words': string_my_words, 'LONG_WORD': LONG_WORD}
        return render(request, 'word_game/check.html', context=context)
    else:
        context = {'my_word': my_words, 'LONG_WORD': LONG_WORD}
        return render(request, 'word_game/game.html', context=context)
