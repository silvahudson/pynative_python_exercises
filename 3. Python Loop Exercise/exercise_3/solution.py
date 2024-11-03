def my_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i 
    return sum 

if __name__ == '__main__':
    n = int(input('Enter number: '))
    sum = my_sum(n)
    print(f'Sum is: {sum}')