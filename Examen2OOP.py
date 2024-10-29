import tkinter as tk
from tkinter import ttk
import requests

# URL de la API
url = "https://671be6612c842d92c381b162.mockapi.io/test"

def obtener_registro_por_id(registro_id):
    try:
        response = requests.get(url)
        response.raise_for_status()
        registros = response.json()
        for registro in registros:
            if int(registro.get('id')) == registro_id:  # Aseguramos que compararemos como int
                return registro
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
    return None

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

def obtener_todos_los_registros():
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
    return []

def mostrar_registro():
    registro = obtener_ultimo_registro()
    if registro:
        ventana_registro = tk.Toplevel()
        ventana_registro.title("Último Registro")
        ventana_registro.geometry("600x200")
        ventana_registro.configure(bg='lightgreen')

        texto = (
            f"ID: {registro.get('id', 'N/A')}\n"
            f"Nombre: {registro.get('nombre', 'N/A')}\n"
            f"Horse: {registro.get('horse', 'N/A')}\n"
            f"Condado: {registro.get('condado', 'N/A')}\n"
            f"Hack: {registro.get('hack', 'N/A')}\n"
            f"Insecto: {registro.get('insecto', 'N/A')}\n"
            f"Color: {registro.get('color', 'N/A')}\n"
        )

        etiqueta = tk.Label(ventana_registro, text=texto, padx=10, pady=10, bg='lightgreen')
        etiqueta.pack()

        boton_regresar = tk.Button(ventana_registro, text="Regresar", command=ventana_registro.destroy, bg='cyan', fg='black')
        boton_regresar.pack(pady=10)
    else:
        print("No se pudo obtener el último registro.")

def mostrar_primer_registro():
    registro = obtener_primer_registro()
    if registro:
        ventana_registro = tk.Toplevel()
        ventana_registro.title("Primer Registro")
        ventana_registro.geometry("300x200")
        ventana_registro.configure(bg='lightblue')

        texto = (
            f"ID: {registro.get('id', 'N/A')}\n"
            f"Nombre: {registro.get('nombre', 'N/A')}\n"
            f"Horse: {registro.get('horse', 'N/A')}\n"
            f"Condado: {registro.get('condado', 'N/A')}\n"
            f"Hack: {registro.get('hack', 'N/A')}\n"
            f"Insecto: {registro.get('insecto', 'N/A')}\n"
            f"Color: {registro.get('color', 'N/A')}\n"
        )

        etiqueta = tk.Label(ventana_registro, text=texto, padx=10, pady=10, bg='lightblue')
        etiqueta.pack()

        boton_regresar = tk.Button(ventana_registro, text="Regresar", command=ventana_registro.destroy, bg='cyan', fg='black')
        boton_regresar.pack(pady=10)
    else:
        print("No se pudo obtener el primer registro.")

