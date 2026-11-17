
from gestor_pacientes import GestorPacientes
from gestor_citas import GestorCitas
from gestor_atenciones import GestorAtenciones
from reporte import Reporte
from conexion_datos import ConexionDatos

from paciente import Paciente
from cita import Cita
from atencion_medica import AtencionMedica


class SistemaSalud:
    """
    Coordina los componentes principales del sistema de salud.
    """

    def __init__(self):
        self.__conexion = ConexionDatos.obtener_instancia()

        self.__gestor_pacientes = GestorPacientes()
        self.__gestor_citas = GestorCitas()
        self.__gestor_atenciones = GestorAtenciones()

        self.__reporte = Reporte(
            self.__gestor_pacientes,
            self.__gestor_citas,
            self.__gestor_atenciones
        )

        self.cargar_datos()

    # Obtener los gestores
    def obtener_gestor_pacientes(self):
        return self.__gestor_pacientes

    def obtener_gestor_citas(self):
        return self.__gestor_citas

    def obtener_gestor_atenciones(self):
        return self.__gestor_atenciones

    def obtener_reporte(self):
        return self.__reporte

    # Guardar información en archivos JSON
    def guardar_datos(self):
        self.__conexion.guardar_datos(
            "pacientes.json",
            self.__gestor_pacientes.listar_pacientes()
        )

        self.__conexion.guardar_datos(
            "citas.json",
            self.__gestor_citas.listar_citas()
        )

        self.__conexion.guardar_datos(
            "atenciones.json",
            self.__gestor_atenciones.listar_atenciones()
        )

    # Recuperar información de los archivos JSON
    def cargar_datos(self):
        pacientes = self.__conexion.cargar_datos("pacientes.json")
        citas = self.__conexion.cargar_datos("citas.json")
        atenciones = self.__conexion.cargar_datos("atenciones.json")

        # Recuperar pacientes
        for datos in pacientes:
            paciente = Paciente(
                datos["id"],
                datos["nombres"],
                datos["apellidos"],
                datos["dni"],
                datos["telefono"]
            )

            self.__gestor_pacientes.registrar_paciente(paciente)

        # Recuperar citas
        for datos in citas:
            id_paciente = datos["paciente"]["id"]
            paciente = self.__gestor_pacientes.buscar_paciente(id_paciente)

            if paciente is None:
                raise ValueError("No se encontró el paciente de una cita.")

            cita = Cita(
                datos["id_cita"],
                paciente,
                datos["fecha"],
                datos["hora"],
                datos["motivo"]
            )

            cita.cambiar_estado(datos["estado"])
            self.__gestor_citas.registrar_cita(cita)

        # Recuperar atenciones médicas
        for datos in atenciones:
            id_cita = datos["cita"]["id_cita"]
            cita = self.__gestor_citas.buscar_cita(id_cita)

            if cita is None:
                raise ValueError("No se encontró la cita de una atención.")

            atencion = AtencionMedica(
                datos["id_atencion"],
                cita,
                datos["diagnostico"],
                datos["tratamiento"],
                datos["observaciones"]
            )

            self.__gestor_atenciones.registrar_atencion(atencion)

    # Mostrar resumen general
    def mostrar_resumen(self):
        return self.__reporte.generar_resumen()
