def rev_word(word):
    word = word.lstrip()
    word = word.rstrip()
    word = word.split()
    print(word)
    print(word[::-1])
    print(' '.join(word[::-1]))


rev_word('    space before')