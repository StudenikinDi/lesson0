numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
sum_ = 0
for i in numbers:
    sum_ = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sum_ += 1
            if sum_ > 2:
                break
    if sum_ > 2:
        not_primes.append(i)
    elif sum_ == 2:
        primes.append(i)
print(primes)
print(not_primes)