from flask_app import app
from flask import redirect, render_template, session, request, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/recipes')
def recipes_index():
    if 'user_id' not in session:
        flash("Please log in to view this page.")
        return redirect('/')
    recipes = Recipe.get_all_recipes()
    return render_template("dashboard.html", recipes = recipes)

@app.route("/recipes/new")
def new_recipes():
    if 'user_id' not in session:
        flash("Please log in to view this page.")
        return redirect('/')
    return render_template('add_recipes.html')


@app.route("/recipes/create", methods=["POST"])
def create_recipe():
    print(request.form)
    if (Recipe.recipe_validator(request.form)):
        data = {
            'name' : request.form['name'],
            'description' : request.form['description'],
            'instructions' : request.form['instructions'],
            'date' : request.form['date'],
            'yes_no' : request.form['yes_no'],
            'user_id' : session['user_id']
        }
        
        Recipe.create_recipe(data)
        return redirect('/recipes')

    # if 'user_id' not in session:
    #     flash("Please log in to view this page.")
    #     return redirect('/')
    return redirect("/recipes/new")
    
@app.route('/recipes/<int:recipe_id>')
def recipe_information(recipe_id):
    recipe = Recipe.get_recipe_by_id({'id':recipe_id})

    return render_template("recipe_data.html", recipe = recipe)

@app.route('/recipes/<int:recipe_id>/edit')
def edit_recipe(recipe_id):
    
    recipe = Recipe.get_recipe_by_id({'id':recipe_id})

    if recipe.user.id != session['user_id']:
        return redirect('/recipes')

    return render_template("edit_recipe.html", recipe = recipe)

@app.route('/recipes/<int:recipe_id>/update', methods=['POST'])
def update_recipe(recipe_id):
    
    recipe = Recipe.get_recipe_by_id({'id':recipe_id})

    if recipe.user.id != session['user_id']:
        return redirect('/recipes')

    data = {
        'id' : recipe_id,
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date' : request.form['date'],
        'yes_no' : request.form['yes_no']
    }

    Recipe.update_recipe(data)

    return redirect(f'/recipes/{recipe.id}')


@app.route('/recipes/<int:recipe_id>/delete')
def delete_recipe(recipe_id):
    
    recipe = Recipe.get_recipe_by_id({'id':recipe_id})

    if recipe.user.id != session['user_id']:
        return redirect('/recipes')

    return render_template('confirm_delete.html', recipe = recipe)


@app.route('/recipes/<int:recipe_id>/confirm_delete')
def confirm_delete(recipe_id):
    recipe = Recipe.get_recipe_by_id({'id':recipe_id})

    if recipe.user.id != session['user_id']:
        return redirect('/recipes')

    Recipe.delete_recipe({'id':recipe_id})

    return redirect('/recipes')



@app.route("/user/<int:id>")
def user(id):
    if "user_id" not in session:
        flash("Must be logged in to view page")
        return redirect("/")

    data = {            
        "id":id
    }
    one_user_recipes = Recipe.get_user_recipes(data)
    return render_template("userpage.html", one_user_recipes=one_user_recipes)
