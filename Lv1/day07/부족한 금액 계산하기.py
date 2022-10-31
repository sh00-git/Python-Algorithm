# https://school.programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    total = 0
    for c in range(1, count+1):
        total += price * c
    if total > money:
        return total - money
    return 0