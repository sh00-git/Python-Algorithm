def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        if signs[i]:
            result += absolutes[i]
        else:
            result += absolutes[i] * (-1)
    return result