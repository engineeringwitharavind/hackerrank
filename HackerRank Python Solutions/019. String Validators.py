# String Validators in Python:

s = input()
for a in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
    print(any(eval("c." + a + "()") for c in s))

#########################################################################################################################################

# Alternate simple Solution:

str = input()
print(any(c.isalnum() for c in str))
print(any(c.isalpha() for c in str))
print(any(c.isdigit() for c in str))
print(any(c.islower() for c in str))
print(any(c.isupper() for c in str))
