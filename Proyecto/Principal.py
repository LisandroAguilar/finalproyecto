import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter.font import Font
from tkinter import PhotoImage
from tkinter import ttk


def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="Proyecto"
    )
    return conexion

def registrar_acceso():
    ventana_acceso = tk.Toplevel(ventana_inicio)
    ventana_acceso.title("Registro de acceso")
    ventana_acceso.geometry("600x600+350+80")
    ventana_acceso.config(bg="#21A2F7")
        
    def cerrar_ventana_actual():
        ventana_acceso.destroy()
        ventana_inicio.deiconify()
            
    def limpiar_campos():
        entrada_nombre.delete(0, tk.END)
        entrada_paterno.delete(0, tk.END)
        entrada_materno.delete(0, tk.END)
        entrada_edad.delete(0, tk.END)
        entrada_contrasena.delete(0, tk.END)
            
    etiqueta_nombre = tk.Label(ventana_acceso, text="Nombre:", font=("Arial", 20), bg="#21A2F7", fg='black')
    etiqueta_nombre.pack()
    etiqueta_nombre.place(x=10, y=170, width=250, height=30)
            
    entrada_nombre = tk.Entry(ventana_acceso, font=("Arial", 14))
    entrada_nombre.pack()
    entrada_nombre.place(x=270, y=170, width=200, height=40)
            
    etiqueta_paterno = tk.Label(ventana_acceso, text="Apellido Paterno:", font=("Arial", 20), bg="#21A2F7", fg='black')
    etiqueta_paterno.pack()
    etiqueta_paterno.place(x=10, y=230, width=250, height=30)
            
    entrada_paterno = tk.Entry(ventana_acceso, font=("Arial", 14))
    entrada_paterno.pack()
    entrada_paterno.place(x=270, y=230, width=200, height=40)
            
    etiqueta_materno = tk.Label(ventana_acceso, text="Apellido Materno:", font=("Arial", 20), bg="#21A2F7", fg='black')
    etiqueta_materno.pack()
    etiqueta_materno.place(x=10, y=290, width=250, height=30)
            
    entrada_materno = tk.Entry(ventana_acceso, font=("Arial", 14))
    entrada_materno.pack()
    entrada_materno.place(x=270, y=290, width=200, height=40)
        
    etiqueta_edad = tk.Label(ventana_acceso, text="Edad:", font=("Arial", 20), bg="#21A2F7", fg='black')
    etiqueta_edad.pack()
    etiqueta_edad.place(x=10, y=350, width=250, height=30)
            
    entrada_edad = tk.Entry(ventana_acceso, font=("Arial", 14))
    entrada_edad.pack()
    entrada_edad.place(x=270, y=350, width=200, height=40)
        
    etiqueta_contrasena = tk.Label(ventana_acceso, text="Contraseña:", font=("Arial", 20), bg="#21A2F7", fg='black')
    etiqueta_contrasena.pack()
    etiqueta_contrasena.place(x=10, y=410, width=250, height=30)
            
    entrada_contrasena = tk.Entry(ventana_acceso, show="*", font=("Arial", 14))
    entrada_contrasena.pack()
    entrada_contrasena.place(x=270, y=410, width=200, height=40)
            
            
    def limpiar_mensaje():
        if mensaje_acceso.winfo_exists():
                mensaje_acceso.config(text="")
                    
    def guardar_registro():
                
        conexion = conectar()
        cursor = conexion.cursor()
            
        nombre = entrada_nombre.get()
        paterno = entrada_paterno.get()
        materno = entrada_materno.get()
        edad = entrada_edad.get()
        contrasena = entrada_contrasena.get()
                
        consulta = "INSERT INTO acceso (nombre, paterno, materno, edad, contrasena) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, paterno, materno, edad, contrasena)
        cursor.execute(consulta, valores)
                
        mensaje_acceso.config(text="Registro exitoso")
        ventana_acceso.after(3000, limpiar_mensaje) 
                
        conexion.commit()
        conexion.close()
        
    acceso_label = tk.Label(ventana_acceso, text="Registro de acceso", font=("Arial", 30), bg="#21A2F7", fg='black')
    acceso_label.pack()
    acceso_label.place(x=170, y=30, width=350, height=45)
                
    boton_guardar = tk.Button(ventana_acceso, text="Guardar", command=guardar_registro, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    boton_guardar.pack()
    boton_guardar.place(x=250, y=500, width=120, height=50)
                
    regresar = tk.Button(ventana_acceso, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    regresar.pack()
    regresar.place(x=100, y=500, width=120, height=50)
                
    boton_limpiar = tk.Button(ventana_acceso, text="Limpiar", command=limpiar_campos, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    boton_limpiar.pack()
    boton_limpiar.place(x=400, y=500, width=120, height=50)
                
    mensaje_acceso = tk.Label(ventana_acceso, text="", fg="red", font=("Arial", 18), bg="#21A2F7")
    mensaje_acceso.pack()
    mensaje_acceso.place(x=60, y=460)
    
    imagen = PhotoImage(file="logo.png")
    label_imagen = Label(ventana_acceso, image=imagen, bg="#21A2F7", fg="white")
    label_imagen.place(x=0, y=0, width=150, height=150)
            
    ventana_inicio.withdraw()
            
    ventana_acceso.mainloop()

def validar_ingreso():
    
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="Proyecto"
    )
    
    nombre = nombre_usuario.get()
    contrasena = password.get()
    
    if not nombre or not contrasena:
        mensaje_campos_inicio.config(text="Por favor, rellena todos los campos")
        ventana_inicio.after(3000, limpiar_mensaje_campos)
        return
    
    cursor = conexion.cursor()
    consulta = "SELECT * FROM acceso WHERE nombre=%s AND contrasena=%s"
    parametros = (nombre, contrasena)
    cursor.execute(consulta, parametros)
    resultado = cursor.fetchone()
    
    if resultado is None:
        mensaje_incorrecto_inicio.config(text="Nombre de usuario y/o contraseña incorrectos")
        ventana_inicio.after(3000, limpiar_mensaje_incorrecto)
        return
    
    else:
        ventana_inicio.destroy()
        abrir_ventana_principal()
        

def abrir_ventana_principal():
    
    ventana_principal = tk.Tk()
    ventana_principal.title("Principal")
    ventana_principal.geometry("600x600+350+80")
    ventana_principal.config(bg="#21A2F7") 
    
    def modificaciones():
        
        ventana_modificaciones = tk.Toplevel(ventana_principal)
        ventana_modificaciones.title("Modoficaciones")
        ventana_modificaciones.geometry("600x600+350+80")
        ventana_modificaciones.config(bg="#21A2F7")
        
        def cerrar_ventana_actual():
            ventana_modificaciones.destroy()
            ventana_principal.deiconify()
            
        def registro_basura():
            ventana_registro_basura = tk.Toplevel(ventana_modificaciones)
            ventana_registro_basura.title("Registro de ingreso de basura")
            ventana_registro_basura.geometry("600x600+350+80")
            ventana_registro_basura.config(bg="#21A2F7")
            
            def cerrar_ventana_actual():
                ventana_registro_basura.destroy()
                ventana_modificaciones.deiconify()
                
            def limpiar_mensaje():
                mensaje_registro_basura.config(text="")
            
            def limpiar_campos():
                entrada_id_usuario.delete(0, tk.END)
                entrada_ID_Basura.delete(0, tk.END)
                entrada_Peso.delete(0, tk.END)
                seleccion_Estado.delete(0, tk.END)
                entrada_Precio.delete(0, tk.END)
                
            etiqueta_id_usuario = tk.Label(ventana_registro_basura, text="Id_Usuario:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_id_usuario.pack()
            etiqueta_id_usuario.place(x=10, y=50, width=250, height=30)
            
            entrada_id_usuario = tk.Entry(ventana_registro_basura, font=("Arial", 14))
            entrada_id_usuario.pack()
            entrada_id_usuario.place(x=270, y=50, width=200, height=40)
            
            etiqueta_ID_Basura = tk.Label(ventana_registro_basura, text="ID_Basura:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_ID_Basura.pack()
            etiqueta_ID_Basura.place(x=10, y=110, width=250, height=30)
            
            entrada_ID_Basura = tk.Entry(ventana_registro_basura, font=("Arial", 14))
            entrada_ID_Basura.pack()
            entrada_ID_Basura.place(x=270, y=110, width=200, height=40)
            
            etiqueta_Peso = tk.Label(ventana_registro_basura, text="Peso:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_Peso.pack()
            etiqueta_Peso.place(x=10, y=170, width=250, height=30)
            
            entrada_Peso = tk.Entry(ventana_registro_basura, font=("Arial", 14))
            entrada_Peso.pack()
            entrada_Peso.place(x=270, y=170, width=200, height=40)
            
            # Lista de opciones para el combobox
            opciones_usuarios = ['A', 'B', 'C']

            # Crear el combobox
            etiqueta_combobox = tk.Label(ventana_registro_basura, text="Estado:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_combobox.pack()
            etiqueta_combobox.place(x=10, y=230, width=250, height=30)
            
            seleccion_Estado = ttk.Combobox(ventana_registro_basura, values=opciones_usuarios, font=("Arial", 14))
            seleccion_Estado.pack()
            seleccion_Estado.place(x=270, y=230, width=200, height=40)
            
            etiqueta_Precio = tk.Label(ventana_registro_basura, text="Precio:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_Precio.pack()
            etiqueta_Precio.place(x=10, y=290, width=250, height=30)
            
            entrada_Precio = tk.Entry(ventana_registro_basura, font=("Arial", 14))
            entrada_Precio.pack()
            entrada_Precio.place(x=270, y=290, width=200, height=40)
            
            
            
            def guarada_usu_modi():
                
                conexion = conectar()
                cursor = conexion.cursor()
                
                id_usuario = entrada_id_usuario.get() 
                ID_Basura = entrada_ID_Basura.get()
                Peso = entrada_Peso.get()
                Estado = seleccion_Estado.get()
                Precio = entrada_Precio.get()

                consulta = "INSERT INTO Basura (ID_Basura, Peso, Estado, Precio, ID_Usuario) VALUES (%s, %s, %s, %s, %s)"
                valores = (ID_Basura, Peso, Estado, Precio, id_usuario)  
                
                cursor.execute(consulta, valores)

                conexion.commit()

                mensaje_registro_basura.config(text="Registro exitoso")
                ventana_registro_basura.after(3000, limpiar_mensaje)

                cursor.close()
                conexion.close()

                
            regresar_modificar = tk.Button(ventana_registro_basura, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            regresar_modificar.pack()
            regresar_modificar.place(x=100, y=500, width=120, height=50)
            
            boton_guardar = tk.Button(ventana_registro_basura, text="Guardar", command=guarada_usu_modi, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_guardar.pack()
            boton_guardar.place(x=250, y=500, width=120, height=50)
            
            boton_limpiar = tk.Button(ventana_registro_basura, text="Limpiar", command=limpiar_campos, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_limpiar.pack()
            boton_limpiar.place(x=400, y=500, width=120, height=50)
                        
            mensaje_registro_basura = tk.Label(ventana_registro_basura, text="", fg="red", font=("Arial", 18), bg="#21A2F7")
            mensaje_registro_basura.pack()
            mensaje_registro_basura.place(x=100, y=460)
                
            ventana_modificaciones.withdraw()
            
            ventana_registro_basura.mainloop()
                
        def consulta_basura():
            ventana_consulta_basura = tk.Toplevel(ventana_modificaciones)
            ventana_consulta_basura.title("Registros de basura")
            ventana_consulta_basura.geometry("600x600+350+80")
            ventana_consulta_basura.config(bg="#21A2F7")
            
            def cerrar_ventana_actual():
                ventana_consulta_basura.destroy()
                ventana_modificaciones.deiconify()
                
            regresar_modificar = tk.Button(ventana_consulta_basura, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            regresar_modificar.pack()
            regresar_modificar.place(x=100, y=500, width=120, height=50)
            
            
                
            ventana_modificaciones.withdraw()
            
            ventana_consulta_basura.mainloop()
            
        boton_modificar_usuario = tk.Button(ventana_modificaciones, text="Registro de Basura", command=registro_basura, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        boton_modificar_usuario.pack()
        boton_modificar_usuario.place(x=230, y=500, width=150, height=50)
            
        boton_modificar_recicladora = tk.Button(ventana_modificaciones, text="Consulta", command=consulta_basura, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        boton_modificar_recicladora.pack()
        boton_modificar_recicladora.place(x=405, y=500, width=150, height=50)
                            
        regresar_modificar = tk.Button(ventana_modificaciones, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        regresar_modificar.pack()
        regresar_modificar.place(x=50, y=500, width=150, height=50)
        
        imagen = PhotoImage(file="logo.png")
        label_imagen = Label(ventana_modificaciones, image=imagen, bg="#21A2F7", fg="white")
        label_imagen.place(x=0, y=0, width=190, height=190)
            
        ventana_principal.withdraw()
            
        ventana_modificaciones.mainloop()

    def registrar():
    
        ventana_registro = tk.Toplevel(ventana_principal)
        ventana_registro.title("Registros")
        ventana_registro.geometry("600x600+350+80")
        ventana_registro.config(bg="#21A2F7") 
        
        def cerrar_ventana_actual():
            ventana_registro.destroy()
            ventana_principal.deiconify()
        
        def registrar_usuario():
        
            ventana_registro_usuario = tk.Toplevel(ventana_registro)
            ventana_registro_usuario.title("Registro de usuario")
            ventana_registro_usuario.geometry("600x600+350+80")
            ventana_registro_usuario.config(bg="#21A2F7")
        
            def cerrar_ventana_actual():
                ventana_registro_usuario.destroy()
                ventana_registro.deiconify()
            
            def limpiar_campos():
                entrada_Id.delete(0, tk.END)
                entrada_contrasena.delete(0, tk.END)
                entrada_nombre.delete(0, tk.END)
                entrada_paterno.delete(0, tk.END)
                entrada_materno.delete(0, tk.END)
                entrada_telefono.delete(0, tk.END)
                entrada_correo.delete(0, tk.END)
            
            etiqueta_Id = tk.Label(ventana_registro_usuario, text="Id:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_Id.pack()
            etiqueta_Id.place(x=10, y=50, width=250, height=30)
            
            entrada_Id = tk.Entry(ventana_registro_usuario, font=("Arial", 14))
            entrada_Id.pack()
            entrada_Id.place(x=270, y=50, width=200, height=40)
            
            etiqueta_contrasena = tk.Label(ventana_registro_usuario, text="Contraseña:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_contrasena.pack()
            etiqueta_contrasena.place(x=10, y=110, width=250, height=30)
            
            entrada_contrasena = tk.Entry(ventana_registro_usuario, show="*", font=("Arial", 14))
            entrada_contrasena.pack()
            entrada_contrasena.place(x=270, y=110, width=200, height=40)
            
            etiqueta_nombre = tk.Label(ventana_registro_usuario, text="Nombre:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_nombre.pack()
            etiqueta_nombre.place(x=10, y=170, width=250, height=30)
            
            entrada_nombre = tk.Entry(ventana_registro_usuario, font=("Arial", 14))
            entrada_nombre.pack()
            entrada_nombre.place(x=270, y=170, width=200, height=40)
            
            etiqueta_paterno = tk.Label(ventana_registro_usuario, text="Apellido Paterno:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_paterno.pack()
            etiqueta_paterno.place(x=10, y=230, width=250, height=30)
            
            entrada_paterno = tk.Entry(ventana_registro_usuario, font=("Arial", 14))
            entrada_paterno.pack()
            entrada_paterno.place(x=270, y=230, width=200, height=40)
            
            etiqueta_materno = tk.Label(ventana_registro_usuario, text="Apellido Materno:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_materno.pack()
            etiqueta_materno.place(x=10, y=290, width=250, height=30)
            
            entrada_materno = tk.Entry(ventana_registro_usuario, font=("Arial", 14))
            entrada_materno.pack()
            entrada_materno.place(x=270, y=290, width=200, height=40)
            
            etiqueta_telefono = tk.Label(ventana_registro_usuario, text="Telefono:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_telefono.pack()
            etiqueta_telefono.place(x=10, y=350, width=250, height=30)
            
            entrada_telefono = tk.Entry(ventana_registro_usuario, font=("Arial", 14))
            entrada_telefono.pack()
            entrada_telefono.place(x=270, y=350, width=200, height=40)
            
            etiqueta_correo = tk.Label(ventana_registro_usuario, text="Correo:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_correo.pack()
            etiqueta_correo.place(x=10, y=410, width=250, height=30)
            
            entrada_correo = tk.Entry(ventana_registro_usuario, font=("Arial", 14))
            entrada_correo.pack()
            entrada_correo.place(x=270, y=410, width=200, height=40)
            
            def limpiar_mensaje():
                if mensaje_guardado.winfo_exists():
                    mensaje_guardado.config(text="")
                    
            def guardar_registro():
                
                conexion = conectar()
                cursor = conexion.cursor()
                
                Id = entrada_Id.get()
                contrasena = entrada_contrasena.get()
                nombre = entrada_nombre.get()
                paterno = entrada_paterno.get()
                materno = entrada_materno.get()
                telefono = entrada_telefono.get()
                correo = entrada_correo.get()
                
                consulta = "INSERT INTO Usuario (ID_Usuario, Contrasena, Nombre, Paterno, Materno, Telefono, Correo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                valores = (Id, contrasena, nombre, paterno, materno, telefono, correo)
                cursor.execute(consulta, valores)
                
                mensaje_guardado.config(text="Registro exitoso")
                ventana_registro_usuario.after(3000, limpiar_mensaje) 
                
                conexion.commit()
                conexion.close()
                
            boton_guardar = tk.Button(ventana_registro_usuario, text="Guardar", command=guardar_registro, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_guardar.pack()
            boton_guardar.place(x=250, y=500, width=120, height=50)
            
            regresar = tk.Button(ventana_registro_usuario, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            regresar.pack()
            regresar.place(x=100, y=500, width=120, height=50)
            
            boton_limpiar = tk.Button(ventana_registro_usuario, text="Limpiar", command=limpiar_campos, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_limpiar.pack()
            boton_limpiar.place(x=400, y=500, width=120, height=50)
            
            mensaje_guardado = tk.Label(ventana_registro_usuario, text="", fg="red", font=("Arial", 18), bg="#21A2F7")
            mensaje_guardado.pack()
            mensaje_guardado.place(x=60, y=460)
            
            ventana_registro.withdraw()
            
            ventana_registro_usuario.mainloop()
            
        def registrar_recicladora():
            
            ventana_registro_recicladora = tk.Toplevel(ventana_registro)
            ventana_registro_recicladora.title("Registro de recicladora")
            ventana_registro_recicladora.geometry("600x600+350+80")
            ventana_registro_recicladora.config(bg="#21A2F7")
            
            def cerrar_ventana_actual():
                ventana_registro_recicladora.destroy()
                ventana_registro.deiconify()
            
            def limpiar_campos():
                entrada_Id.delete(0, tk.END)
                entrada_nombre.delete(0, tk.END)
                entrada_direccion.delete(0, tk.END)
                entrada_telefono.delete(0, tk.END)
                entrada_correo.delete(0, tk.END)
                entrada_tipo.delete(0,tk, END)
                
            etiqueta_Id = tk.Label(ventana_registro_recicladora, text="Id:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_Id.pack()
            etiqueta_Id.place(x=10, y=50, width=250, height=30)
            
            entrada_Id = tk.Entry(ventana_registro_recicladora, font=("Arial", 14))
            entrada_Id.pack()
            entrada_Id.place(x=270, y=50, width=200, height=40)
            
            etiqueta_nombre = tk.Label(ventana_registro_recicladora, text="Nombre:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_nombre.pack()
            etiqueta_nombre.place(x=10, y=110, width=250, height=30)
            
            entrada_nombre = tk.Entry(ventana_registro_recicladora, font=("Arial", 14))
            entrada_nombre.pack()
            entrada_nombre.place(x=270, y=110, width=200, height=40)
            
            etiqueta_direccion = tk.Label(ventana_registro_recicladora, text="Dirección:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_direccion.pack()
            etiqueta_direccion.place(x=10, y=170, width=250, height=30)
            
            entrada_direccion = tk.Entry(ventana_registro_recicladora, font=("Arial", 14))
            entrada_direccion.pack()
            entrada_direccion.place(x=270, y=170, width=200, height=40)
            
            etiqueta_telefono = tk.Label(ventana_registro_recicladora, text="Telefono:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_telefono.pack()
            etiqueta_telefono.place(x=10, y=230, width=250, height=30)
            
            entrada_telefono = tk.Entry(ventana_registro_recicladora, font=("Arial", 14))
            entrada_telefono.pack()
            entrada_telefono.place(x=270, y=230, width=200, height=40)
            
            etiqueta_correo = tk.Label(ventana_registro_recicladora, text="Correo:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_correo.pack()
            etiqueta_correo.place(x=10, y=290, width=250, height=30)
            
            entrada_correo = tk.Entry(ventana_registro_recicladora, font=("Arial", 14))
            entrada_correo.pack()
            entrada_correo.place(x=270, y=290, width=200, height=40)
            
            etiqueta_tipo = tk.Label(ventana_registro_recicladora, text="Tipo:", font=("Arial", 20), bg="#21A2F7", fg='black')
            etiqueta_tipo.pack()
            etiqueta_tipo.place(x=10, y=350, width=250, height=30)
            
            entrada_tipo = tk.Entry(ventana_registro_recicladora, font=("Arial", 14))
            entrada_tipo.pack()
            entrada_tipo.place(x=270, y=350, width=200, height=40)
            
            def limpiar_mensaje():
                mensaje_guardado.config(text="")
                
            def guardar_recicladora():
                
                conexion = conectar()
                cursor = conexion.cursor()
                
                Id = entrada_Id.get()
                nombre = entrada_nombre.get()
                direccion = entrada_direccion.get()
                telefono = entrada_telefono.get()
                correo = entrada_correo.get()
                tipo = entrada_tipo.get()
                
                consulta = "INSERT INTO Recicladora (ID_Recicladora, Nombre, Direccion, Telefono, Correo, Tipo) VALUES (%s, %s, %s, %s, %s, %s)"
                valores = (Id, nombre, direccion, telefono, correo, tipo)
                cursor.execute(consulta, valores)
                
                mensaje_guardado.config(text="Registro exitoso")
                ventana_registro_recicladora.after(3000, limpiar_mensaje) 
                
                conexion.commit()
                conexion.close()
                
            boton_guardar = tk.Button(ventana_registro_recicladora, text="Guardar", command=guardar_recicladora, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_guardar.pack()
            boton_guardar.place(x=250, y=500, width=120, height=50)
            
            regresar = tk.Button(ventana_registro_recicladora, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            regresar.pack()
            regresar.place(x=100, y=500, width=120, height=50)
            
            boton_limpiar = tk.Button(ventana_registro_recicladora, text="Limpiar", command=limpiar_campos, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_limpiar.pack()
            boton_limpiar.place(x=400, y=500, width=120, height=50)
            
            mensaje_guardado = tk.Label(ventana_registro_recicladora, text="", fg="red", font=("Arial", 18), bg="#21A2F7")
            mensaje_guardado.pack()
            mensaje_guardado.place(x=60, y=460)
                
            ventana_registro.withdraw()
            
            ventana_registro_recicladora.mainloop()
                
        boton_usuario_usuario = tk.Button(ventana_registro, text="Nuevo usuario", command=registrar_usuario, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        boton_usuario_usuario.pack()
        boton_usuario_usuario.place(x=245, y=500, width=120, height=50)
        
        boton_recicladora_recicladora = tk.Button(ventana_registro, text="Nueva recicladora", command=registrar_recicladora, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        boton_recicladora_recicladora.pack()
        boton_recicladora_recicladora.place(x=400, y=500, width=140, height=50)
                        
        regresar_usuario = tk.Button(ventana_registro, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        regresar_usuario.pack()
        regresar_usuario.place(x=80, y=500, width=120, height=50)
        
        imagen = PhotoImage(file="logo.png")
        label_imagen = Label(ventana_registro, image=imagen, bg="#21A2F7", fg="white")
        label_imagen.place(x=0, y=0, width=190, height=190)
                
        ventana_principal.withdraw()
        
        ventana_registro.mainloop()

    def eliminar():
        ventana_eliminar = tk.Toplevel(ventana_principal)
        ventana_eliminar.title("Eliminar registro")
        ventana_eliminar.geometry("600x600+350+80")
        ventana_eliminar.config(bg="#21A2F7") 
        
        def cerrar_ventana_actual():
                ventana_eliminar.destroy()
                ventana_principal.deiconify()
        
        def eliminar_usuario():
            ventana_eliminar_usuario = tk.Toplevel(ventana_eliminar)
            ventana_eliminar_usuario.title("Eliminar usuario")
            ventana_eliminar_usuario.geometry("600x600+350+80")
            ventana_eliminar_usuario.config(bg="#21A2F7") 
            
            def cerrar_ventana_actual():
                ventana_eliminar_usuario.destroy()
                ventana_eliminar.deiconify()
                
            def limpiar_campos():
                entrada_id.delete(0, tk.END)
                entrada_nombre.delete(0, tk.END)

            etiqueta_id = tk.Label(ventana_eliminar_usuario, text="Id:", font=("Arial", 18), bg="#21A2F7", fg='black')
            etiqueta_id.pack()
            etiqueta_id.place(x=170, y=30, width=280, height=35)
            
            entrada_id = tk.Entry(ventana_eliminar_usuario)
            entrada_id.pack()
            entrada_id.place(x=170, y=100, width=280, height=35)
            
            etiqueta_nombre = tk.Label(ventana_eliminar_usuario, text="Nombre:", font=("Arial", 18), bg="#21A2F7", fg='black')
            etiqueta_nombre.pack()
            etiqueta_nombre.place(x=170, y=130, width=280, height=35)
            
            entrada_nombre = tk.Entry(ventana_eliminar_usuario)
            entrada_nombre.pack()
            entrada_nombre.place(x=170, y=200, width=280, height=35)

            def eliminar_registro():
                
                conexion = conectar()
                cursor = conexion.cursor()
                
                id = int(entrada_id.get())
                
                consulta = "DELETE FROM Usuario WHERE ID_Usuario = %s and Nombre = %s"
                valores = (id,)
                cursor.execute(consulta, valores)
                
                conexion.commit()
                conexion.close()
                
                cerrar_ventana_actual()
            
            boton_eliminar_usuario = tk.Button(ventana_eliminar_usuario, text="Guardar", command=eliminar_registro, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_eliminar_usuario.pack()
            boton_eliminar_usuario.place(x=250, y=500, width=120, height=50)
                        
            regresar = tk.Button(ventana_eliminar_usuario, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            regresar.pack()
            regresar.place(x=100, y=500, width=120, height=50)
                        
            boton_limpiar = tk.Button(ventana_eliminar_usuario, text="Limpiar", command=limpiar_campos, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_limpiar.pack()
            boton_limpiar.place(x=400, y=500, width=120, height=50)
        
            ventana_eliminar.withdraw()
                
            ventana_eliminar_usuario.mainloop()
            
        def eliminar_recicladora():
            
            ventana_eliminar_recicladora = tk.Toplevel(ventana_eliminar)
            ventana_eliminar_recicladora.title("Eliminar usuario")
            ventana_eliminar_recicladora.geometry("600x600+350+80")
            ventana_eliminar_recicladora.config(bg="#21A2F7") 
            
            def cerrar_ventana_actual():
                ventana_eliminar_recicladora.destroy()
                ventana_eliminar.deiconify()
                
            def limpiar_campos():
                entrada_id.delete(0, tk.END)
                entrada_nombre.delete(0, tk.END)
            
            etiqueta_id = tk.Label(ventana_eliminar_recicladora, text="Id:")
            etiqueta_id.pack()
            etiqueta_id.place(x=170, y=30, width=280, height=35)
            
            entrada_id = tk.Entry(ventana_eliminar_recicladora)
            entrada_id.pack()
            entrada_id.place(x=170, y=100, width=280, height=35)
            
            etiqueta_nombre = tk.Label(ventana_eliminar_recicladora, text="Nombre:")
            etiqueta_nombre.pack()
            etiqueta_nombre.place(x=170, y=130, width=280, height=35)
            
            entrada_nombre = tk.Entry(ventana_eliminar_recicladora)
            entrada_nombre.pack()
            entrada_nombre.place(x=170, y=200, width=280, height=35)

            def eliminar_registro():
                
                conexion = conectar()
                cursor = conexion.cursor()
                
                id = int(entrada_id.get())
                
                consulta = "DELETE FROM Recicladora WHERE ID_Recicladora = %s and Nombre = %s"
                valores = (id, nombre)
                cursor.execute(consulta, valores)
                
                conexion.commit()
                conexion.close()
                
                cerrar_ventana_actual()
            
            boton_eliminar_recicladora = tk.Button(ventana_eliminar_recicladora, text="Guardar", command=eliminar_registro, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_eliminar_recicladora.pack()
            boton_eliminar_recicladora.place(x=250, y=500, width=120, height=50)
            
            regresar = tk.Button(ventana_eliminar_recicladora, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            regresar.pack()
            regresar.place(x=100, y=500, width=120, height=50)
            
            boton_limpiar = tk.Button(ventana_eliminar_recicladora, text="Limpiar", command=limpiar_campos, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_limpiar.pack()
            boton_limpiar.place(x=400, y=500, width=120, height=50)
            
            
            ventana_eliminar.withdraw()
                
            ventana_eliminar_recicladora.mainloop()
            
        boton_usuario_usuario = tk.Button(ventana_eliminar, text="Eliminar usuario", command=eliminar_usuario, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        boton_usuario_usuario.pack()
        boton_usuario_usuario.place(x=250, y=500, width=120, height=50)
        
        boton_recicladora_recicladora = tk.Button(ventana_eliminar, text="Eliminar recicladora", command=eliminar_recicladora, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        boton_recicladora_recicladora.pack()
        boton_recicladora_recicladora.place(x=400, y=500, width=140, height=50)
                        
        regresar_eliminar = tk.Button(ventana_eliminar, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        regresar_eliminar.pack()
        regresar_eliminar.place(x=100, y=500, width=120, height=50)
        
        imagen = PhotoImage(file="logo.png")
        label_imagen = Label(ventana_eliminar, image=imagen, bg="#21A2F7", fg="white")
        label_imagen.place(x=0, y=0, width=190, height=190)
        
        ventana_principal.withdraw()
        
        ventana_eliminar.mainloop()
        
    def creditos():
        ventana_creditos = tk.Toplevel(ventana_principal)
        ventana_creditos.title("Creditos")
        ventana_creditos.geometry("600x600+350+80")
        ventana_creditos.config(bg="#21A2F7")
        
        def cerrar_ventana_actual():
            ventana_creditos.destroy()
            ventana_principal.deiconify()
        
        etiqueta_creditos = tk.Label(ventana_creditos, text="Software creado por Alumnos de Sistemas Compucionales del 4K")
        etiqueta_creditos.pack()
        etiqueta_creditos.place(x=170, y=30, width=400, height=35)
        
        regresar_eliminar = tk.Button(ventana_creditos, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        regresar_eliminar.pack()
        regresar_eliminar.place(x=100, y=500, width=120, height=50)
        
        imagen = PhotoImage(file="logo.png")
        label_imagen = Label(ventana_creditos, image=imagen, bg="#21A2F7", fg="white")
        label_imagen.place(x=0, y=0, width=190, height=190)
        
        ventana_principal.withdraw()
        
        ventana_creditos.mainloop()
        
    def contactos():
        ventana_contactos = tk.Toplevel(ventana_principal)
        ventana_contactos.title("Contactos")
        ventana_contactos.geometry("600x600+350+80")
        ventana_contactos.config(bg="#21A2F7")
        
        def cerrar_ventana_actual():
            ventana_contactos.destroy()
            ventana_principal.deiconify()
        
        etiqueta_creditos = tk.Label(ventana_contactos, text="Lisandro Aguilar Cano")
        etiqueta_creditos.pack()
        etiqueta_creditos.place(x=170, y=30, width=280, height=35)
        
        regresar_eliminar = tk.Button(ventana_contactos, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        regresar_eliminar.pack()
        regresar_eliminar.place(x=100, y=500, width=120, height=50)
        
        imagen = PhotoImage(file="logo.png")
        label_imagen = Label(ventana_contactos, image=imagen, bg="#21A2F7", fg="white")
        label_imagen.place(x=0, y=0, width=190, height=190)
        
        ventana_principal.withdraw()
        
        ventana_contactos.mainloop()
            

    def ver_registros():
        ventana_consultas = tk.Toplevel(ventana_principal)
        ventana_consultas.title("Consultas")
        ventana_consultas.geometry("600x600+350+80")
        ventana_consultas.config(bg="#21A2F7")
        
        def cerrar_ventana_actual():
            ventana_consultas.destroy()
            ventana_principal.deiconify()
        
        def consulta_usuario():
            ventana_consulta_usuario = tk.Toplevel(ventana_consultas)
            ventana_consulta_usuario.title("Consulta de usuarios")
            ventana_consulta_usuario.geometry("630x600+350+80")
            ventana_consulta_usuario.config(bg="#21A2F7")
            
            def cerrar_ventana_actual():
                ventana_consulta_usuario.destroy()
                ventana_consultas.deiconify()
            
            conexion = conectar()
            cursor = conexion.cursor()

            # Ejecutar la consulta SELECT
            consulta = "SELECT * FROM Usuario"
            cursor.execute(consulta)
            resultados = cursor.fetchall()

            text_area = tk.Text(ventana_consulta_usuario)
            text_area.configure(width=50, height=10)
            text_area.config(bg="#21A2F7")
            text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Crear encabezado de la tabla
            encabezado = ["ID Usuario", "Contraseña", "Nombre", "Paterno", "Materno", "Teléfono", "Correo"]
            for i in range(len(encabezado)):
                etiqueta_encabezado = tk.Label(text_area, text=encabezado[i], font=("Arial", 12, "bold"), relief="solid", borderwidth=1, bg="#EFEFEF", padx=5, pady=5)
                etiqueta_encabezado.grid(row=0, column=i, sticky="nsew")

            # Mostrar los registros de la tabla
            for i in range(len(resultados)):
                for j in range(len(resultados[i])):
                    etiqueta_resultado = tk.Label(text_area, text=str(resultados[i][j]), font=("Arial", 10), relief="solid", borderwidth=1, bg="#FFFFFF", padx=5, pady=5)
                    etiqueta_resultado.grid(row=i+1, column=j, sticky="nsew")
            
            # Colocar el Text widget en la ventana principal
            text_area.place(x=0, y=0, width=630, height=400)
            
            # Crear botones
            boton_salir = tk.Button(ventana_consulta_usuario, text="Salir", font=("Arial", 12), command=cerrar_ventana_actual)
            boton_salir.place(x=500, y=550)
            
            conexion.close()
            
            ventana_consultas.withdraw()
            
            ventana_consulta_usuario.mainloop()
            
        def consulta_basu():
            ventana_consulta_basu = tk.Toplevel(ventana_consultas)
            ventana_consulta_basu.title("Consulta de usuarios")
            ventana_consulta_basu.geometry("630x600+350+80")
            ventana_consulta_basu.config(bg="#21A2F7")
            
            def cerrar_ventana_actual():
                ventana_consulta_basu.destroy()
                ventana_consultas.deiconify()
            
            conexion = conectar()
            cursor = conexion.cursor()

            # Ejecutar la consulta SELECT
            consulta = "SELECT * FROM Usuario"
            cursor.execute(consulta)
            resultados = cursor.fetchall()

            text_area = tk.Text(ventana_consulta_basu)
            text_area.configure(width=50, height=10)
            text_area.config(bg="#21A2F7")
            text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Crear encabezado de la tabla
            encabezado = ["ID Usuario", "Contraseña", "Nombre", "Paterno", "Materno", "Teléfono", "Correo"]
            for i in range(len(encabezado)):
                etiqueta_encabezado = tk.Label(text_area, text=encabezado[i], font=("Arial", 12, "bold"), relief="solid", borderwidth=1, bg="#EFEFEF", padx=5, pady=5)
                etiqueta_encabezado.grid(row=0, column=i, sticky="nsew")

            # Mostrar los registros de la tabla
            for i in range(len(resultados)):
                for j in range(len(resultados[i])):
                    etiqueta_resultado = tk.Label(text_area, text=str(resultados[i][j]), font=("Arial", 10), relief="solid", borderwidth=1, bg="#FFFFFF", padx=5, pady=5)
                    etiqueta_resultado.grid(row=i+1, column=j, sticky="nsew")
            
            # Colocar el Text widget en la ventana principal
            text_area.place(x=0, y=0, width=630, height=400)
            
            # Crear botones
            boton_salir = tk.Button(ventana_consulta_basu, text="Salir", font=("Arial", 12), command=cerrar_ventana_actual)
            boton_salir.place(x=400, y=450)
            
            conexion.close()
            
            ventana_consultas.withdraw()
            
            ventana_consulta_basu.mainloop()
            
        consulta_usu = tk.Button(ventana_consultas, text="Consulta usuario", command=consulta_usuario, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        consulta_usu.pack()
        consulta_usu.place(x=10, y=430, width=120, height=80)
        
        consulta_basu = tk.Button(ventana_consultas, text="Consulta de basura", command=consulta_basu, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        consulta_basu.pack()
        consulta_basu.place(x=200, y=430, width=120, height=80)
        
        salir = tk.Button(ventana_consultas, text="Salir", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        salir.pack()
        salir.place(x=390, y=430, width=120, height=80)
        
        imagen = PhotoImage(file="logo.png")
        label_imagen = Label(ventana_consultas, image=imagen, bg="#21A2F7", fg="white")
        label_imagen.place(x=0, y=0, width=190, height=190)
        
        ventana_principal.withdraw()
            
        ventana_consultas.mainloop()
        
    menu_label = tk.Label(ventana_principal, text="Menu", font=("Arial", 35), bg="#21A2F7", fg='black')
    menu_label.pack()
    menu_label.place(x=170, y=30, width=280, height=35)

    registrar = tk.Button(ventana_principal, text="Registros", command=registrar, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    registrar.pack()
    registrar.place(x=10, y=300, width=120, height=80)
    
    modificaciones = tk.Button(ventana_principal, text="Registro de basura", command=modificaciones, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    modificaciones.pack()
    modificaciones.place(x=430, y=300, width=150, height=80)
    
    eliminar = tk.Button(ventana_principal, text="Eliminar", command=eliminar, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    eliminar.pack()
    eliminar.place(x=150, y=300, width=120, height=80)
    
    ver_registro = tk.Button(ventana_principal, text="Consultas", command=ver_registros, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    ver_registro.pack()
    ver_registro.place(x=290, y=300, width=120, height=80)
    
    creditos = tk.Button(ventana_principal, text="Creditos", command=creditos, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    creditos.pack()
    creditos.place(x=10, y=430, width=120, height=80)
    
    contactos = tk.Button(ventana_principal, text="Contactanos", command=contactos, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    contactos.pack()
    contactos.place(x=200, y=430, width=120, height=80)
    
    salir = tk.Button(ventana_principal, text="Salir", command=ventana_principal.destroy, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    salir.pack()
    salir.place(x=390, y=430, width=120, height=80)
    
    imagen = PhotoImage(file="logo.png")
    label_imagen = Label(ventana_principal, image=imagen, bg="#21A2F7", fg="white")
    label_imagen.place(x=0, y=0, width=190, height=190)
    
    ventana_principal.mainloop()

ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio de sesión")
ventana_inicio.geometry("600x600+350+80")
ventana_inicio.config(bg="#21A2F7")


def limpiar_mensaje_incorrecto():
    if mensaje_incorrecto_inicio.winfo_exists():
        mensaje_incorrecto_inicio.config(text="")
        
mensaje_incorrecto_inicio = tk.Label(ventana_inicio, text="", fg="red", font=("Arial", 18), bg="#21A2F7")
mensaje_incorrecto_inicio.pack()
mensaje_incorrecto_inicio.place(x=60, y=350)
ventana_inicio.after(3000, limpiar_mensaje_incorrecto)

def limpiar_mensaje_campos():
    if mensaje_campos_inicio.winfo_exists():
        mensaje_campos_inicio.config(text="")
        
mensaje_campos_inicio = tk.Label(ventana_inicio, text="", fg="red", font=("Arial", 18), bg="#21A2F7")
mensaje_campos_inicio.pack()
mensaje_campos_inicio.place(x=110, y=350)
ventana_inicio.after(3000, limpiar_mensaje_campos)

iniciar_label = tk.Label(ventana_inicio, text="Iniciar sesión", font=("Arial", 35), bg="#21A2F7", fg='black')
iniciar_label.pack()
iniciar_label.place(x=200, y=30, width=280, height=35)

tuxtla_label = tk.Label(ventana_inicio, text="Tuxtla Green", font=("Arial", 35), bg="#21A2F7", fg='black')
tuxtla_label.pack()
tuxtla_label.place(x=200, y=100, width=280, height=35)

nombre_usuario_label = tk.Label(ventana_inicio, text="Nombre de usuario", font=("Arial", 22), bg="#21A2F7", fg='black')
nombre_usuario_label.pack()
nombre_usuario_label.place(x=10, y=200, width=250, height=30)

password_label = tk.Label(ventana_inicio, text="Contraseña", font=("Arial", 22), bg="#21A2F7", fg='black')
password_label.pack()
password_label.place(x=10, y=285, width=250, height=30)

nombre_usuario = tk.Entry(ventana_inicio, font=("Arial", 14))
nombre_usuario.pack()
nombre_usuario.place(x=270, y=200, width=200, height=40)

password = tk.Entry(ventana_inicio, show="*", font=("Arial", 20))
password.pack()
password.place(x=270, y=285, width=200, height=40)

iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar sesión", command=validar_ingreso, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
iniciar_sesion.pack()
iniciar_sesion.place(x=220, y=390, width=200, height=50)

Registrarme = tk.Button(ventana_inicio, text="Registrarme", command=registrar_acceso, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
Registrarme.pack()
Registrarme.place(x=220, y=460, width=200, height=50)

salir = tk.Button(ventana_inicio, text="Salir", command=ventana_inicio.destroy, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
salir.pack()
salir.place(x=220, y=530, width=200, height=50)

imagen = PhotoImage(file="logo.png")
label_imagen = Label(ventana_inicio, image=imagen, bg="#21A2F7", fg="white")
label_imagen.place(x=0, y=0, width=190, height=190)

ventana_inicio.mainloop()