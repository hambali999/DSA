def to_jaden_case(string):
    # ...
    textArr = string.split(" ")
    jadenCaseArr = []
    for word in textArr:
        jadenCaseArr.append(word.capitalize())
        
    return " ".join(jadenCaseArr)

def capitalize(string):
    for x in string.split():
        string = string.replace(x, x.capitalize())
    return string


print(to_jaden_case('JonAh Hill Is A Genius'))
print(capitalize('JonAh Hill Is A Genius'))