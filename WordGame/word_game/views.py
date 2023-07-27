from django.shortcuts import render, redirect
from .service import all_comp_words, add_word, check_user_words, search_words, \
    comp_words, my_words_list_add, my_words, my_words_list_cancel, \
    SaveLongWord, check_my_word, count_words, open_records, save_this_game, delete_seved_game


def main(request):
    my_words.clear()
    comp_words.clear()
    if request.method == 'POST':
        long_word = request.POST.get('long_word')
        SaveLongWord(long_word)
        return redirect('game')
    return render(request, 'word_game/main.html')


def game(request):
    context = {'my_word': my_words, 'LONG_WORD': SaveLongWord.LONG_WORD}
    if request.method == 'POST' and 'add' in request.POST:
        word = request.POST.get('word')
        no_passed = check_my_word(word, SaveLongWord.LONG_WORD)
        word_repetition = my_words_list_add(word, no_passed)
        last_elem_in_my_words = my_words[-1]
        new_context = {'word_repetition': word_repetition, 'no_passed': no_passed,
                       'last_elem_in_my_words': last_elem_in_my_words} | context
        return render(request, 'word_game/game.html', context=new_context)
    if request.method == 'POST' and 'cancel' in request.POST:
        my_words_list_cancel()
        last_elem_in_my_words = my_words[-1]
        new_context = {'last_elem_in_my_words': last_elem_in_my_words} | context
        return render(request, 'word_game/game.html', context=new_context)
    if request.method == 'POST' and 'count' in request.POST:
        text_count = count_words()
        last_elem_in_my_words = my_words[-1]
        new_context = {'text_count': text_count, 'last_elem_in_my_words': last_elem_in_my_words} | context
        return render(request, 'word_game/game.html', context=new_context)
    if request.method == 'POST' and 'check' in request.POST:
        result_search_words = search_words(all_comp_words, SaveLongWord.LONG_WORD)
        result_check = check_user_words(my_words, comp_words)
        add_word(my_words)
        if my_words:
            last_elem_in_my_words = my_words[-1]
        else:
            last_elem_in_my_words = []
        if comp_words:
            last_elem_in_comp_words = comp_words[-1]
        else:
            last_elem_in_comp_words = []
        save_this_game(SaveLongWord.LONG_WORD, len(my_words), len(comp_words))  # сохраняем в БД
        context = {'result_search_words': result_search_words, 'result_check': result_check,
                   'my_words': my_words, 'LONG_WORD': SaveLongWord.LONG_WORD,
                   'last_elem_in_comp_words': last_elem_in_comp_words,
                   'last_elem_in_my_words': last_elem_in_my_words,}
        return render(request, 'word_game/check.html', context=context)
    return render(request, 'word_game/game.html', context=context)


def savedgames(request):
    saved_games = open_records()
    context = {'saved_games': saved_games}
    return render(request, 'word_game/savedgames.html', context=context)


def delete_game(request, pk):
    if request.method == 'GET':
        delete_seved_game(pk)
    return redirect('savedgames')
