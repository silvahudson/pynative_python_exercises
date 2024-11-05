def pattern(n, pattern):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(pattern, end = ' ')
        print('')
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(pattern, end = ' ')
        print('')

if __name__ == '__main__':
    pattern(n = 5, pattern = '*')
    