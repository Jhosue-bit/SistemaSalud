
import pytest

from persona import Persona
from paciente import Paciente
from gestor_pacientes import GestorPacientes


def test_crear_persona():
    persona = Persona("P001", "Ana", "Torres")

    assert persona.obtener_id() == "P001"
    assert persona.obtener_nombres() == "Ana"
    assert persona.obtener_apellidos() == "Torres"


def test_persona_sin_nombre():
    with pytest.raises(ValueError):
        Persona("P001", "", "Torres")


def test_crear_paciente():
    paciente = Paciente(
        "P001", "Ana", "Torres",
        "12345678", "987654321"
    )

    assert paciente.obtener_dni() == "12345678"
    assert paciente.obtener_telefono() == "987654321"


def test_paciente_sin_dni():
    with pytest.raises(ValueError):
        Paciente("P001", "Ana", "Torres", "", "987654321")


def test_registrar_paciente():
    gestor = GestorPacientes()
    paciente = Paciente(
        "P001", "Ana", "Torres",
        "12345678", "987654321"
    )

    gestor.registrar_paciente(paciente)

    assert gestor.contar_pacientes() == 1
    assert gestor.buscar_paciente("P001") is paciente


def test_paciente_duplicado():
    gestor = GestorPacientes()

    paciente = Paciente(
        "P001", "Ana", "Torres",
        "12345678", "987654321"
    )

    gestor.registrar_paciente(paciente)

    with pytest.raises(ValueError):
        gestor.registrar_paciente(paciente)


from cita import Cita
from atencion_medica import AtencionMedica
from gestor_citas import GestorCitas
from gestor_atenciones import GestorAtenciones
from reporte import Reporte


def crear_paciente_prueba():
    return Paciente(
        "P100", "Maria", "Lopez",
        "87654321", "987654321"
    )


def crear_cita_prueba():
    paciente = crear_paciente_prueba()
    return Cita(
        "C100", paciente,
        "2026-11-20", "10:00",
        "Consulta general"
    )


def test_registrar_cita():
    gestor = GestorCitas()
    cita = crear_cita_prueba()

    gestor.registrar_cita(cita)

    assert gestor.contar_citas() == 1
    assert gestor.buscar_cita("C100") is cita


def test_cita_duplicada():
    gestor = GestorCitas()
    cita = crear_cita_prueba()

    gestor.registrar_cita(cita)

    with pytest.raises(ValueError):
        gestor.registrar_cita(cita)


def test_cambiar_estado_cita():
    cita = crear_cita_prueba()

    cita.cambiar_estado("Atendida")

    assert cita.obtener_estado() == "Atendida"


def test_estado_cita_invalido():
    cita = crear_cita_prueba()

    with pytest.raises(ValueError):
        cita.cambiar_estado("Desconocido")


def test_registrar_atencion():
    gestor = GestorAtenciones()
    cita = crear_cita_prueba()

    atencion = AtencionMedica(
        "A100", cita,
        "Diagnostico de prueba",
        "Tratamiento de prueba",
        "Sin observaciones"
    )

    gestor.registrar_atencion(atencion)

    assert gestor.contar_atenciones() == 1
    assert gestor.buscar_atencion("A100") is atencion


def test_generar_reporte():
    gestor_pacientes = GestorPacientes()
    gestor_citas = GestorCitas()
    gestor_atenciones = GestorAtenciones()

    paciente = crear_paciente_prueba()
    gestor_pacientes.registrar_paciente(paciente)

    cita = Cita(
        "C100", paciente,
        "2026-11-20", "10:00",
        "Consulta general"
    )
    gestor_citas.registrar_cita(cita)

    reporte = Reporte(
        gestor_pacientes,
        gestor_citas,
        gestor_atenciones
    )

    resumen = reporte.generar_resumen()

    assert resumen["total_pacientes"] == 1
    assert resumen["total_citas"] == 1
    assert resumen["total_atenciones"] == 0
    assert len(reporte.obtener_citas_pendientes()) == 1
