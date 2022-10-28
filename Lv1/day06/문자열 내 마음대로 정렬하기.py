# https://school.programmers.co.kr/learn/courses/30/lessons/12915
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
    ## sorted함수에서 기준으로 정렬하고 싶은 부분을 key로 넘겨준다.
    ## 문자열에 n번째 부분으로 1차 정렬하고 문자열로 한번 더 정렬해준다.