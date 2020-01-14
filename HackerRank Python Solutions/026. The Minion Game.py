# The Minion Game in Python:
def minion_game(string):
    Vowels = frozenset('AEIOU')
    Kevin_score = 0
    Stuart_score = 0
    for i in range(len(s)):
        if s[i] in Vowels:
            Kevin_score += (len(s)-i)
        else:
            Stuart_score += (len(s)-i)

    if Kevin_score > Stuart_score:
        print("Kevin", Kevin_score)
    elif Stuart_score > Kevin_score:
        print("Stuart", Stuart_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
