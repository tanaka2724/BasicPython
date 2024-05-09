a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO

r = a % b
while r != 0:
    a = b
    b = r
    r = a % b
    
print(b)    
