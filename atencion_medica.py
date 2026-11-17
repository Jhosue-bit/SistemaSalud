
class AtencionMedica:
    """
    Representa la atención médica brindada a un paciente.
    """

    def __init__(self, id_atencion, cita, diagnostico, tratamiento, observaciones):
        self.__id_atencion = id_atencion
        self.__cita = cita
        self.__diagnostico = diagnostico
        self.__tratamiento = tratamiento
        self.__observaciones = observaciones

    # Métodos de acceso
    def obtener_id(self):
        return self.__id_atencion

    def obtener_cita(self):
        return self.__cita

    def obtener_diagnostico(self):
        return self.__diagnostico

    def obtener_tratamiento(self):
        return self.__tratamiento

    def obtener_observaciones(self):
        return self.__observaciones

    # Método para actualizar las observaciones
    def actualizar_observaciones(self, nuevas_observaciones):
        if not nuevas_observaciones.strip():
            raise ValueError("Las observaciones no pueden estar vacías.")

        self.__observaciones = nuevas_observaciones

    # Método para obtener los datos de la atención
    def obtener_datos(self):
        return {
            "id_atencion": self.__id_atencion,
            "cita": self.__cita.obtener_datos(),
            "diagnostico": self.__diagnostico,
            "tratamiento": self.__tratamiento,
            "observaciones": self.__observaciones
        }
