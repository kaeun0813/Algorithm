def solution(answers):
    ans1=ans2=ans3=0  
    sol1=[1,2,3,4,5]
    sol2=[2,1,2,3,2,4,2,5]
    sol3=[3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if sol1[i%5]==answers[i]:
            ans1+=1
        if sol2[i%8]==answers[i]:
            ans2+=1
        if sol3[i%10]==answers[i]:
            ans3+=1
    answer=[]
    t=max(ans1,ans2,ans3)
    if t==ans1: 
        answer.append(1)
    if t==ans2: 
        answer.append(2)
    if t==ans3: 
        answer.append(3)  
    return answer