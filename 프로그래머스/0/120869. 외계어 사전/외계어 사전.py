def solution(spell, dic):
    for word in dic:
        if set(word) == set(spell) and len(word) == len(spell):
            return 1
    return 2
