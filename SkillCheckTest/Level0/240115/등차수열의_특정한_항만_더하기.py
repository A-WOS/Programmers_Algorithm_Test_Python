def solution(a, d, included):
    nums, answer = [0] * len(included), 0
    nums[0] = a
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + d

    for j in range(len(nums)):
        if included[j] is True:
            answer += nums[j]
    return answer


print(solution(3, 4, [True, False, False, True, True]))  # 37
print(solution(7, 1, [False, False, False, True, False, False, False]))  # 10
