# https://school.programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        answer += i
    return answer

# sum함수와 min, max 함수의 사용
def solution(a, b):
    return sum(range(min(a,b), max(a,b)+1))