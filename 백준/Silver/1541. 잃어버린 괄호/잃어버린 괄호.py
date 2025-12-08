data=list((input().split("-")))
result=0
for i in range(len(data)):
    nums=list(data[i].split("+"))
    total=0
    for j in range(len(nums)):
        total+=int(nums[j])
    if i==0:
        result+=total
    else:
        result-=total
    
print(result)