cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def print_recipe(recipe_name):
    try:
        print(f"\nRecipe for {recipe_name}:")
        print(f"Ingredients list: {cookbook[recipe_name]['ingredients']}")
        print(f"To be eaten for {cookbook[recipe_name]['meal']}.")
        print(f"Takes {cookbook[recipe_name]['prep_time']} minutes of cooking.")
    except KeyError:
        print("This option does not exist, please enter type the corresponding number")

def delete_recipe(recipe_name):
    try:
        del cookbook[recipe_name]
        print("the recipe succesfully deleted!")
    except KeyError:
        print("This option does not exist, please enter a valid recipe name")

def add_recipe(recipe_name, ingredients, meal, prep_time):
    try:
        new_recipe = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
        }
        cookbook[name] = new_recipe
    except:
        print("somthing wrong!")

def print_all():
    print(cookbook.items())


option = ''
while option != 5:
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    if option == 1:
        name = input("enter the name of your recipe: ")
        ingredients = input("enter the ingredients of your recipe: ")
        meal = input("meal: ")
        prep_time = input("enter preparation time: ")
        add_recipe(name, ingredients, meal, prep_time)
    elif option == 2:
        name = input("enter the recipe name that you want to remove: ")  
        delete_recipe(name)
    elif option == 3:
        name = input("enter the recipe name that you want to show: ")
        print_recipe(name)
    elif option == 4:
        print_all()
    option = int(input())
if option == 5:
    print("disconnected!")
