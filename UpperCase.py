import string

text = input()

positions = [] 

for charPosition, char in enumerate(text):
    if char.isupper():
        positions.append(charPosition)
        
print(positions)
