def calorie_count(weight, goal, active, gender):
    if goal == 'L':
        return (weight * (7 + (active*2))) * gender
    elif goal == 'G':
        return (weight * (12 + (active*2))) * gender
    elif goal == 'C':
        return (weight * (11 + (active*2))) * gender
    elif goal == 'M':
        return (weight * (9 + (active*1.5))) * gender
    elif goal == 'S':
        return (weight * (15 + (active*2))) * gender
