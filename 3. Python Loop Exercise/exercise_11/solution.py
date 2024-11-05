def prime_range(start, end):
    lst_prime = []
    for i in range(start, end):
        divisors = {1, i}
        for j in range(1, (i // 2)  + 1):
            if i % j == 0:
                divisors.add(j)
        if len(divisors) == 2:
            lst_prime.append(i)
    return lst_prime
            
if __name__ == '__main__':
    start = 25
    end = 50
    print(prime_range(25, 50))

            