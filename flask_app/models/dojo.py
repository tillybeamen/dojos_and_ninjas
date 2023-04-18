from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

DATABASE = "dojos_and_ninjas_schema"

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name,  created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'
        return connectToMySQL(DATABASE).query_db(query,data)
    




# READ ALL
    @classmethod
    def get_all(cls):
        
        query = 'SELECT * FROM dojos;'
        
        result = connectToMySQL(DATABASE).query_db(query)
        print(result)
        
        dojos = []
        
        for dojo in result:
            dojos.append(cls(dojo))
        return dojos
        #handle means to save for the routes



#! READ ONE
    @classmethod
    def get_dojo(cls, id):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, id)
        print(result)
        dojo = cls(result[0])
        # print(dojo.ninjas)
        for item in result:
            print(item)
            temp_ninja = {
                'id': item['ninjas.id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'age':item['age'],
                'dojo_id': item['dojo_id'],
                'created_at': item['ninjas.created_at'],
                'updated_at': item['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(temp_ninja))
        return dojo





