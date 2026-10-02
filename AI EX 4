from itertools import permutations

def solve_cryptarithm():
    # Equation: SEND + MORE = MONEY
    letters = 'SENDMOREMONEY'
    unique_letters = list(set(letters))
    
    assert len(unique_letters) <= 10, "Too many unique letters!"
    
    first_letters = {'S', 'M'}
    
    for p in permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, p))
        
        # Leading digits cannot be 0
        if any(mapping[char] == 0 for char in first_letters):
            continue
            
        send = mapping['S']*1000 + mapping['E']*100 + mapping['N']*10 + mapping['D']
        more = mapping['M']*1000 + mapping['O']*100 + mapping['R']*10 + mapping['E']
        money = mapping['M']*10000 + mapping['O']*1000 + mapping['N']*100 +
                mapping['E']*10 + mapping['Y']
        
        if send + more == money:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            print("Mapping:", mapping)
            return

solve_cryptarithm()
