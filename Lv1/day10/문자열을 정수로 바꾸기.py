# https://school.programmers.co.kr/learn/courses/30/lessons/12925
def solution(s):
    return int(s[1:]) * (-1) if s[0] == '-' else int(s)

# 파이썬은 숫자 앞 부호를 인식함.
def solution(s):
    return int(s)