# https://school.programmers.co.kr/learn/courses/30/lessons/12921
def solution(n):
    answer = 0
    for i in range(3, n+1):
        condition = True
        for j in range(2, int((i**0.5) + 1)):
            if i % j == 0:
                condition = False
                break
        if condition:
            answer += 1
    return answer+1