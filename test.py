from hashlib import sha256

x = 5
y = 10  






while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    print(sha256(f'{x*y}'.encode()).hexdigest())
    y += 1
print(sha256(f'{21*5}'.encode()).hexdigest())    
print(f'The solution is y = {y}')