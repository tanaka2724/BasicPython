import math
import random
#問3
def euclid(a, b): 
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
     
    return b

#問4
def coprime(a, b):
    if euclid(a, b) == 1:
        return True
    else:
        return False

a = int(input("自然数aを入力"))
b = int(input("自然数bを入力"))    
print("最大公約数 ", euclid(a, b))  
print("互いに素 ", coprime(a, b))  
   
#extra
def probability(pairs, max):
    coprime_count = 0
    for _ in range(pairs):
        a = random.randint(1, max)
        b = random.randint(1, max)
        if euclid(a, b) == 1:
            coprime_count += 1
    return coprime_count / pairs

pairs = 100000
max = 10000

print("エクストラ問題の確率", probability(pairs, max))
    

