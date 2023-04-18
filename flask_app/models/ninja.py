from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.controllers.dojos import Dojo


########-----Trying to understand the relationship between methods 
# and controllers and what relates to the corresponding route and method
# I know I need a save and a create but do i also need the read????'
# I only need 5 routes for this assignment between both controllers
# but how many methods do I need between them both???????????




DATABASE = "dojos_and_ninjas_schema"

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



#! CREATE
#! CONVENTION TO NAME CREATE as SAVE

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());'
        return connectToMySQL(DATABASE).query_db(query,data)
    



#! READ ALL

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        result = connectToMySQL(DATABASE).query_db(query)
        print(result)
        ninjas = []
        for ninja_dict in result:
            ninjas.append(cls(ninja_dict))
        return ninjas
    

#! READ ONE

    @classmethod
    def get_ninja(cls, id):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        data = {'id': id}
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result[0])
        ninja = Ninja(result[0])
        return ninja

    

#! READ ONE
    # @classmethod
    # def get_ninja(cls, id):
    #     query = "SELECT * FROM ninjas JOIN dojos ON ninjas.id = dojos.ninja_id WHERE ninjas.id = %(id)s;"
    #     result = connectToMySQL(DATABASE).query_db(query, id)
    #     print(result)
    #     ninja = Ninja(result[0])
    #     print(ninja.dojos)
    #     for item in result:
    #         print(item)
          
    #         ninja.dojos.append(Dojo(temp_ninja))
    #     return ninja