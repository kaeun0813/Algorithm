n=int(input())
w=[]
max=0
for i in range(n):
    w.append(int(input()))
w.sort(reverse=True)

for i in range(n):
    if w[i]*(i+1)>=max:
        max=w[i]*(i+1)
        #print ("if 문 안",max)
print(max)