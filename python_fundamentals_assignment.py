# Q1. Data Sorting and Ranking
# Setup Code
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93},
]
# Expected Task: Sort the list of dictionaries by grade in descending order and add a "rank" key to each dictionary based on the sorting.
sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
for i, student in enumerate(sorted_students):
    student["rank"] = i + 1
for student in sorted_students:
    print(student)
# ---------------------------------
# Q2. Merging Data from Two Lists
# Setup Code
employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]
# Expected Task: Merge these lists into a single list of dictionaries by matching the "id" field, including all keys.
merged = [
    {**employee, **salary}
    for employee in employees
    for salary in salaries
    if employee["id"] == salary["id"]
]
print(merged)
# ---------------------------------
# Q3. Advanced Filtering with Multiple Conditions
# Setup Code
products = [
    {"id": 1, "category": "Electronics", "price": 850},
    {"id": 2, "category": "Furniture", "price": 1200},
    {"id": 3, "category": "Electronics", "price": 400},
]
# Expected Task: Filter the list to include only products in the "Electronics" category with a price less than 500.
filtered_products = [
    product
    for product in products
    if product["category"] == "Electronics" and product["price"] < 500
]
print(filtered_products)
# ---------------------------------
# Q4. Complex Data Transformation
# Setup Code
orders = [
    {
        "order_id": 1,
        "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}],
    },
    {
        "order_id": 2,
        "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}],
    },
]
# Expected Task: Transform this list into a dictionary where keys are product names and values are total quantities ordered across all orders.
product_quantities = {}
for order in orders:
    for item in order["items"]:
        product = item["product"]
        quantity = item["quantity"]
        if product in product_quantities:
            product_quantities[product] += quantity
        else:
            product_quantities[product] = quantity
print(product_quantities)
# ---------------------------------
# Q5. Data Consolidation and Summarization
# Setup Code
transactions = [
    {"date": "2021-01-01", "amount": 100, "category": "Food"},
    {"date": "2021-01-01", "amount": 200, "category": "Transport"},
    {"date": "2021-01-02", "amount": 150, "category": "Food"},
]
# Expected Task: Summarize the total amount spent per category.
category_totals = {transaction["category"]: 0 for transaction in transactions}
for transaction in transactions:
    category_totals[transaction["category"]] += transaction["amount"]
print(category_totals)
# ---------------------------------
# Q6. Grouping and Aggregating Data
# Setup Code
sales = [
    {"salesperson": "Alice", "amount": 200},
    {"salesperson": "Bob", "amount": 150},
    {"salesperson": "Alice", "amount": 100},
]
# Expected Task: Group sales by salesperson and calculate the total sales amount for each.
total_sales = {}
for sale in sales:
    salesperson = sale["salesperson"]
    amount = sale["amount"]

    if salesperson in total_sales:
        total_sales[salesperson] += amount
    else:
        total_sales[salesperson] = amount
print(total_sales)
# ---------------------------------
# Q7. Lambda Functions for Spell Power
# Setup Code
spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]
# Expected Task: Sort the spells list by power level in descending order using a lambda function.
sorted_spells = sorted(spells, key=lambda x: x[1], reverse=True)
print(sorted_spells)
# ---------------------------------
# Q8. Map Transformation for Potion Ingredients
# Setup Code
ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]
# Expected Task: Use `map` to append ": 3 grams" to each ingredient.
ingredients_with_quantity = list(map(lambda x: x + ": 3 grams", ingredients))
print(ingredients_with_quantity)
# ---------------------------------
# Q9. Magical Book Filter and Formatter
# Setup Code
books = [
    {"title": "A History of Magic", "pages": 100},
    {"title": "Magical Drafts and Potions", "pages": 150},
]
# Expected Task: Filter books with more than 120 pages and format their titles to uppercase.
filtered_and_formatted_titles = [
    book["title"].upper() for book in books if book["pages"] > 120
]
print(filtered_and_formatted_titles)


# ---------------------------------
# Q10. Wizard Duel Game Class
# Setup Code
# Expected Task: Implement a class with methods for casting spells, reducing health points, and determining the winner.
class WizardDuel:
    spell_damage = 10

    def __init__(self, wizard1, wizard2):
        self.wizard1 = wizard1
        self.wizard2 = wizard2

    def cast_spell(self, wizard):
        wizard.health -= self.spell_damage
        # print(f"{wizard.name} casts a spell and deals {self.spell_damage} damage.")

    def duel(self):
        while self.wizard1.health > 0 and self.wizard2.health > 0:
            self.cast_spell(self.wizard2)
            if self.wizard2.health <= 0:
                print(
                    f"After a duel between {self.wizard1.name} and {self.wizard2.name}, {self.wizard1.name} wins with {self.wizard1.health} health points left."
                )
                break

            self.cast_spell(self.wizard1)
            if self.wizard1.health <= 0:
                print(
                    f"After a duel between {self.wizard1.name} and {self.wizard2.name}, {self.wizard2.name} wins with {self.wizard2.health} health points left."
                )
                break


class Wizard:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health


harry = Wizard("Harry")
draco = Wizard("Draco")
duel = WizardDuel(harry, draco)
duel.duel()


