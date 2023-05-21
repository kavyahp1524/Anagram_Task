
def check(S1,S2):
    
    if( sorted(S1)== sorted(S2) ):
        print("\nThe Strings Are Anagram\n")
    else:
        print("\nThe Strings Aren't Anagram\n")


str1 = 'Listen'
str2 = 'Silent'

S1 = str1.lower()
S2 = str2.lower()
check(S1,S2)