def solution(numbers):
    numbers.sort()
    if numbers[0]*numbers[1] <numbers[len(numbers)-1]*numbers[len(numbers)-2]:
        return numbers[len(numbers)-1]*numbers[len(numbers)-2]
    else:
        return numbers[0]*numbers[1]