# ---------------------------------
# Q11. Custom Error Handling in Potion Making
# Setup Code
# Expected Task: Define a `PotionError` exception and use it in a potion-making function.
class PotionError(Exception):
    """Exception raised for errors in potion making."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def love_potion(ingredient):
    valid_ingredients = ["Rose Petals", "Unicorn Tears", "Butterfly Wings"]

    if ingredient not in valid_ingredients:
        raise PotionError(
            f"'{ingredient}' is not a valid ingredient for the Love Potion."
        )
    else:
        return "Love potion successfully brewed!"


try:
    ingredient = "Eye of Newt"
    result = love_potion(ingredient)
    print(result)
except PotionError as e:
    print("Caught PotionError:", e)
# ---------------------------------
# Q12. Hogwarts Library Database Query
# Setup Code
library = [
    {"title": "Unfogging the Future", "author": "Cassandra Vablatsky"},
    {"title": "Magical Hieroglyphs and Logograms", "author": "Bathilda Bagshot"},
]
# Expected Task: Use a list comprehension to select books written by Bathilda Bagshot.
bathildas_books = [book for book in library if book["author"] == "Bathilda Bagshot"]
print(bathildas_books)
# ---------------------------------
# Q13. Hogwarts House Points Calculator
# Setup Code
house_points = [
    {"house": "Gryffindor", "points": 35},
    {"house": "Slytherin", "points": 50},
    {"house": "Gryffindor", "points": 60},
    {"house": "Slytherin", "points": 40},
]
# Expected Task: Aggregate points for each house and print the total.
house_totals = {
    house: sum(entry["points"] for entry in house_points if entry["house"] == house)
    for house in set(entry["house"] for entry in house_points)
}
print(house_totals)


# ---------------------------------
# Q14. Class Inheritance for Magical Creatures
# Setup Code
# Expected Task: Create a base class `MagicalCreature` and subclasses `Dragon`, `Unicorn`. Each subclass should have a unique `sound` method.
class MagicalCreature:
    def sound(self):
        raise NotImplementedError("Subclasses must implement the sound method")


class Dragon(MagicalCreature):
    def sound(self):
        return "Roar"


class Unicorn(MagicalCreature):
    def sound(self):
        return "Neigh"


dragon = Dragon()
unicorn = Unicorn()

print(dragon.sound())
print(unicorn.sound())
# ---------------------------------
# Q15. Custom Sorting with Lambda for Magical Artifacts
# Setup Code
artifacts = [
    {"name": "Cloak of Invisibility", "age": 657, "power": 9.5},
    {"name": "Elder Wand", "age": 1000, "power": 10},
    {"name": "Resurrection Stone", "age": 800, "power": 7},
]
# Expected Task: Sort the artifacts first by age, then by power, using a lambda function.
sorted_artifacts = sorted(artifacts, key=lambda x: (x["age"], x["power"]))
print(sorted_artifacts)
# ---------------------------------
# Q16. Wizard Profile Generator with f-strings
# Setup Code
wizard = {"name": "Albus Dumbledore", "title": "Headmaster", "house": "Gryffindor"}
# Expected Task: Use an f-string to create a profile string that includes the wizard's name, title, and house.
profile = f"'{wizard['name']}, the {wizard['title']} of {wizard['house']}.'"
print(profile)
# ---------------------------------
# Q17. Magical Creature Adoption Matching
# Setup Code
adopters = [("Harry", "Phoenix"), ("Hermione", "House Elf")]
creatures = [("Fawkes", "Phoenix"), ("Dobby", "House Elf"), ("Buckbeak", "Hippogriff")]
# Expected Task: Use `filter` and `map` to create a list of matches between adopters and creatures.
matches = filter(
    lambda adopter: any(creature[1] == adopter[1] for creature in creatures), adopters
)
matched_list = list(
    map(
        lambda match: (
            match[0],
            [creature[0] for creature in creatures if creature[1] == match[1]][0],
        ),
        matches,
    )
)
print(matched_list)
# ---------------------------------
# Q18. Advanced Potion Making with Nested Loops
# Setup Code
ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]


# Expected Task: For each pair of ingredients, print out the unique potion they produce.
def unique_potion(ingredient1, ingredient2):
    if ingredient1 == "Moonstone" and ingredient2 == "Silver Dust":
        return "Visibility Potion"
    elif ingredient1 == "Silver Dust" and ingredient2 == "Dragon Blood":
        return "Strength Potion"
    elif ingredient1 == "Moonstone" and ingredient2 == "Dragon Blood":
        return "Fireproof Potion"
    else:
        return "Unknown Potion"


for i in range(len(ingredients)):
    for j in range(i + 1, len(ingredients)):
        ingredient1 = ingredients[i]
        ingredient2 = ingredients[j]
        potion = unique_potion(ingredient1, ingredient2)
        print(f"Combining {ingredient1} and {ingredient2} produces a {potion}.")
# ---------------------------------
# Q19. Nested Data Manipulation
# Setup Code
data = [
    {"id": 1, "name": "Item 1", "tags": ["tag1", "tag2"]},
    {"id": 2, "name": "Item 2", "tags": ["tag2", "tag3"]},
    {"id": 3, "name": "Item 3", "tags": ["tag1", "tag3"]},
]
# Expected Task: For each item, add a new tag "tag4" only if "tag1" is present in the tags list.
data_tag4 = [
    {**item, "tags": item["tags"] + ["tag4"]} if "tag1" in item["tags"] else item
    for item in data
]
print(data_tag4)
# ---------------------------------
# Q20. Implementing a Custom Sort Function
# Setup Code
tasks = [
    {"id": 1, "priority": "High", "completed": False},
    {"id": 2, "priority": "Low", "completed": True},
    {"id": 3, "priority": "Medium", "completed": False},
]
# Expected Task: Sort the tasks by "completed" status (False first) and then by priority ("High", "Medium", "Low").
sorted_tasks = sorted(
    tasks,
    key=lambda x: (x["completed"], {"High": 0, "Medium": 1, "Low": 2}[x["priority"]]),
)
print(sorted_tasks)
