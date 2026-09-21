def generate(A, gamma0, N):
    result = []
    result.append(gamma0)
    for _ in range(N - 1):
        x = A * result[-1]
        x = x - int(x)
        result.append(x)
    return result

# print(generate(5**17, 2**-40, 100))
# nums = generate(5**17, 2**-40, 100)
# avg = sum(nums) / len(nums)
# print(avg)

# var = sum((x - avg) ** 2 for x in nums) / (len(nums) - 1)
# print(var)

