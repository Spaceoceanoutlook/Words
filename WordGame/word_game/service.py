with open('word_game/DB.txt', 'r', encoding='utf-8') as f:
    all_comp_words = [line[:-1] for line in f.readlines()]