
class Cita:
    """
    Representa una cita médica programada para un paciente.
    """

    def __init__(self, id_cita, paciente, fecha, hora, motivo):
        self.__id_cita = id_cita
        self.__paciente = paciente
        self.__fecha = fecha
        self.__hora = hora
        self.__motivo = motivo
        self.__estado = "Pendiente"

    # Métodos de acceso
    def obtener_id(self):
        return self.__id_cita

    def obtener_paciente(self):
        return self.__paciente

    def obtener_fecha(self):
        return self.__fecha

    def obtener_hora(self):
        return self.__hora

    def obtener_motivo(self):
        return self.__motivo

    def obtener_estado(self):
        return self.__estado

    # Método para cambiar el estado de la cita
    def cambiar_estado(self, nuevo_estado):
        estados_validos = ["Pendiente", "Confirmada", "Atendida", "Cancelada"]

        if nuevo_estado not in estados_validos:
            raise ValueError("El estado de la cita no es válido.")

        self.__estado = nuevo_estado

    # Método para obtener los datos de la cita
    def obtener_datos(self):
        return {
            "id_cita": self.__id_cita,
            "paciente": self.__paciente.obtener_datos(),
            "fecha": self.__fecha,
            "hora": self.__hora,
            "motivo": self.__motivo,
            "estado": self.__estado
        }
