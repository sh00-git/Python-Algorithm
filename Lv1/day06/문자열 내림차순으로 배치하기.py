# https://school.programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    return ''.join(sorted(s, reverse=True))
    ## 문자열을 sorted하면 정렬된 하나의 문자들의 리스트가 반환되므로 join을 써서 다시 문자열로 만들어준다.