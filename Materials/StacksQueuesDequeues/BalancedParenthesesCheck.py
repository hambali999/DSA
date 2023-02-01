def balance_check(s):
    # print(s)

    
    closeToOpen = {')': '(', '}': '{', ']': '['}
    stack = []

    for x in s:
        if x in closeToOpen:
            if stack and stack[-1] == closeToOpen[x]:
                stack.pop()
            else:
                return False
        else:
            stack.append(x)

    if stack == []:
        return True
    else:
        return False




# print(balance_check("[]()(())[]]"))


def checker(s):
    
    closeToOpen = {")":"(", "]":"[", "}":"{"}
    stack = []

    for x in s:
        if x in closeToOpen:
            if stack and stack[-1] == closeToOpen[x]:
                stack.pop()
            else:
                return False
        else:
            stack.append(x)

    if stack == []:
        return True
    else: 
        return False


print(checker("([])"))
