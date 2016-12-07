def calorie_count(weight, goal, active, gender):
    if goal == 'L':
        return (weight * (7 + (active*2))) * gender
    elif goal == 'G':
        return (weight * (12 + (active*1.6))) * gender
    elif goal == 'C':
        return (weight * (9 + (active*2.5))) * gender
    elif goal == 'M':
        return (weight * (9 + (active*1.5))) * gender
    elif goal == 'S':
        return (weight * (15 + (active*2))) * gender


def protein_count(weight, goal, active, gender):
    if goal == 'L':
        return (weight * (.4 + (active/100))) * (gender -.2)
    elif goal == 'G':
        return (weight * (.75 + (active/100))) * gender
    elif goal == 'C':
        return (weight * (.55 + (active/100))) * gender
    elif goal == 'M':
        return (weight * (.4 + (active/100))) * gender
    elif goal == 'S':
        return (weight * (.65 + (active/100))) * gender

def carbs_count(weight, goal, active, gender):
    if goal == 'L':
        return (100 + (weight/2) + (active*10)) * gender
    elif goal == 'G':
        return (140 + (weight/2) + (active*10)) * gender
    elif goal == 'C':
        return (180 + (weight/2) + (active*10)) * gender
    elif goal == 'M':
        return (140 + (weight/2) + (active*10)) * gender
    elif goal == 'S':
        return (200 + (weight/2) + (active*10)) * gender
