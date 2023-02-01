def main(n):

    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n
    



print(main(942))