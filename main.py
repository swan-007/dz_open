
with open('recept.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredient_count = int(file.readline())
        ingredient = []
        for _ in range(ingredient_count):
            emp = file.readline().strip().split(' | ')
            product_name, quantity, measure = emp
            ingredient.append({'ingredient_name': product_name,
                              'quantity': quantity,
                              'measure': measure
                              })
        file.readline()
        cook_book[dish_name] = ingredient

print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):







