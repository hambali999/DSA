# Codility challenge for base -2 with the least significative bit at the left.
# 
# In base -2 integers are represented by sequences of bits in the following way.
# Bits are ordered from the least to the most significant. Sequence B of N bits
# represents the number: sum(B[i] * (-2)^i for i = 0..N-1). The empty sequence represents 0.
# Note that such representation is suitable for both positive and negative numbers.

# NOTE: Remember negative division returns the floor. http://python-history.blogspot.mx/2010/08/why-pythons-integer-division-floors.html


# In regular english:
# You are given a binary number in the form of an array in base -2
# Base -2 works in the following way:
# Given an array A = [1,1,0,1,1]
# The number is: 1 + (-2) + 0 + (-8) + 16 = 7. The numbers come from the following operations.
# A[0] * -2 ^ 0 = 1 * 1 = 1
# A[1] * -2 ^ 1 = 1 *-2 = -2
# A[2] * -2 ^ 2 = 0
# A[3] * -2 ^ 3 = 1 *-8 = -8
# A[4] * -2 ^ 4 = 1 *16 = 16

# Given A = [1,1,0,1,1] = 7 (Decimal)
# We have to express now -7 in base -2

# Which would be [1, 0, 0, 1]
# A[0] * -2 ^ 0 = 1 * 1 = 1
# A[1] * -2 ^ 1 = 0
# A[2] * -2 ^ 2 = 0
# A[3] * -2 ^ 3 = 1 *-8 = -8

import math


def solution(bits):
    decimal = getDecimalFromBits(bits)
    bits = getBitsFromDecimal(-decimal)
    return bits
    

def getBitsFromDecimal(number):
    number = -number
    result = []
    while number != 0:
        result.append(number % 2)
        number /=  -2
    
    return result


def getDecimalFromBits(bits):
    result = 0;
    
    for index, bit in enumerate(bits):
        # You can either use math.pow or ** the exponentiation operator
        # Be careful to cover odd indices when using ** operator
        result += bit * int(math.pow(-2, index))
    
    return result

# def test():
    
#     for number in range(0, 20):
        
#         bits = getBitsFromDecimal(number)
#         neg = getBitsFromDecimal(-number)
#         print "Number: %s -> Bits %s  -%s bits: %s" % (number, bits, number, neg)
    