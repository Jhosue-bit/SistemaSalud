
class GestorPacientes:
    """
    Administra el registro y consulta de pacientes.
    """

    def __init__(self):
        self.__pacientes = []

    # Registrar un paciente
    def registrar_paciente(self, paciente):
        if paciente is None:
            raise ValueError("Debe proporcionar un paciente válido.")

        for existente in self.__pacientes:
            if existente.obtener_id() == paciente.obtener_id():
                raise ValueError("Ya existe un paciente con ese ID.")

            if existente.obtener_dni() == paciente.obtener_dni():
                raise ValueError("Ya existe un paciente con ese DNI.")

        self.__pacientes.append(paciente)
        return True

    # Buscar un paciente por su ID
    def buscar_paciente(self, id_paciente):
        for paciente in self.__pacientes:
            if paciente.obtener_id() == id_paciente:
                return paciente

        return None

    # Listar todos los pacientes
    def listar_pacientes(self):
        return [
            paciente.obtener_datos()
            for paciente in self.__pacientes
        ]

    # Obtener los objetos Paciente originales
    def obtener_pacientes(self):
        return self.__pacientes.copy()

    # Obtener la cantidad de pacientes registrados
    def contar_pacientes(self):
        return len(self.__pacientes)
