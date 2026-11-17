
class GestorPacientes:
    """
    Administra el registro y consulta de pacientes.
    """

    def __init__(self):
        self.__pacientes = []

    # Registrar un paciente
    def registrar_paciente(self, paciente):
        for existente in self.__pacientes:
            if existente.obtener_id() == paciente.obtener_id():
                raise ValueError("Ya existe un paciente con ese ID.")

            if existente.obtener_dni() == paciente.obtener_dni():
                raise ValueError("Ya existe un paciente con ese DNI.")

        self.__pacientes.append(paciente)
        return True

    # Buscar un paciente por su ID
    def buscar_paciente(self, id_paciente):
        resultado = filter(
            lambda paciente: paciente.obtener_id() == id_paciente,
            self.__pacientes
        )

        return next(resultado, None)

    # Listar todos los pacientes
    def listar_pacientes(self):
        return list(map(
            lambda paciente: paciente.obtener_datos(),
            self.__pacientes
        ))

    # Obtener los objetos Paciente originales
    def obtener_pacientes(self):
        return self.__pacientes.copy()

    # Obtener la cantidad de pacientes registrados
    def contar_pacientes(self):
        from functools import reduce

        return reduce(
            lambda total, paciente: total + 1,
            self.__pacientes,
            0
        )
