def count_developers(lst):
    # Your code here
    developers = [ d for d in lst 
                if d['continent'] == 'Europe' 
                and d['language'] == 'JavaScript' ]
    print(developers)
    return len(developers)
    pass