def mostrar_todos_registros():
    ventana_todos = tk.Toplevel()
    ventana_todos.title("Todos los Registros")
    ventana_todos.geometry("1800x500")
    ventana_todos.configure(bg='lightcoral')

    tree = ttk.Treeview(ventana_todos, columns=("ID", "Nombre", "Horse", "Condado", "Insecto", "Hack", "Color"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Horse", text="Horse")
    tree.heading("Condado", text="Condado")
    tree.heading("Hack", text="Hack")
    tree.heading("Insecto", text="Insecto")
    tree.heading("Color", text="Color")

    tree.tag_configure('yellow', background='lightyellow')
    tree.pack(expand=True, fill='both')

    boton_regresar = tk.Button(ventana_todos, text="Regresar", command=ventana_todos.destroy, bg='cyan', fg='black')
    boton_regresar.pack(pady=10)

    registros = obtener_todos_los_registros()
    for registro in registros:
        tree.insert("", "end", values=(registro.get('id', 'N/A'),
                                        registro.get('nombre', 'N/A'),
                                        registro.get('horse', 'N/A'),
                                        registro.get('condado', 'N/A'),
                                        registro.get('hack', 'N/A'),
                                        registro.get('insecto', 'N/A'),
                                        registro.get('color', 'N/A')),
                     tags=('yellow',))

def mostrar_registro_por_id():
    try:
        registro_id = int(entry_id.get())
        registro = obtener_registro_por_id(registro_id)
        if registro:
            ventana_registro = tk.Toplevel()
            ventana_registro.title(f"Registro ID: {registro_id}")
            ventana_registro.geometry("600x200")
            ventana_registro.configure(bg='lightyellow')

            texto = (
                f"ID: {registro.get('id', 'N/A')}\n"
                f"Nombre: {registro.get('nombre', 'N/A')}\n"
                f"Horse: {registro.get('horse', 'N/A')}\n"
                f"Condado: {registro.get('condado', 'N/A')}\n"
                f"Hack: {registro.get('hack', 'N/A')}\n"
                f"Insecto: {registro.get('insecto', 'N/A')}\n"
                f"Color: {registro.get('color', 'N/A')}\n"
            )

            etiqueta = tk.Label(ventana_registro, text=texto, padx=10, pady=10, bg='lightyellow')
            etiqueta.pack()

            boton_regresar = tk.Button(ventana_registro, text="Regresar", command=ventana_registro.destroy, bg='cyan', fg='black')
            boton_regresar.pack(pady=10)
        else:
            ventana_error = tk.Toplevel()
            ventana_error.title("Error")
            ventana_error.geometry("300x100")
            etiqueta_error = tk.Label(ventana_error, text=f"No se encontró un registro con ID: {registro_id}", padx=10, pady=10)
            etiqueta_error.pack()
            boton_regresar = tk.Button(ventana_error, text="Cerrar", command=ventana_error.destroy, bg='red', fg='white')
            boton_regresar.pack(pady=5)
    except ValueError:
        ventana_error = tk.Toplevel()
        ventana_error.title("Error")
        ventana_error.geometry("300x100")
        etiqueta_error = tk.Label(ventana_error, text="Por favor, ingresa un número válido.", padx=10, pady=10)
        etiqueta_error.pack()
        boton_regresar = tk.Button(ventana_error, text="Cerrar", command=ventana_error.destroy, bg='red', fg='white')
        boton_regresar.pack(pady=5)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gustos del Condado")
ventana.geometry("500x400")
ventana.configure(bg='black')

# Crear un marco para centrar los botones
frame = tk.Frame(ventana, bg='black')
frame.pack(expand=True)

# Casilla para ingresar ID
label_id = tk.Label(frame, text="Ingresa ID del Registro:", bg='black', fg='red',font=('Arial', 12))
label_id.pack(pady=5)
entry_id = tk.Entry(frame, bg='white')
entry_id.pack(pady=5)

# Botón para buscar el registro por ID
boton_buscar_id = tk.Button(frame, text="Buscar Registro", command=mostrar_registro_por_id, bg='cyan', fg='black', font=('Arial', 12))
boton_buscar_id.pack(pady=10)

# Botón para cargar el último registro
boton_mostrar_ultimo = tk.Button(frame, text="Mostrar Último Registro", command=mostrar_registro, bg='cyan', fg='black', font=('Arial', 12))
boton_mostrar_ultimo.pack(pady=10)

# Botón para mostrar el primer registro
boton_mostrar_primer = tk.Button(frame, text="Mostrar Primer Registro", command=mostrar_primer_registro, bg='cyan', fg='black', font=('Arial', 12))
boton_mostrar_primer.pack(pady=10)

# Botón para mostrar todos los registros
boton_mostrar_todos = tk.Button(frame, text="Mostrar Todos los Registros", command=mostrar_todos_registros, bg='cyan', fg='black', font=('Arial', 12))
boton_mostrar_todos.pack(pady=10)

# Botón para salir
boton_salir = tk.Button(frame, text="Salir", command=ventana.quit, bg='cyan', fg='black', font=('Arial', 12))
boton_salir.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()

