def solution(num_list):
    even, odd = '', ''
    for i in num_list:
        if i % 2:
            odd += str(i)
        else:
            even += str(i)
    answer = int(odd) + int(even)
    return answer


print(solution([3, 4, 5, 2, 1]))  # 393
print(solution([5, 7, 8, 3]))  # 581

