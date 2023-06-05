

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def display(self):
        print("Username:", self.name)
        print("password:",self.password)
class Ingredient:
    def __init__(self, name):
        self.name = name
    def getname(self):
        return self.name

    def displayIngredients(self):
        print("Ingredients:",self.name)
        
   



class Recipe(Ingredient):
    def __init__(self, name, ingredients, cooking_time, instructions,cooking_method):
        super(). __init__(name)
        self.name= name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.instructions = instructions
        self.cooking_method=cooking_method
        self.nutritionalinformation = None
        self.ratings = []
        self.reviews = []

    def display(self):
        return self.name,self.ingredients, self.cooking_time, self.instructions,self.cooking_method

    def addRating(self, rating):
        self.ratings.append(rating)
        print("Rating added successfully.")

    def addReview(self, review):
        self.reviews.append(review)
        print("Review added successfully.")
    def display_rating(self):
        return self.rating
    def display_review(self):
        
        return self.review
    
class baking(Recipe):
    def __init__(self,name, ingredients, cooking_time, instructions,cooking_method,temperature):
        super(). __init__(name, ingredients, cooking_time, instructions,cooking_method)
        self.temperature=temperature
    def display(self):
        super.display()
        print(self.temperature)

class stove(Recipe):
    def __init__(self,name, ingredients, cooking_time, instructions,cooking_method,pan):
        super(). __init__(name, ingredients, cooking_time, instructions,cooking_method)
        self.pan=pan
    def display(self):
        super.display()
        print(self.pan)

class cooking(Recipe):        
    def __init__(self,name, ingredients, cooking_time, instructions,cooking_method,boiling):
        super(). __init__(name, ingredients, cooking_time, instructions,cooking_method)
        self.boiling=boiling
    def display(self):
        super.display()
        print(self.boiling)        
        
class NutritionMenu:
    def __init__(self):
        self.menu_items = []

    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)

    def calculate_total_nutrition(self):
        total_nutrition_info = {'calories': 0, 'carbohydrates': 0, 'protein': 0, 'fat': 0}

        for menu_item in self.menu_items:
            menu_item_nutrition = menu_item.get_nutrition_info()
            for nutrient in total_nutrition_info:
                total_nutrition_info[nutrient] += menu_item_nutrition[nutrient]

        return total_nutrition_info
   


   

class Rating:
    def __init__(self, user, rating):
        self.user = user
        self.rating = rating

    def getUser(self):
        return self.user

    def getRating(self):
        return self.rating
    def display_rating(self):
        return self.rating
    
    


class Review:
    def __init__(self, user, review):
        self.user = user
        self.review = review

    def getUser(self):
        return self.user

    def getReview(self):
        return self.review
    def display_review(self):
        return self.review


user_accounts = []

recipe_list = []

