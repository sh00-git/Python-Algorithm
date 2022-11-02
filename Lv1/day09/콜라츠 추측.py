# https://school.programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    n = 0
    while n < 500:
        if num == 1:
            break
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        n += 1
    if n == 500:
        return -1
    return n