import string

alphabet_up = frozenset(string.ascii_uppercase)

def capital_indexes(text):
    positions = [] 
    for charPosition, char in enumerate(text):
        if char in alphabet_up:
            positions.append(charPosition)
    
    return positions
        
positions = capital_indexes(input())
print(positions)