while True:
    print("1. Login")
    print("2. Sign Up")
    print("3. Ingredient Management")
    print("4. Recipe Management")
    print("5.Nutritional Information:")
    print("6.Search and Filtering Options")
    print("7. Exit")
    option = input("Choose an Option: ")

    if option == "1":
        name = input("Enter your username: ")
        password = input("Enter your password: ")

        found_user = None
        for user in user_accounts:
            if user.name == name and user.password == password:
                found_user = user
                break

        if found_user:
            print("You're logged in.")
            found_user.display()
        else:
            print("Invalid username or password.")

    elif option == "2":
        name = input("Enter your username: ")
        password = input("Enter a password: ")
        user = User(name, password)
        user_accounts.append(user)
        print("Account created successfully.")
    elif option == "3":
        print("Ingredient Management")
        print("1. Add ingredient")
        print("2. Edit ingredient")
        print("3. Delete ingredient")
        print("4. Exit Ingredient Management")
        ingredient_option = input("Choose an Option: ")
        if ingredient_option == "1":
            recipe_choice = input("Enter the number of the recipe to add ingredient: ")
            if recipe_choice.isdigit():
                recipe_choice = int(recipe_choice)
            if 1 <= recipe_choice <= len(recipe_list):
                selected_recipe = recipe_list[recipe_choice - 1]
                ingredient_name = input("Enter ingredient name: ")
                
                ingredient = Ingredient(ingredient_name)
                selected_recipe.addIngredient(ingredient)
            else:
                print("Invalid recipe number.")
        else:
            print("Invalid input.")

        if ingredient_option == "2":
            recipe_choice = input("Enter the number of the recipe to edit ingredient: ")
            if recipe_choice.isdigit():
               recipe_choice = int(recipe_choice)
            if 1 <= recipe_choice <= len(recipe_list):
                selected_recipe = recipe_list[recipe_choice - 1]
                ingredient_name = input("Enter the ingredient name to edit: ")
                selected_recipe.updateIngredient(ingredient_name)
            else:
                print("Invalid recipe number.")
        else:
            print("Invalid input.")

        if ingredient_option == "3":
            recipe_choice = input("Enter the number of the recipe to delete ingredient: ")
            if recipe_choice.isdigit():
                recipe_choice = int(recipe_choice)
            if 1 <= recipe_choice <= len(recipe_list):
                selected_recipe = recipe_list[recipe_choice - 1]
                ingredient_name = input("Enter the ingredient name to delete: ")
                selected_recipe.removeIngredient(ingredient_name)
            else:
                print("Invalid recipe number.")
        else:
            print("Invalid input.")

        if ingredient_option == "4":
            recipe_choice = input("Enter the number of the recipe to display ingredients: ")
            if recipe_choice.isdigit():
               recipe_choice = int(recipe_choice)
            if 1 <= recipe_choice <= len(recipe_list):
                selected_recipe = recipe_list[recipe_choice - 1]
                selected_recipe.displayIngredients()
            else:
                print("Invalid recipe number.")
        else:
            print("Invalid input.")

        if ingredient_option == "5":
            break
        else:
            print("Invalid option. Please try again.")
            continue
    elif option == "4":
        print("Recipe Management")
        print("1. Add Recipe")
        print("2. Edit Recipe")
        print("3. Delete Recipe")
        print("4. Display Recipes")
        print("5. Exit")
        recipe_option = input("Choose an Option: ")
        if recipe_option == "1":
            recipe_name = input("Enter recipe name: ")
            ingredients = []
            cooking_time = input("Enter the cooking time (in minutes): ")

            instructions = input("Enter the recipe instructions: ")
            cooking_method = input("Enter the cooking method (baking, mixing, or using stove): ")
            print("Nutritional information:")
            calories = input("Enter calories: ")
            fat = input("Enter fat: ")
            protein = input("Enter protein: ")
            carbohydrates = input("Enter carbohydrates: ")
            recipe = Recipe(recipe_name, ingredients, cooking_time, instructions, cooking_method)
            recipe.calories = calories
            recipe.fat = fat
            recipe.protein = protein
            recipe.carbohydrates = carbohydrates

            rating = float(input("Rate the recipe (1-5): "))
            review = input("Write a review for the recipe: ")

            recipe.addRating(rating)
            recipe.addReview(review)

            recipe_list.append(recipe)
            print("Recipe added successfully.")            
            
        elif recipe_option == "2":
            if len(recipe_list) == 0:
                print("No recipes available to edit.")
            else:
                print("Select a recipe to edit:")
                for i, recipe in enumerate(recipe_list):
                    print(f"{i + 1}. {recipe.name}")
                recipe_choice = input("Enter the number of the recipe to edit: ")
                if recipe_choice.isdigit():
                    recipe_choice = int(recipe_choice)
                    if 1 <= recipe_choice <= len(recipe_list):
                        selected_recipe = recipe_list[recipe_choice - 1]
                        new_recipe_name = input("Enter new recipe name (leave empty to keep the same): ")
                        if new_recipe_name.strip():
                            selected_recipe.name = new_recipe_name
                        new_ingredients = input("Enter new ingredients (leave empty to keep the same): ")
                        if new_ingredients.strip():
                            selected_recipe.ingredients = new_ingredients
                        new_cooking_time = input("Enter new cooking time (leave empty to keep the same): ")
                        if new_cooking_time.strip():
                            selected_recipe.cooking_time = new_cooking_time
                        new_instructions = input("Enter new recipe instructions (leave empty to keep the same): ")
                        if new_instructions.strip():
                            selected_recipe.instructions = new_instructions
                        print("Recipe updated.")
                    else:
                        print("Invalid recipe number.")
                else:
                    print("Invalid input.")
           

        elif recipe_option == "3":
            if len(recipe_list) == 0:
                print("No recipes available to delete.")
            else:
                print("Select a recipe to delete:")
                for i, recipe in enumerate(recipe_list):
                    print(f"{i + 1}. {recipe.name}")
                recipe_choice = input("Enter the number of the recipe to delete: ")
                if recipe_choice.isdigit():
                    recipe_choice = int(recipe_choice)
                    if 1 <= recipe_choice <= len(recipe_list):
                        del recipe_list[recipe_choice - 1]
                        print("Recipe deleted.")
                    else:
                        print("Invalid recipe number.")
                else:
                    print("Invalid input.")

        elif recipe_option == "4":
            print("Displaying Recipes:")
            for i, recipe in enumerate(recipe_list):
                print(f"{i + 1}. {recipe.name}")
            recipe_choice = input("Enter the number of the recipe to display its information: ")
            if recipe_choice.isdigit():
                recipe_choice = int(recipe_choice)
                if 1 <= recipe_choice <= len(recipe_list):
                    selected_recipe = recipe_list[recipe_choice - 1]
                    print(f"\nDisplaying Recipe: {selected_recipe.name}")
                    print("Cooking Time:", selected_recipe.cooking_time)
                    print("Instructions:", selected_recipe.instructions)
                    print("Cooking Method:", selected_recipe.cooking_method)
                    print("Nutritional Information:")
                    print("Calories:", selected_recipe.calories)
                    print("Fat:", selected_recipe.fat)
                    print("Protein:", selected_recipe.protein)
                    print("Carbohydrates:", selected_recipe.carbohydrates)
                else:
                    print("Invalid recipe number.")
            else:
                print("Invalid input.")
  

        elif recipe_option == "5":
            break
        else:
            print("Invalid option. Please try again.")

    elif option == "5":
        print("Nutritional Information:")
        for i, recipe in enumerate(recipe_list):
            print(f"\n{i + 1}. Recipe: {recipe.name}")
            print(f"Calories: {recipe.calories}")
            print(f"Protein: {recipe.protein}g")
            print(f"Carbohydrates: {recipe.carbohydrates}g")
            print(f"Fat: {recipe.fat}g")
        
    elif option == "6":
        print("Search and Filtering Options")
        print("1. Search by Name")
        print("2. Search by Time")
        print("3. Search by Ingredients")
        print("4. Back")

        search_option = input("Choose an option: ")

        if search_option == "1":
            name = input("Enter the name of the recipe: ")
            found_recipes = []
            for recipe in recipe_list:
                if recipe.name.lower() == name.lower():
                    found_recipes.append(recipe)

            if found_recipes:
                print(f"\nFound {len(found_recipes)} recipe(s) with the name '{name}':")
                for i, recipe in enumerate(found_recipes):
                    print(f"{i + 1}. {recipe.name}")
            else:
                print(f"No recipes found with the name '{name}'.")

        elif search_option == "2":
            time = input("Enter the cooking time: ")
            found_recipes = []
            for recipe in recipe_list:
                if recipe.cooking_time.lower() == time.lower():
                    found_recipes.append(recipe)

            if found_recipes:
                print(f"\nFound {len(found_recipes)} recipe(s) with cooking time '{time}':")
                for i, recipe in enumerate(found_recipes):
                        print(f"{i + 1}. {recipe.name}")
            else:
                print(f"No recipes found with cooking time '{time}'.")
            
        elif search_option == "3":
            ingredient = input("Enter an ingredient: ")
            found_recipes = []
            for recipe in recipe_list:
                for recipe_ingredient in recipe.ingredients:
                    if ingredient.lower() in recipe_ingredient.lower():
                        found_recipes.append(recipe)
                        break

            if found_recipes:
                print(f"\nFound {len(found_recipes)} recipe(s) containing the ingredient '{ingredient}':")
                for i, recipe in enumerate(found_recipes):
                    print(f"{i + 1}. {recipe.name}")
            else:
                print(f"No recipes found containing the ingredient '{ingredient}'.")
            

        elif search_option == "4":
            continue

        else:
            print("Invalid input.")



        

        
        
    elif option == "7":
            break

        

    else:
        print("Invalid option.")
        print()


   












