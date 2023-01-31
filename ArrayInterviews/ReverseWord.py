def rev_word(word):
    word = word.lstrip()
    word = word.rstrip()
    word = word.split()
    print(word)
    print(word[::-1])
    print(' '.join(word[::-1]))


def rev_word1(s):
    return " ".join(reversed(s.split()))

#Or

def rev_word2(s):
    return " ".join(s.split()[::-1])


print(rev_word1('    space before    Hello'))
print(rev_word2('    space before    Hello'))


