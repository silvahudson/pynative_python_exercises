def print_odd(lst):
    for i in lst[1::2]:
        print(i, end = ' ')
    
if __name__ == '__main__':
    lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print_odd(lst)
    