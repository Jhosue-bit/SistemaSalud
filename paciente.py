
from persona import Persona


class Paciente(Persona):
    """
    Representa a un paciente del Centro Materno Infantil.
    Hereda los datos generales de la clase Persona.
    """

    def __init__(self, id_persona, nombres, apellidos, dni, telefono):
        super().__init__(id_persona, nombres, apellidos)

        if not isinstance(dni, str) or not dni.strip():
            raise ValueError("El DNI no puede estar vacío.")

        if not isinstance(telefono, str) or not telefono.strip():
            raise ValueError("El teléfono no puede estar vacío.")

        self.__dni = dni.strip()
        self.__telefono = telefono.strip()

    # Métodos de acceso
    def obtener_dni(self):
        return self.__dni

    def obtener_telefono(self):
        return self.__telefono

    # Método para actualizar el teléfono
    def actualizar_telefono(self, nuevo_telefono):
        if not isinstance(nuevo_telefono, str) or not nuevo_telefono.strip():
            raise ValueError("El teléfono debe ser un texto válido.")

        self.__telefono = nuevo_telefono.strip()

    # Método para obtener todos los datos del paciente
    def obtener_datos(self):
        datos = super().obtener_datos()
        datos["dni"] = self.__dni
        datos["telefono"] = self.__telefono

        return datos
