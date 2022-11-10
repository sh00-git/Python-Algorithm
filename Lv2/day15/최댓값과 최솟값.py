# https://school.programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    s = list(map(lambda x: int(x), s.split(' ')))
    return f"{min(s)} {max(s)}"

## lambda 사용 x -> map 만 사용
def solution(s):
    s = list(map(int, s.split(' ')))
    return f"{min(s)} {max(s)}"