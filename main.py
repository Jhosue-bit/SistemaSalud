
from sistema_salud import SistemaSalud
from paciente import Paciente
from cita import Cita
from atencion_medica import AtencionMedica


def mostrar_menu():
    print("\n===================================")
    print("       SISTEMA DE SALUD")
    print("===================================")
    print("1. Registrar paciente")
    print("2. Mostrar pacientes")
    print("3. Registrar cita")
    print("4. Mostrar citas")
    print("5. Registrar atención médica")
    print("6. Mostrar atenciones médicas")
    print("7. Mostrar resumen general")
    print("8. Guardar datos")
    print("9. Salir")
    print("===================================")


def ejecutar_sistema():
    sistema = SistemaSalud()

    gestor_pacientes = sistema.obtener_gestor_pacientes()
    gestor_citas = sistema.obtener_gestor_citas()
    gestor_atenciones = sistema.obtener_gestor_atenciones()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                print("\nREGISTRAR PACIENTE")

                id_paciente = input("ID: ").strip()
                nombres = input("Nombres: ").strip()
                apellidos = input("Apellidos: ").strip()
                dni = input("DNI: ").strip()
                telefono = input("Teléfono: ").strip()

                if not all([id_paciente, nombres, apellidos, dni, telefono]):
                    raise ValueError("Todos los campos son obligatorios.")

                paciente = Paciente(
                    id_paciente, nombres, apellidos, dni, telefono
                )

                gestor_pacientes.registrar_paciente(paciente)
                print("Paciente registrado correctamente.")

            elif opcion == "2":
                print("\nLISTA DE PACIENTES")
                print(gestor_pacientes.listar_pacientes())

            elif opcion == "3":
                print("\nREGISTRAR CITA")

                id_cita = input("ID de la cita: ").strip()
                id_paciente = input("ID del paciente: ").strip()
                fecha = input("Fecha: ").strip()
                hora = input("Hora: ").strip()
                motivo = input("Motivo: ").strip()

                paciente = gestor_pacientes.buscar_paciente(id_paciente)

                if paciente is None:
                    raise ValueError("No se encontró el paciente.")

                if not all([id_cita, fecha, hora, motivo]):
                    raise ValueError("Todos los campos son obligatorios.")

                cita = Cita(
                    id_cita, paciente, fecha, hora, motivo
                )

                gestor_citas.registrar_cita(cita)
                print("Cita registrada correctamente.")

            elif opcion == "4":
                print("\nLISTA DE CITAS")
                print(gestor_citas.listar_citas())

            elif opcion == "5":
                print("\nREGISTRAR ATENCIÓN MÉDICA")

                id_atencion = input("ID de la atención: ").strip()
                id_cita = input("ID de la cita: ").strip()
                diagnostico = input("Diagnóstico: ").strip()
                tratamiento = input("Tratamiento: ").strip()
                observaciones = input("Observaciones: ").strip()

                cita = gestor_citas.buscar_cita(id_cita)

                if cita is None:
                    raise ValueError("No se encontró la cita.")

                if not all([
                    id_atencion, diagnostico,
                    tratamiento
                ]):
                    raise ValueError("Los campos ID, diagnóstico y tratamiento son obligatorios.")

                atencion = AtencionMedica(
                    id_atencion, cita, diagnostico,
                    tratamiento, observaciones
                )

                gestor_atenciones.registrar_atencion(atencion)
                cita.cambiar_estado("Atendida")

                print("Atención médica registrada correctamente.")

            elif opcion == "6":
                print("\nLISTA DE ATENCIONES MÉDICAS")
                print(gestor_atenciones.listar_atenciones())

            elif opcion == "7":
                print("\nRESUMEN GENERAL")
                print(sistema.mostrar_resumen())

            elif opcion == "8":
                sistema.guardar_datos()
                print("Datos guardados correctamente.")

            elif opcion == "9":
                sistema.guardar_datos()
                print("Datos guardados. Hasta luego.")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        except ValueError as error:
            print(f"Error: {error}")

        except Exception as error:
            print(f"Ocurrió un error inesperado: {error}")


if __name__ == "__main__":
    ejecutar_sistema()
