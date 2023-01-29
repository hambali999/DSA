import time

# BIG O(1)
tweets = ['hi','my','hello']
tweetsDict = {'hi': 2012, 'my': 2014, 'hello': 2018}

print(tweets[0]) # O(1)
print(tweets[-1]) # O(1)

#print first value in the dict
print(list(tweetsDict.values())[0])

#print first key in the dict
print(list(tweetsDict.keys())[0])


# BIG O(n)
for i in range(len(tweets)):
    t1 = time.time()
    if tweets[i] == 'my':
        break
    t2 = time.time()
    timetaken = t2-t1
print(timetaken)

# BIG O(n ** 2) / BIG O(n^2)
for i in tweets:
    for y in tweets:
        print(i,y)

#loop through dict
for k,v in tweetsDict.items():
    print(k,v)

#loop through dict values 
for i in list(tweetsDict.values()):
    print(i)

#loop through dict keys 
for i in list(tweetsDict.keys()):
    print(i)