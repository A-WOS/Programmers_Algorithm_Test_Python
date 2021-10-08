def solution(numbers):
    # answer = set(range(10))
    answer = [i for i in range(10)]
    for i in numbers:
        answer.remove(i)
    return sum(answer)
numbers = [1, 2, 3, 4, 6, 7, 8, 0]
# print(numbers)
print(solution(numbers))
