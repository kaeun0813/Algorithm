#최빈값이 하나만 나온다면,, statistics의 mode를 사용해서 해결...
"""
import statistics
def sol(array):
    return statistics.mode(array)
"""
from collections import Counter
def solution(array):
    counter =Counter(array)
    freq= counter.most_common()
    if len(freq)>1 and freq[0][1]==freq[1][1]:
        return -1
    return freq[0][0]
