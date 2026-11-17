
class GestorCitas:
    """
    Administra el registro y consulta de citas médicas.
    """

    def __init__(self):
        self.__citas = []

    # Registrar una cita
    def registrar_cita(self, cita):
        for existente in self.__citas:
            if existente.obtener_id() == cita.obtener_id():
                raise ValueError("Ya existe una cita con ese ID.")

        self.__citas.append(cita)
        return True

    # Buscar una cita por su ID
    def buscar_cita(self, id_cita):
        resultado = filter(
            lambda cita: cita.obtener_id() == id_cita,
            self.__citas
        )

        return next(resultado, None)

    # Listar todas las citas
    def listar_citas(self):
        return list(map(
            lambda cita: cita.obtener_datos(),
            self.__citas
        ))

    # Obtener los objetos Cita originales
    def obtener_citas(self):
        return self.__citas.copy()
    
    # Contar las citas registradas
    def contar_citas(self):
        return len(self.__citas)
