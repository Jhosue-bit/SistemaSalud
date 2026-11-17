
import json
import os


class ConexionDatos:
    """
    Administra el acceso a los archivos JSON del sistema.
    Implementa el patrón Singleton.
    """

    __instancia = None

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)

        return cls.__instancia

    def __init__(self):
        if hasattr(self, "_inicializado"):
            return

        self.__carpeta_datos = "Datos"
        os.makedirs(self.__carpeta_datos, exist_ok=True)

        self._inicializado = True

    # Guardar información en un archivo JSON
    def guardar_datos(self, nombre_archivo, datos):
        ruta = os.path.join(
            self.__carpeta_datos,
            nombre_archivo
        )

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    # Leer información de un archivo JSON
    def cargar_datos(self, nombre_archivo):
        ruta = os.path.join(
            self.__carpeta_datos,
            nombre_archivo
        )

        if not os.path.exists(ruta):
            return []

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)

        except json.JSONDecodeError:
            raise ValueError(
                f"El archivo {nombre_archivo} contiene información inválida."
            )

    # Obtener la instancia Singleton
    @classmethod
    def obtener_instancia(cls):
        return cls()
