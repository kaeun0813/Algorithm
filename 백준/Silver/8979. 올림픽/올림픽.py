n,k=map(int,input().split())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))
array.sort(key=lambda x:(-x[1],-x[2],-x[3]))
rank=[]
num=1
rank.append((array[0][0],num))
for i in range(1,n):

    if array[i][1]==array[i-1][1]:
        if array[i][2]==array[i-1][2]:
            #은메달 수 같을 때
            if array[i][3]==array[i-1][3]:
                #동메달 수 같을 때
                #그 전 num과 동일하게 진행.
                rank.append((array[i][0],num))
                num+=1
            else:
                num+=1
                rank.append((array[i][0],num))
        else:
            num+=1
            rank.append((array[i][0],num))
    else:
        num+=1
        rank.append((array[i][0],num))
    
for j in range (len(rank)):
    if rank[j][0]==k:
        print(rank[j][1])
