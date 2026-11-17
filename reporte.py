
class Reporte:
    """
    Genera reportes sobre pacientes, citas y atenciones médicas.
    """

    def __init__(self, gestor_pacientes, gestor_citas, gestor_atenciones):
        self.__gestor_pacientes = gestor_pacientes
        self.__gestor_citas = gestor_citas
        self.__gestor_atenciones = gestor_atenciones

    # Generar un resumen general
    def generar_resumen(self):
        return {
            "total_pacientes": self.__gestor_pacientes.contar_pacientes(),
            "total_citas": self.__gestor_citas.contar_citas(),
            "total_atenciones": self.__gestor_atenciones.contar_atenciones()
        }

    # Obtener la lista de citas pendientes
    def obtener_citas_pendientes(self):
        citas = self.__gestor_citas.listar_citas()

        return list(filter(
            lambda cita: cita["estado"] == "Pendiente",
            citas
        ))

    # Generar un reporte de pacientes
    def generar_reporte_pacientes(self):
        return self.__gestor_pacientes.listar_pacientes()
