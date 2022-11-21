# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    max_0 = max(sizes[0])
    max_1 = min(sizes[0])
    
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        if size[0] > max_0:
            max_0 = size[0]
        if size[1] > max_1:
            max_1 = size[1]
    
    return max_0 * max_1