def even_numbers(a, b):
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result 

if __name__ == '__main__':
    res = even_numbers(4, 30)
    print(res)
    
    
    