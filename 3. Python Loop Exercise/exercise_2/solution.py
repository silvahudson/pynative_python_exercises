def my_pattern(n):
    for i in range(1, n+1):
        for j in range(1, i + 1):
            print(j, end = ' ')
        print('\n')
            
if __name__ == '__main__':
    n = 5
    my_pattern(n)
    