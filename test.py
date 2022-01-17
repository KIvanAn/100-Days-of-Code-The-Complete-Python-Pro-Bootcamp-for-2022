def get_score(n):
    return sum(i * 50 for i in range(1, n + 1))


print(get_score(5))
