# https://school.programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    return [int(str(n)[i]) for i in range(len(str(n))-1, -1, -1)]