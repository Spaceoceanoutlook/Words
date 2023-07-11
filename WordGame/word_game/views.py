from django.shortcuts import render, redirect
from .service import comp_words


my_words = []
answer = []
LONG_WORD = ''


def check_user_words(arr, comp):
    if len(arr) > len(comp):
        return f'Количество твоих слов: {len(arr)}, компьютера: {len(comp)}. Вы победили!'
    elif len(arr) < len(comp):
        return f'Количество твоих слов: {len(arr)}, компьютера: {len(comp)}. Вы проиграли!'
    else:
        return f'Количество твоих слов: {len(arr)}, компьютера: {len(comp)}. Ничья!'


def main(request):
    global LONG_WORD
    if request.method == 'POST':
        LONG_WORD = request.POST.get('long_word')
        return redirect('game')
    return render(request, 'word_game/main.html')


def search_words():
    for word in comp_words:
        for symbol in word:
            if symbol in LONG_WORD and LONG_WORD.count(symbol) >= word.count(symbol):
                pass
            else:
                break
        else:
            answer.append(word)
    if len(answer) == 0:
        return 'Я не составил ни одного слова'
    return f"{', '.join(answer)}"


def game(request):
    if request.method == 'POST' and 'add' in request.POST:
        word = request.POST.get('word')
        my_words.append(word)
        return redirect('game')
    if request.method == 'POST' and 'check' in request.POST:
        ans = search_words()
        ch = check_user_words(my_words, answer)
        context = {'ans': ans, 'ch': ch, 'my_words': ', '.join(my_words)}
        return render(request, 'word_game/check.html', context=context)
    else:
        context = {'my_word': my_words, 'LONG_WORD': LONG_WORD}
        return render(request, 'word_game/game.html', context=context)





