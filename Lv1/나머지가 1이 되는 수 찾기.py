def solution(n):
    min_num = 0

    # 큰 수부터 찾기
    for i in range(n-1, 1, -1):
        if n % i == 1:
            min_num = i

    # 작은 수부터 찾기
    for i in range(1, n, 1):
        if n % i == 1:
            min_num = i
            break

    # 컴프리헨션 사용
    min_num = [i for i in range(1, n) if n % i == 1][0]

    return min_num