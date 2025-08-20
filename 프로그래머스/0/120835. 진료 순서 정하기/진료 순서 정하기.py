def solution(emergency):
    # 1) 큰 값일수록 작은 등수(1위) 부여
    rank = {v: i+1 for i, v in enumerate(sorted(emergency, reverse=True))}
    # 2) 원래 순서대로 등수 맵핑
    return [rank[v] for v in emergency]
