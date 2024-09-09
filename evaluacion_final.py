import tkinter as tk
from tkinter import messagebox
import mysql.connector

#Conexión MySQL:

connection = mysql.connector.connect(
    host='localhost',
    database='evaluacion_final',
    user='root',
    password='password'
)
cursor = connection.cursor()

#Ventana principal:

root = tk.Tk()
root.title("Información de envío")

#Agregar:

def agregar_informacion():
    Numero_seguimiento = entry_numero.get()
    Origen = entry_origen.get()
    Destino = entry_destino.get()
    Fecha_prevista = entry_fecha.get()
    Estado = entry_estado.get()
    query = "INSERT INTO Envios (NumeroSeguimiento, Origen, Destino, FechaEntregaPrevista, Estado) VALUES (%s, %s, %s, %s, %s)"
    values = (Numero_seguimiento, Origen, Destino,Fecha_prevista,Estado)
    try:
        cursor.execute(query, values)
        connection.commit()
        messagebox.showinfo("Excelente!!", "Información de envío agregada con éxito")
        mostrar_informacion()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error no se pudo agregar información: {e}")

#Mostrar:

def mostrar_informacion():
    query = "SELECT * FROM Envios"
    cursor.execute(query)
    datos = cursor.fetchall()
    listbox.delete(0, tk.END)
    for dato in datos:
        listbox.insert(tk.END, dato)

#Actualizar:

def actualizar_informacion():
    Numero_seguimiento = entry_numero.get()
    Origen = entry_origen.get()
    Destino = entry_destino.get()
    Fecha_prevista = entry_fecha.get()
    Estado = entry_estado.get()
    query = "UPDATE Envios SET Origen= %s, Destino=%s, FechaEntregaPrevista=%s, Estado=%s WHERE NumeroSeguimiento= %s"
    values = (Origen, Destino,Fecha_prevista,Estado, Numero_seguimiento)
    try:
        cursor.execute (query,values)
        connection.commit()
        messagebox.showinfo ("Actualizado!", "Se ha actualizado la información con éxito")
        mostrar_informacion()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar la información: {e}")

#Eliminar:

def eliminar_informacion():
    try:
        selected = listbox.get(listbox.curselection())
        id = selected[0]
        query = "DELETE FROM Envios WHERE ID = %s"
        cursor.execute(query, (id,))
        connection.commit()
        messagebox.showinfo("Información eliminada","Se elimino la información con éxito")
        mostrar_informacion()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar la información: {e}")

#Frames:

frame_numero = tk.Frame(root)
frame_numero.pack(pady=10)

frame_origen = tk.Frame(root)
frame_origen.pack(pady=10)

frame_destino = tk.Frame(root)
frame_destino.pack(pady=10)

frame_fecha = tk.Frame(root)
frame_fecha.pack(pady=10)

frame_estado = tk.Frame(root)
frame_estado.pack(pady=10)

#Labels:

label_numero = tk.Label (frame_numero, text="Número de seguimiento: ")
label_numero.grid(row=0,column=0, padx=5, pady=5)

label_origen = tk.Label(frame_origen, text="Origen: ")
label_origen.grid(row=1, column=0, padx=5, pady=5)

label_destino = tk.Label(frame_destino, text="Destino: ")
label_destino.grid(row=2, column=0, padx=5, pady=5)

label_fecha = tk.Label(frame_fecha, text="Fecha estimada de entrega: ")
label_fecha.grid(row=3, column=0, padx=5, pady=5)

label_estado = tk.Label(frame_estado, text="Estado envío: ")
label_estado.grid(row=4, column=0, padx=5, pady=5)

#Entradas:

entry_numero = tk.Entry(frame_numero)
entry_numero.grid(row=0, column=1, padx=5, pady=5)

entry_origen = tk.Entry(frame_origen)
entry_origen.grid(row=1, column=1, padx=5, pady=5)

entry_destino = tk.Entry(frame_destino)
entry_destino.grid(row=2,column=1, padx=5, pady=5)

entry_fecha = tk.Entry(frame_fecha)
entry_fecha.grid(row=3, column=1, padx=5, pady=5)

entry_estado = tk.Entry(frame_estado)
entry_estado.grid(row=4, column=1, padx=5, pady=5)

#Botones:

button_agregar = tk.Button(root, text="Agregar información de envío",command=agregar_informacion)
button_agregar.pack(pady=10)

button_mostrar = tk.Button(root, text="Mostrar información de envío", command=mostrar_informacion)
button_mostrar.pack(pady=10)

button_actualizar = tk.Button(root, text="Actualizar información de envío", command=actualizar_informacion)
button_actualizar.pack(pady=10)

button_eliminar = tk.Button(root, text="Eliminar información", command=eliminar_informacion)
button_eliminar.pack(pady=10)

#Listbox:

listbox = tk.Listbox(root)
listbox.pack(pady=10)

#Cerrar conexión:

root.mainloop()

cursor.close()
connection.close()