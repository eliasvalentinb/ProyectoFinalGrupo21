class Usuario:
    def __init__(self, username, dni, password, email):
        self.__id = id
        self.__username = username
        self.__dni = dni
        self.__password = password
        self.__email = email
    
    def get_id(self):
        return self.__id    
    def set_id(self, id):
        self.__id = id
    
    def get_username(self):
        return self.__username 
    def set_username(self, username):
        self.__username = username

    def get_dni(self):
        return self.__dni
    def set_dni(self, dni):
        self.__dni = dni
    
    def get_password(self):
        return self.__password
    def set_password(self, password):
        self.__password = password

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

def mostrar_info(self):
    print(f"ID: {self.__id} \nUsername: {self.__username} \nDNI: {self.__dni} \nEmail: {self.__email}")

