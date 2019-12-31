# String Validators in Python:

s = input()
for a in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
    print(any(eval("c." + a + "()") for c in s))
