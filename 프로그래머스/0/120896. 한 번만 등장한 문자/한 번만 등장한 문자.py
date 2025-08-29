from collections import Counter

def solution(s):
    counter=Counter(s)
    unique=[ch for ch, cnt in counter.items() if cnt ==1]
    return "".join(sorted(unique))