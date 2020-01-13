# The Minion Game in Python

def minion_game(string):
    # your code goes here
    vowels = frozenset('AEIOU')

    kevin_score = 0
    stuart_score = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevin_score += (len(s)-i)
        else:
            stuart_score += (len(s)-i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
