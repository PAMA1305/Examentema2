import tkinter as tk
from tkinter import ttk
import requests

# URL de la API
url = "https://671be6612c842d92c381b162.mockapi.io/test"


class ApiManager:
    @staticmethod
    def obtener_registro_por_id(registro_id):
        try:
            response = requests.get(url)
            response.raise_for_status()
            registros = response.json()
            for registro in registros:
                if int(registro.get('id')) == registro_id:
                    return registro
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
        return None

    @staticmethod
    def obtener_ultimo_registro():
        try:
            response = requests.get(url)
            response.raise_for_status()
            registros = response.json()
            if registros:
                return registros[-1]
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
        return None

    @staticmethod
    def obtener_primer_registro():
        try:
            response = requests.get(url)
            response.raise_for_status()
            registros = response.json()
            if registros:
                return registros[0]
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
        return None

    @staticmethod
    def obtener_todos_los_registros():
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
        return []


class RegistroManager:
    def __init__(self, api_manager):
        self.api_manager = api_manager

    def mostrar_ultimo_registro(self):
        registro = self.api_manager.obtener_ultimo_registro()
        self._mostrar_registro_en_ventana(registro, "Último Registro", "lightgreen")

    def mostrar_primer_registro(self):
        registro = self.api_manager.obtener_primer_registro()
        self._mostrar_registro_en_ventana(registro, "Primer Registro", "lightblue")

    def mostrar_todos_registros(self):
        ventana_todos = tk.Toplevel()
        ventana_todos.title("Todos los Registros")
        ventana_todos.geometry("1800x500")
        ventana_todos.configure(bg='lightcoral')

        tree = ttk.Treeview(ventana_todos, columns=("ID", "Nombre", "Horse", "Condado", "Insecto", "Hack", "Color"),
                            show='headings')
        for col in tree["columns"]:
            tree.heading(col, text=col)

        tree.tag_configure('yellow', background='lightyellow')
        tree.pack(expand=True, fill='both')

        registros = self.api_manager.obtener_todos_los_registros()
        for registro in registros:
            tree.insert("", "end", values=(registro.get('id', 'N/A'),
                                           registro.get('nombre', 'N/A'),
                                           registro.get('horse', 'N/A'),
                                           registro.get('condado', 'N/A'),
                                           registro.get('hack', 'N/A'),
                                           registro.get('insecto', 'N/A'),
                                           registro.get('color', 'N/A')),
                        tags=('yellow',))

        boton_regresar = tk.Button(ventana_todos, text="Regresar", command=ventana_todos.destroy, bg='cyan', fg='black')
        boton_regresar.pack(pady=10)

    def mostrar_registro_por_id(self, registro_id):
        registro = self.api_manager.obtener_registro_por_id(registro_id)
        if registro:
            self._mostrar_registro_en_ventana(registro, f"Registro ID: {registro_id}", "lightyellow")
        else:
            self._mostrar_error(f"No se encontró un registro con ID: {registro_id}")

    def _mostrar_registro_en_ventana(self, registro, titulo, color):
        ventana_registro = tk.Toplevel()
        ventana_registro.title(titulo)
        ventana_registro.geometry("600x200")
        ventana_registro.configure(bg=color)

        texto = (
            f"ID: {registro.get('id', 'N/A')}\n"
            f"Nombre: {registro.get('nombre', 'N/A')}\n"
            f"Horse: {registro.get('horse', 'N/A')}\n"
            f"Condado: {registro.get('condado', 'N/A')}\n"
            f"Hack: {registro.get('hack', 'N/A')}\n"
            f"Insecto: {registro.get('insecto', 'N/A')}\n"
            f"Color: {registro.get('color', 'N/A')}\n"
        )

        etiqueta = tk.Label(ventana_registro, text=texto, padx=10, pady=10, bg=color)
        etiqueta.pack()

        boton_regresar = tk.Button(ventana_registro, text="Regresar", command=ventana_registro.destroy, bg='cyan',
                                   fg='black')
        boton_regresar.pack(pady=10)

    def _mostrar_error(self, mensaje):
        ventana_error = tk.Toplevel()
        ventana_error.title("Error")
        ventana_error.geometry("300x100")
        etiqueta_error = tk.Label(ventana_error, text=mensaje, padx=10, pady=10)
        etiqueta_error.pack()
        boton_regresar = tk.Button(ventana_error, text="Cerrar", command=ventana_error.destroy, bg='red', fg='white')
        boton_regresar.pack(pady=5)


class VentanaManager:
    def __init__(self, registro_manager):
        self.registro_manager = registro_manager
        self.ventana = tk.Tk()
        self.ventana.title("Gustos del Condado")
        self.ventana.geometry("500x400")
        self.ventana.configure(bg='black')

        self.frame = tk.Frame(self.ventana, bg='black')
        self.frame.pack(expand=True)

        label_id = tk.Label(self.frame, text="Ingresa ID del Registro:", bg='black', fg='red', font=('Arial', 12))
        label_id.pack(pady=5)
        self.entry_id = tk.Entry(self.frame, bg='white')
        self.entry_id.pack(pady=5)

        self._crear_botones()

    def _crear_botones(self):
        boton_buscar_id = tk.Button(self.frame, text="Buscar Registro", command=self._buscar_registro, bg='cyan',
                                    fg='black', font=('Arial', 12))
        boton_buscar_id.pack(pady=10)

        boton_mostrar_ultimo = tk.Button(self.frame, text="Mostrar Último Registro",
                                         command=self.registro_manager.mostrar_ultimo_registro, bg='cyan', fg='black',
                                         font=('Arial', 12))
        boton_mostrar_ultimo.pack(pady=10)

        boton_mostrar_primer = tk.Button(self.frame, text="Mostrar Primer Registro",
                                         command=self.registro_manager.mostrar_primer_registro, bg='cyan', fg='black',
                                         font=('Arial', 12))
        boton_mostrar_primer.pack(pady=10)

        boton_mostrar_todos = tk.Button(self.frame, text="Mostrar Todos los Registros",
                                        command=self.registro_manager.mostrar_todos_registros, bg='cyan', fg='black',
                                        font=('Arial', 12))
        boton_mostrar_todos.pack(pady=10)

        boton_salir = tk.Button(self.frame, text="Salir", command=self.ventana.quit, bg='cyan', fg='black',
                                font=('Arial', 12))
        boton_salir.pack(pady=10)

    def _buscar_registro(self):
        try:
            registro_id = int(self.entry_id.get())
            self.registro_manager.mostrar_registro_por_id(registro_id)
        except ValueError:
            self.registro_manager._mostrar_error("Por favor, ingresa un número válido.")

    def ejecutar(self):
        self.ventana.mainloop()


class App:
    def __init__(self):
        self.api_manager = ApiManager()
        self.registro_manager = RegistroManager(self.api_manager)
        self.ventana_manager = VentanaManager(self.registro_manager)

    def run(self):
        self.ventana_manager.ejecutar()


# Ejecutar la aplicación
if __name__ == "__main__":
    app = App()
    app.run()
