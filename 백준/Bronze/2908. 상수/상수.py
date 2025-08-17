a, b = map(int, input().split())

if int(str(a)[::-1]) > int(str(b)[::-1]):
    print(int(str(a)[::-1])) 
else: 
    print(int(str(b)[::-1])) 
