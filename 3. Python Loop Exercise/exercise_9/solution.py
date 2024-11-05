def my_range(a, b):
    for i in range(a, b + 1, 1):
        print(i)
        
if __name__ == '__main__':
    a, b = -10, -1 
    my_range(a, b)