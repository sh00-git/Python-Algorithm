# https://school.programmers.co.kr/learn/courses/30/lessons/12934
import math
def solution(n):
    if int(math.sqrt(n)) ** 2 == n:
        return (int(math.sqrt(n))+1) **2
    return -1

# math 라이브러리 사용하지 않고
# x ** (1/2) == math.sqrt(x)
def solution(n):
    if int(n**(1/2)) ** 2 == n:
        return (n**(1/2)+1) **2
    return -1