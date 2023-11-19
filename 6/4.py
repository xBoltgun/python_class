def find_senior(lst): 
    max_age = max(a['age'] for a in lst)
    return [a for a in lst if a['age']==max_age]
