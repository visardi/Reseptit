import db

def add_recipe(name, cooking_time, ingredients, instructions, user_id):
    sql = """INSERT INTO recipes (name, cooking_time, ingredients, instructions, user_id) VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [name, cooking_time, ingredients, instructions, user_id])

def get_recipes():
    sql = "SELECT id, name FROM recipes ORDER BY id DESC"
    return db.query(sql)

def get_recipe(recipe_id):
    sql = """SELECT recipes.name,
                    recipes.cooking_time,
                    recipes.ingredients,
                    recipes.instructions,
                    users.username
            FROM recipes, users
            WHERE recipes.id = ?"""
    return db.query(sql,[recipe_id])[0]

