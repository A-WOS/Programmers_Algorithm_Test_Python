def solution(price, money, count):
    answer = sum(price*i for i in range(1, count+1)) - money
    if answer < 0:
        answer = 0
    return answer


print(solution(3, 20, 4))