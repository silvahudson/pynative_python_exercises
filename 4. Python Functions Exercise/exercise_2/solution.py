def func1(*args):
    print('Printing values:')
    for i in args:
        print(i)

if __name__ == '__main__':
    func1(1)
    func1(2, 3, 4)
    
    