from django.shortcuts import render, redirect

my_word = []
LONG_WORD = None


def main(request):
    global LONG_WORD
    if request.method == 'POST':
        long_word = request.POST.get('long_word')
        LONG_WORD = long_word
        return redirect('game')
    return render(request, 'word_game/main.html')


def game(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        my_word.append(word)
        return redirect('game')
    else:
        context = {'my_word': my_word, 'LONG_WORD': LONG_WORD}
        return render(request, 'word_game/game.html', context=context)


def check(request):
    pass

