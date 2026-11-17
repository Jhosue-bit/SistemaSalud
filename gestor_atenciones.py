
class GestorAtenciones:
    """
    Administra el registro y consulta de atenciones médicas.
    """

    def __init__(self):
        self.__atenciones = []

    # Registrar una atención médica
    def registrar_atencion(self, atencion):
        if atencion is None:
            raise ValueError("Debe proporcionar una atención médica válida.")

        for existente in self.__atenciones:
            if existente.obtener_id() == atencion.obtener_id():
                raise ValueError("Ya existe una atención con ese ID.")

        self.__atenciones.append(atencion)
        return True

    # Buscar una atención por su ID
    def buscar_atencion(self, id_atencion):
        for atencion in self.__atenciones:
            if atencion.obtener_id() == id_atencion:
                return atencion

        return None

    # Listar todas las atenciones
    def listar_atenciones(self):
        return [
            atencion.obtener_datos()
            for atencion in self.__atenciones
        ]

    # Obtener los objetos AtencionMedica originales
    def obtener_atenciones(self):
        return self.__atenciones.copy()

    # Contar las atenciones registradas
    def contar_atenciones(self):
        return len(self.__atenciones)
