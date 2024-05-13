def is_prime():
    if not n.is_integer() or not n >= 2:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        else:
            return True    
    
n = float(input("自然数nを入力してください"))  
print(is_prime())      
    
    
    
    
    
    
    
    
    
    

    