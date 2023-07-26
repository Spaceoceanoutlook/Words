from django.shortcuts import render, redirect
from .service import all_comp_words, add_word, check_user_words, search_words, \
    comp_words, my_words_list_add, my_words, open_records, save_records, my_words_list_cancel, \
    open_long_word, SaveLongWord, check_my_word, count_words


def main(request):
    my_words.clear()
    comp_words.clear()
    if request.method == 'POST':
        long_word = request.POST.get('long_word')
        SaveLongWord(long_word)
        return redirect('game')
    return render(request, 'word_game/main.html')


def game(request):
    if request.method == 'POST' and 'add' in request.POST:
        word = request.POST.get('word')
        no_passed = check_my_word(word, SaveLongWord.LONG_WORD)
        word_repetition = my_words_list_add(word, no_passed)
        last_elem_in_my_words = my_words[-1]
        context = {'word_repetition': word_repetition, 'no_passed': no_passed,
                   'last_elem_in_my_words': last_elem_in_my_words, 'my_word': my_words,
                   'LONG_WORD': SaveLongWord.LONG_WORD}
        return render(request, 'word_game/game.html', context=context)
    if request.method == 'POST' and 'cancel' in request.POST:
        my_words_list_cancel()
        last_elem_in_my_words = my_words[-1]
        context = {'last_elem_in_my_words': last_elem_in_my_words,
                   'my_word': my_words, 'LONG_WORD': SaveLongWord.LONG_WORD}
        return render(request, 'word_game/game.html', context=context)
    if request.method == 'POST' and 'count' in request.POST:
        text_count = count_words()
        last_elem_in_my_words = my_words[-1]
        context = {'text_count': text_count, 'last_elem_in_my_words': last_elem_in_my_words,
                   'my_word': my_words, 'LONG_WORD': SaveLongWord.LONG_WORD}
        return render(request, 'word_game/game.html', context=context)
    if request.method == 'POST' and 'check' in request.POST:
        user_record_from_txt, comp_record_from_txt = open_records()
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
        save_records(user_record_from_txt, comp_record_from_txt, SaveLongWord.LONG_WORD)
        context = {'result_search_words': result_search_words, 'result_check': result_check,
                   'my_words': my_words, 'LONG_WORD': SaveLongWord.LONG_WORD,
                   'last_elem_in_comp_words': last_elem_in_comp_words,
                   'last_elem_in_my_words': last_elem_in_my_words}
        return render(request, 'word_game/check.html', context=context)
    else:
        context = {'my_word': my_words, 'LONG_WORD': SaveLongWord.LONG_WORD}
        return render(request, 'word_game/game.html', context=context)


def records(request):
    long_word = open_long_word()
    user_record_from_txt, comp_record_from_txt = open_records()
    context = {'user_record_from_txt': user_record_from_txt,
               'comp_record_from_txt': comp_record_from_txt,
               'long_word': long_word}
    return render(request, 'word_game/records.html', context=context)
