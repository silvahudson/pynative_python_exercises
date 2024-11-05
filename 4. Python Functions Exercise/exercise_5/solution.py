def  inner_function(a, b):
    
    def addiction(a, b):
        return a + b 
    
    add = addiction(a, b)
    
    return add + 5

if __name__ == '__main__':
    result = inner_function(5, 10)
    print(result)
    
    