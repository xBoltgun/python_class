def disemvowel(string):
    vowels = 'aeiouAEIOU'
    new_string = ''
    for i in string:

        if i not in vowels:
            new_string+= i 
    return new_string