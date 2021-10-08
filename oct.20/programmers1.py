def solution(n):
    # answer = n-1
    answer = []
    for val in range(1, n):
        if n % val == 1:
            answer.append(val)
    return min(answer)


print(solution(12))
