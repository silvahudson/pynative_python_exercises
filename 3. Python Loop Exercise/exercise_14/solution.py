def reverse_number(n):
    string = str(n)
    return int(string[::-1])

if __name__ == '__main__':
    n = 76542
    print(reverse_number(n))