def solution(numbers, k):
    n = len(numbers)
    return numbers[(2 * (k - 1)) % n]