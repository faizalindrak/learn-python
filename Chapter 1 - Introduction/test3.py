new_menu = ['Hawaiian', 'Margherita', 'Mushroom', 'Prosciutto', 'Meat Feast', 'Hawaiian', 'Bacon', 'Black Olive Special', 'Sausage', 'Sausage']

final_new_menu = list(set(new_menu))

print(final_new_menu)

def remove_duplicate_with_set(obj_list):
    new_list = []
    for i in obj_list:
      if i not in new_list:
        new_list.append(i)
    return new_list