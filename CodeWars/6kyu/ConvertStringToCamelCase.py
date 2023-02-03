#bali ans
def to_camel_case(text):
    if text == "":
        return ""
    print(text.split())
    slist = [x for x in text]
    slist2 = []
    for ch in slist:
        if ch.isalpha():
            slist2.append(ch)
        else:
            slist2.append(" ")
    test = (''.join(slist2))
    hello = [x for x in test.split()]
    print(hello)
    result = f"{hello[0]}"
    for i in range(len(hello)-1):
        result+=hello[i+1].capitalize()
    return result


def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

def to_camel_case(text):
    return ''.join(x if text.index(x) == 0 else x.capitalize() for x in text.replace('-', ' ').replace('_', ' ').split())

