# https://school.programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    return s.isdigit() if len(s) == 4 or len(s) ==6 else False

## try except를 사용하여 int형 변환 오류가 생긴 경우 False를 반환
def solution(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6