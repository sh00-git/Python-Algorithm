# https://school.programmers.co.kr/learn/courses/30/lessons/12977
from itertools import *
def solution(nums):
    answer = 0
    num_combi = list(combinations(nums, 3))
    for i in range(len(num_combi)):
        condition=True
        num = sum(num_combi[i])
        for j in range(2, int(num**0.5)+1):
            if num % j == 0:
                condition=False
                break
        if condition:
                answer += 1

    return answer