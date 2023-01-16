
import tkinter as tk
import pandas as pd
ventana=tk.Tk()

nombres, direcciones, telefonos = [],[],[]

def confirmacion():
    global nombres, direcciones, telefonos
    nombres.append(nombre.get())
    direcciones.append(direccion.get())
    telefonos.append(telefono.get())

    nombre.delete(0, tk.END)
    direccion.delete(0, tk.END)
    telefono.delete(0, tk.END)

def archivo():
    global nombres, direcciones, telefonos
    datos = {'Nombre y apellido': nombres,'Dirección': direcciones,'Teléfono':telefonos}
    df = pd.DataFrame(datos, columns=['Nombre y apellido','Dirección','Teléfono'])
    nom_archivo = str(nombre_archivo.get()+'.csv')
    df = df.to_csv(nom_archivo)
    nombre_archivo.delete(0, tk.END)

ventana.config(width=400, height=250, bg='lightyellow')
ventana.title('Informacion personal')
label_nombre= tk.Label(ventana, text='ingrese su nombre y apellido: ', font=('Arial', 10), bg='lightyellow')
label_nombre.place(x=5, y=10)
nombre=tk.Entry(ventana, width=20)
nombre.place(x=180, y=10)
label_direccion= tk.Label(ventana, text='ingrese su direccion: ', font=('Arial', 10), bg='lightyellow')
label_direccion.place(x=5, y=40)
direccion=tk.Entry(ventana, width=20)
direccion.place(x=180, y=40)
label_telefono= tk.Label(ventana, text='ingrese su telefono: ', font=('Arial', 10), bg='lightyellow')
label_telefono.place(x=5, y=70)
telefono=tk.Entry(ventana, width=20)
telefono.place(x=180, y=70)
boton_confir=tk.Button(ventana, text='Agregar', bg='#995600', command=lambda: confirmacion())
boton_confir.place(x=180, y=100)
label_archivo=tk.Label(ventana, text='Indique nombre para \nel archivo:', font=('Arial', 10), bg='lightyellow')
label_archivo.place(x=5, y=140)
nombre_archivo=tk.Entry(ventana, width=20)
nombre_archivo.place(x=180, y=140)
boton_guardar=tk.Button(ventana, text='Guardar archivo', bg='#995600', command=lambda: archivo() )
boton_guardar.place(x=180, y=170)

tk.mainloop()
