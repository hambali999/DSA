def solution(text, ending):
    # your code here...
    checker = ""
    print(ending[::-1])
    for x in text[::-1]:
        checker+=x
        if checker == ending[::-1]:
            return True
    return False

def solution(string, ending):
    return ending in string[-len(ending):]