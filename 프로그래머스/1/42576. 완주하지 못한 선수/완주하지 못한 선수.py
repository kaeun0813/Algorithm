def solution(participant, completion):
    
    #완주자에서 참가자를 뺴고 남은 이름을 출력한다.
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if completion[i]!=participant[i]:
            return participant[i]
    return participant[-1]
            