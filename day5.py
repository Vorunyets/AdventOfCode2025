# for range in list
#   add to dict with @lowBound @highBound
#   dict = dict.sort
# add ingredient to list and sort
# for ingredient in list
#   for each item in @range
#       if ingredient >= @lowBound, 
#           if igredient <= @highBound
#               @goodIngredients += 1
#               break
#       
import re

def findIngedients(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]  # Empty lines
    
    ingredientRange = []
    ingredients = []

    good = 0

    for each in lines:
        if re.search(r'-',each):
            minValue, maxValue = each.split('-')
            ingredientRange.append({
                "min" :int(minValue),
                "max" :int(maxValue)

            })
        else:
            ingredients.append(int(each))
            
    for ingredient in ingredients:
        for everyRange in ingredientRange:
            if ingredient >= everyRange["min"] and ingredient <= everyRange["max"]:
                good += 1
                break

    
    print(good)




findIngedients('resources/ingredients.txt')