def duplicate_count(text):
    # Your code goes here
    checker = {}
    counter = 0
    print(text)
    for x in text:
        if x.isalpha():
            x = x.lower()
            if x in checker:
                checker[x] = 1
            else:
                checker[x] = 0
        else:
            if x in checker:
                checker[x] = 1
            else:
                checker[x] = 0
    for k,v in checker.items():
        if v == 1:
            counter+=1
    return counter
     
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])