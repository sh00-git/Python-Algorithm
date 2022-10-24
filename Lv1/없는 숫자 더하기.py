# https://school.programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):
    return sum([i for i in range(10) if i not in numbers])

# 0~9까지의 숫자가 들어있는 정수 배열 중 없는 숫자를 더해서 반환하는 것이므로
# 0~9의 합인 45에서 numbers의 값을 빼주면 답이 나온다.
def solution(numbers):
    return 45 - sum(numbers)