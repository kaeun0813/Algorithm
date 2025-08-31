def solution(quiz):
    ans = []
    for q in quiz:
        x, op, y, _, z = q.split()
        x, y, z = int(x), int(y), int(z)

        if op == '+':
            ok = (x + y == z)
        else: 
            ok = (x - y == z)

        ans.append("O" if ok else "X")
    return ans
