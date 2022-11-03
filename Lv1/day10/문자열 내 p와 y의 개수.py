# https://school.programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    s = s.lower()
    p = y = 0
    for i in range(len(s)):
        if s[i] == 'p':
            p += 1
        elif s[i] == 'y':
            y += 1
    return p == y

# count함수 사용
def solution(s):
    return s.lower().count('p') == s.lower().count('y')