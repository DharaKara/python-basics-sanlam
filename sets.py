# string, list, tuple, dictionary, sets
# sets - like lists mutable but unique
# {}

# tech_gadgets_set={'Smartphone','Laptop','Smartwatch','Tablet','Tablet'}
# tech_gadgets_list=['Smartphone','Laptop','Smartwatch','Tablet','Tablet']

# print(tech_gadgets_list)
# print(tech_gadgets_set)

# tech_gadgets_set.add('E-reader')

# more_gadgets=['Drone','Selfiestick']
# tech_gadgets_set.update(more_gadgets)

# tech_gadgets_set.discard('Drone')

# empty_set=set()
# empty_set.add('Quinlan')

# set1={'Gaming','Cycling','Reading'}
# set2={'Swiming','Gaming','Cycling'}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))

# colors = ["red", "blue", 'red', "green", "pink", "blue"]
# uniquecolors=set(colors) # easy
# uniquecolors=set() # hard
# for color in colors:
#   uniquecolors.add(color)
# print(uniquecolors, list(uniquecolors))
# print(list(set(colors)))

outdoor_activities = {'Hiking', 'Cycling', 'Swimming'}
indoor_activities = {'Gaming', 'Reading', 'Cycling'}
activity_gadgets = {'Smartwatch': 'Hiking', 'VR Headset': 'Gaming', 'Smartphone': 'Reading', 'Drone': 'Cycling'}

# Task 1: Find outdoor gadgets
# outdoor_gadgets = set()
# for gadget, activity in activity_gadgets.items():
#   if activity in outdoor_activities:
#     outdoor_gadgets.add(gadget)
# print("Outdoor Gadgets:", outdoor_gadgets)
    
# # Task 2: Find indoor gadgets
# indoor_gadgets = set()
# for gadget, activity in activity_gadgets.items():
#     if activity in indoor_activities:
#         indoor_gadgets.add(gadget)
# print("Indoor Gadgets:", indoor_gadgets)

# # Task 3: Dry
# outdoor_gadgets = {gadget for gadget, activity in activity_gadgets.items() if activity in outdoor_activities}
# print("Outdoor Gadgets:", outdoor_gadgets)

# indoor_gadgets = {gadget for gadget, activity in activity_gadgets.items() if activity in indoor_activities}
# print("Indoor Gadgets:", indoor_gadgets)

# Task 3: Dryer
# def check(activity_gadgets, activities):
#   gadgets=set()
#   for gadget, activity in activity_gadgets.items():
#     if activity in activities:
#       gadgets.add(gadget)
#   return gadgets
# print(check(activity_gadgets, outdoor_activities))
# print(check(activity_gadgets, indoor_activities))

# Task 4 - set comprehension
# def find_gadgets(activity_gadgets, activities):
#   return {gadget for gadget, activity in activity_gadgets.items() if activity in activities}

# outdoor_gadgets = find_gadgets(activity_gadgets, outdoor_activities)
# print("Outdoor Gadgets:", outdoor_gadgets)

# indoor_gadgets = find_gadgets(activity_gadgets, indoor_activities)
# print("Indoor Gadgets:", indoor_gadgets)



