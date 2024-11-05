def sum_series(n):
    sum = 0
    for i in range(1, n + 1):
        str_num = ''
        for j in range(1, i + 1):
            str_num += '2'
        sum += int(str_num)
    return sum 

if __name__ == '__main__':
    n = 5
    print(sum_series(n))
    