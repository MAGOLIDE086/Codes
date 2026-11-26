def count_vowels(given_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0 
    
    for char in given_string:
        if char in vowels:
            count = count + 1
        else:
            continue
        
    return count

given_string = "we are the best music lovers"

print(count_vowels(given_string))