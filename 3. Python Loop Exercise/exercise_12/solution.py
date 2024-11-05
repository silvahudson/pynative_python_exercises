def fibonacci(n):
    lst_fibonacci = [0, 1]
    for i in range(2, n):
        pre_before = lst_fibonacci[i - 2]
        before = lst_fibonacci[i - 1]
        actual = pre_before + before
        lst_fibonacci.append(actual)
    return lst_fibonacci

if __name__ == '__main__':
    n = 10
    print(fibonacci(n))
                
        