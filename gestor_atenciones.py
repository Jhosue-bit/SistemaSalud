
class GestorAtenciones:
    """
    Administra el registro y consulta de atenciones médicas.
    """

    def __init__(self):
        self.__atenciones = []

    # Registrar una atención médica
    def registrar_atencion(self, atencion):
        for existente in self.__atenciones:
            if existente.obtener_id() == atencion.obtener_id():
                raise ValueError("Ya existe una atención con ese ID.")

        self.__atenciones.append(atencion)
        return True

    # Buscar una atención por su ID
    def buscar_atencion(self, id_atencion):
        resultado = filter(
            lambda atencion: atencion.obtener_id() == id_atencion,
            self.__atenciones
        )

        return next(resultado, None)

    # Listar todas las atenciones
    def listar_atenciones(self):
        return list(map(
            lambda atencion: atencion.obtener_datos(),
            self.__atenciones
        ))

    # Obtener los objetos AtencionMedica originales
    def obtener_atenciones(self):
        return self.__atenciones.copy()
    
    # Contar las atenciones registradas
    def contar_atenciones(self):
        return len(self.__atenciones)
