a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO
#aの素数判定
factor = 2
while factor * factor <= a :
    if a % factor == 0:
        print(str(a),"は素数ではない")
        break
    
    else:
        factor += 1
else:
    if a == 1:
        print(str(a), "は素数ではない")
    else:
        print(str(a),"は素数です")       
     
     
#bの素数判定
factor = 2
while factor * factor <= b:
    if b % factor == 0:
        print(str(b), "は素数ではない")
        break
    else:
        factor += 1
else:
    if b == 1:
        print(str(b),"は素数ではない")
    else:
        print(str(b), "は素数です")     



    
    