def naughty_or_nice(data):
    mood = 0
    str1 = 'Nice!'
    str2 = 'Naughty!'
    for month,days in data.items():
        for day,moods in days.items():
            if moods == 'Nice':
                mood +=1
            if moods == 'Naughty':
                mood -=1
    if mood >=0:
        return str1
    else:
        return str2