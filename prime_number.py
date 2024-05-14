def is_prime(n):
    if not isinstance(n, int) or n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True        

try:
    n = int(input("自然数nを入力してください: "))  
    print(is_prime(n))
except ValueError:
    print("整数を入力してください。")
