import db

def add_recipe(name, cooking_time, ingredients, instructions, user_id):
    sql = """INSERT INTO recipes (name, cooking_time, ingredients, instructions, user_id) VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [name, cooking_time, ingredients, instructions, user_id])

def get_recipes():
    sql = "SELECT id, name FROM recipes ORDER BY id DESC"
    return db.query(sql)

def get_recipe(recipe_id):
    sql = """SELECT recipes.id,
                    recipes.name,
                    recipes.cooking_time,
                    recipes.ingredients,
                    recipes.instructions,
                    users.id user_id,
                    users.username
            FROM recipes, users
            WHERE recipes.user_id = users.id AND recipes.id = ?"""
    return db.query(sql,[recipe_id])[0]

def update_recipe(recipe_id, name, cooking_time, ingredients, instructions):
    sql = """UPDATE recipes SET name = ?,
                                cooking_time = ?,
                                ingredients = ?,
                                instructions = ?
                            WHERE id = ?"""
    db.execute(sql, [name, cooking_time, ingredients, instructions, recipe_id])

def remove_recipe(recipe_id):
    sql = "DELETE FROM recipes WHERE id = ?"
    db.execute(sql, [recipe_id])


def find_recipes(query):
    sql = """SELECT id, name
             FROM recipes
             WHERE INGREDIENTS LIKE ?
             ORDER BY id DESC"""
    return db.query(sql, ["%" + query + "%"])