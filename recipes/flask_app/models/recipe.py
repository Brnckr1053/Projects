from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
# from flask_app.config.connectToMySQL import connectToMySQL
from flask_app.models.user import User



class Recipe():

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.yes_no = data['yes_no']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def create_recipe(cls,data):
        query  = 'INSERT INTO recipes (name,description,instructions,date,yes_no,user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(date)s,%(yes_no)s,%(user_id)s)'
        results = connectToMySQL("recipes_data").query_db(query,data)

        return results

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL("recipes_data").query_db(query)

        recipes = []

        for item in results:
            if item['yes_no'] == 1:
                item['yes_no'] = "Yes"
            if item['yes_no'] == 0:
                item['yes_no'] = "No"
            recipe = Recipe(item)
            user_data = {

                'id' : item['users.id'],
                'first_name' : item['first_name'],
                'last_name' : item['last_name'],
                'email' : item['email'],
                'password' : item['password'],
                'created_at' : item['users.created_at'],
                'updated_at' : item['users.updated_at']
            }

            user = User(user_data)
            recipe.user = user
            recipes.append(recipe)

        return recipes

    @classmethod
    def get_recipe_by_id(cls,data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE  recipes.id = %(id)s"
        result = connectToMySQL("recipes_data").query_db(query,data)[0]



        recipe = Recipe(result)
        print (recipe.yes_no)
        if recipe.yes_no == 1:
            recipe.yes_no = "yes"
        
        if recipe.yes_no == 0:
            recipe.yes_no = "no"


            
        user_data = {

                'id' : result['users.id'],
                'first_name' : result['first_name'],
                'last_name' : result['last_name'],
                'email' : result['email'],
                'password' : result['password'],
                'created_at' : result['users.created_at'],
                'updated_at' : result['users.updated_at']
            }


        recipe.user = User(user_data)


        return recipe

    @classmethod
    def update_recipe(cls,data):
        query = 'UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s, yes_no = %(yes_no)s WHERE id = %(id)s;'
        connectToMySQL("recipes_data").query_db(query,data)


    @classmethod
    def delete_recipe(cls,data):
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        connectToMySQL("recipes_data").query_db(query,data)


    @staticmethod
    def recipe_validator(data):
        is_valid = True

        if len(data['name']) < 1 or len(data['name']) > 100:
            flash("Recipe name should be 1 to 100 characters")
            is_valid = False
        
        if len(data['description']) < 1 or len(data['description']) > 500:
            flash("Recipe description should be 1 to 500 characters")
            is_valid = False

        if len(data['instructions']) < 1 or len(data['instructions']) > 500:
            flash("Recipe instruction should be 1 to 500 characters")
            is_valid = False

        if len(data['date']) != 10:
            flash("please provide a valid date")
            is_valid = False

        return is_valid

    @classmethod
    def get_user_recipes(cls,data):
        query = "SELECT * FROM users JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s"
        user_recipes_db = connectToMySQL("recipes_data").query_db(query,data)
        print(user_recipes_db)
        user = User(user_recipes_db[0])
        
        for i in user_recipes_db:
            if i['yes_no'] == 1:
                i['yes_no'] = "Yes"
            if i['yes_no'] == 0:
                i['yes_no'] = "No"
            recipe = Recipe(i)
            recipe_data = {

                'id' : i['recipes.id'],
                'name' : i['name'],
                'description' : i['description'],
                'instructions' : i['instructions'],
                'date' : i['date'],
                'yes_no' : i['yes_no'],
                'created_at' : i['created_at'],
                'updated_at' : i['updated_at'],
                'user_id' : i['user_id']
            }

            recipe.user = user
            user.recipes.append(Recipe(recipe_data))
            
        return user