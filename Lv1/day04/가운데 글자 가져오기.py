# https://school.programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    if len(s) % 2 == 0:
        s = s[len(s)//2 - 1] + s[len(s)//2]
    else:
        s = s[len(s)//2]
    return s