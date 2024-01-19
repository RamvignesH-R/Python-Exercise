str=input("Enter a string:\n")
vowels=str.count('a')+str.count('e')+str.count('i')+str.count('o')+str.count('u')
consonant=len(str)-vowels
print(vowels,"are the number of vowels")
print(consonant,"are the number of consonents")