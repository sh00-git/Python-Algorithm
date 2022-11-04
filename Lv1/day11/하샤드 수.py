# https://school.programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    return x % sum(map(lambda x: int(x), list(str(x)))) == 0