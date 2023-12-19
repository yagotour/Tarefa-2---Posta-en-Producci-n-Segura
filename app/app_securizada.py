#Imports de Tkinter y lector de XML
import xml.etree.ElementTree as ET
from tkinter import Tk, Label, Entry, Button, messagebox
#Defino una variable para poner un límite de intentos
intentos = 3

#Función para leer usuario y contraseña en el users.xl
def verificar_credenciales(usuario, contraseña):
    try:
        tree = ET.parse("users.xml")
        root = tree.getroot()

        for usuario_elem in root.findall("usuario"):
            usuario_archivo = usuario_elem.find("nombre").text
            contraseña_archivo = usuario_elem.find("contrasena").text

            if usuario == usuario_archivo and contraseña == contraseña_archivo:
                return True
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo de credenciales no fue encontrado.")
    return False

#Funcion que valida el input con las credenciales de la anterior función, y chequea elnúmero de intetnos
def validar_ingreso(event=None):
    global intentos
    usuario_ingresado = entry_usuario.get()
    contraseña_ingresada = entry_contraseña.get()
    if verificar_credenciales(usuario_ingresado, contraseña_ingresada):
        messagebox.showinfo("Éxito", "Credenciales válidas. Acceso concedido.")
        # Restablecer el contador si es exitoso y cerrar la ventana
        intentos = 3
        ventana.destroy()
    else:
        intentos -= 1
        if intentos > 0:
            messagebox.showerror("Error", f"Credenciales inválidas. Intentos restantes: {intentos}")
        else:
            messagebox.showerror("Error", "Límite de intentos alcanzado. Aplicación cerrada.")
            ventana.destroy()

# Crear la ventana principal
ventana = Tk()
ventana.title("Aplicación Test  ")

# Etiquetas e inputs para usuario y contraseña
label_usuario = Label(ventana, text="Usuario:")
label_usuario.grid(row=0, column=0, padx=10, pady=10)
entry_usuario = Entry(ventana)
entry_usuario.grid(row=0, column=1, padx=10, pady=10)

label_contraseña = Label(ventana, text="Contraseña:")
label_contraseña.grid(row=1, column=0, padx=10, pady=10)
entry_contraseña = Entry(ventana, show="*")
entry_contraseña.grid(row=1, column=1, padx=10, pady=10)

# Validar contraseña con la tecla "Enter"
entry_contraseña.bind("<Return>", validar_ingreso)

# Botón para validar credenciales
boton_validar = Button(ventana, text="Validar", command=validar_ingreso)
boton_validar.grid(row=2, column=0, columnspan=2, pady=10)

# Iniciar la aplicación
ventana.mainloop()
