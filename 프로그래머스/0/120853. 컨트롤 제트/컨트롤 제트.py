def solution(s):
    stack=[]
    for ch in s.split():
        if ch =="Z":
            if stack: stack.pop()
        else:
            stack.append(int(ch))
    return sum(stack)