def square_digits(num):
    # Your code here
    result=[]
    nums = [x for x in str(num)]
    for x in nums:
        result.append(int(x)*int(x))
    s = [str(i) for i in result]   
    res = int("".join(s))
    return res


def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))