def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]:
            (sizes[i][0],sizes[i][1])=(sizes[i][1],sizes[i][0])
    #print(sizes)
    max_f=max_s=0
    for i in range(len(sizes)):
        if max_f<sizes[i][0]:
            max_f=sizes[i][0]
        if max_s<sizes[i][1]:
            max_s=sizes[i][1]
    #print(max_f,max_s)
    return max_f*max_s