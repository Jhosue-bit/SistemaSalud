
class Persona:
    """
    Representa los datos generales de una persona.
    Clase base para otras entidades del sistema.
    """

    def __init__(self, id_persona, nombres, apellidos):
        self.__id = id_persona
        self.__nombres = nombres
        self.__apellidos = apellidos

    # Métodos de acceso (getters)
    def obtener_id(self):
        return self.__id

    def obtener_nombres(self):
        return self.__nombres

    def obtener_apellidos(self):
        return self.__apellidos

    # Método para obtener los datos generales
    def obtener_datos(self):
        return {
            "id": self.__id,
            "nombres": self.__nombres,
            "apellidos": self.__apellidos
        }
