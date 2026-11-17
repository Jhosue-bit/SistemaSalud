
class Persona:
    """
    Representa los datos generales de una persona.
    Clase base para otras entidades del sistema.
    """

    def __init__(self, id_persona, nombres, apellidos):
        if not isinstance(id_persona, str) or not id_persona.strip():
            raise ValueError("El ID de la persona no puede estar vacío.")

        if not isinstance(nombres, str) or not nombres.strip():
            raise ValueError("Los nombres no pueden estar vacíos.")

        if not isinstance(apellidos, str) or not apellidos.strip():
            raise ValueError("Los apellidos no pueden estar vacíos.")

        self.__id = id_persona.strip()
        self.__nombres = nombres.strip()
        self.__apellidos = apellidos.strip()

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
