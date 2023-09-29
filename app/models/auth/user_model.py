from ...database import DatabaseConnection



class User:

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.email = kwargs.get("email")
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.role_id = kwargs.get("role_id")

    def serialize(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }

    @classmethod
    def is_registered(cls, user):
        query = """SELECT user_id FROM app_discord.usuarios 
        WHERE usuario = %(username)s and contrasena = %(password)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False

    @classmethod
    def get(cls, user):
        query = """SELECT * FROM app_discord.usuarios
        WHERE usuario = %(username)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                user_id=result[0],
                username=result[1],
                password=result[2],
                email=result[3],
                first_name=result[4],
                last_name=result[5],
            )
        return None
    
    @classmethod
    def regist(cls,username,password,email,first_name,last_name,fecha_nacimiento):
        query = """INSERT INTO app_discord.usuarios (usuario, nombre, apellido, email, contrasena, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s);"""
        params = username,first_name,last_name,email,password,fecha_nacimiento,
        DatabaseConnection.execute_query(query, params=params)
        
        
    @classmethod
    def is_regist(cls, user):
        query = """SELECT user_id FROM app_discord.usuarios 
        WHERE usuario = %(username)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
        
        
    @classmethod
    def get2(cls, user):
        """Get a film by id
        Args:
            - film (Film): Film object with the id attribute
        Returns:
            - Film: Film object
        """

        query = """SELECT film_id, title, description, release_year,
        language_id, original_language_id, rental_duration, rental_rate,
        length, replacement_cost, rating, special_features, last_update 
        FROM sakila.film WHERE film_id = %s"""
        params = user.usuario,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
<<<<<<< Updated upstream
        return None
=======
        return None
    
    @classmethod
    def readperfil(cls, usuario):
        uss=[]
        uss.append(usuario)
        query = """SELECT usuario, nombre, apellido, email, contrasena, fecha_nacimiento FROM app_discord.usuarios WHERE usuario = %s"""
        params = uss
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return result
        return None
>>>>>>> Stashed changes
