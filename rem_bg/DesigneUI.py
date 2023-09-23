import tkinter as tk
from tkinter import filedialog
import Logic as logic
from tkinter import messagebox as mb

# Crear la ventana
window = tk.Tk()
window.title("Remove Background")
window.eval('tk::PlaceWindow . center')
window.config(bg="#000000")
window.geometry("620x200")
window.iconbitmap("./src/paintIco.ico")

# rutas de iconos
photo = tk.PhotoImage(file="./src/photo.png")
file = tk.PhotoImage(file="./src/file.png")
rem = tk.PhotoImage(file="./src/paint.png")


# función para abrir la imagen
def open_file():
    # Mostrar la ventana de dialogo para seleccionar el archivo
    file_path = filedialog.askopenfilename()

    if file_path:
        input_path.delete(0, tk.END)
        input_path.insert(0, file_path)
    else:
        input_path.delete(0, tk.END)


# Mostrar la ventana de dialogo para seleccionar la ruta de guardado
def open_path():
    path_output = filedialog.askdirectory()

    if output_path:
        print("la carpeta seleccionada es: ", path_output)
        output_path.delete(0, tk.END)
        ruta_select = output_path
        output_path.insert(0, path_output)
    else:
        output_path.delete(0, tk.END)


# función para eliminar el fondo de la imagen
def remove_bg():
    input_ = input_path.get()
    output = f"{output_path.get()}/{name_img.get()}.png"
    logic.rem_bg(input_, output)
    clean_inputs()


# Método para limpiar los inputs
def clean_inputs():
    input_path.delete(0, tk.END)
    output_path.delete(0, tk.END)
    name_img.delete(0, tk.END)


# Etiquetas de la ventana
lbl_input = tk.Label(window, text="Elige imagen: ")
lbl_input.config(font=("Arial", 10), bg="#000000", foreground="#ffffff", anchor="w")
lbl_input.grid(row=1, column=0)

lbl_save = tk.Label(window, text="Guardar Imagen: ")
lbl_save.config(font=("Arial", 10), bg="#000000", foreground="#ffffff", anchor="w")
lbl_save.grid(row=2, column=0)

lbl_name = tk.Label(window, text="Asignar nombre: ")
lbl_name.config(font=("Arial", 10), bg="#000000", foreground="#ffffff", anchor="w")
lbl_name.grid(row=3, column=0)

# Espacios
space_zero = tk.Label(window, text=" ")
space_zero.config(font=("Arial", 10), bg="#000000", foreground="#ffffff", anchor="w")
space_zero.grid(row=0, column=0, columnspan=4)

space_uno = tk.Label(window, text=" ")
space_uno.config(font=("Arial", 10), bg="#000000", foreground="#ffffff", anchor="w")
space_uno.grid(row=1, column=2)

space_dos = tk.Label(window, text=" ")
space_dos.config(font=("Arial", 10), bg="#000000", foreground="#ffffff", anchor="w")
space_dos.grid(row=2, column=2)

space_tres = tk.Label(window, text=" ")
space_tres.config(font=("Arial", 10), bg="#000000", foreground="#ffffff", anchor="w")
space_tres.grid(row=3, column=2)

space_cuatro = tk.Label(window, text=" ")
space_cuatro.config(font=("Arial", 10), bg="#000000", foreground="#ffffff", anchor="w")
space_cuatro.grid(row=4, column=0, columnspan=4)

# inputs de la ventana
input_path = tk.Entry(window, width=35)
input_path.config(font=("Consolas", 12), bg="#000000", foreground="#9c9c9c", width=50, insertbackground="#ffffff")
input_path.grid(row=1, column=1)

output_path = tk.Entry(window, width=35)
output_path.config(font=("Consolas", 12), bg="#000000", foreground="#9c9c9c", width=50, insertbackground="#ffffff")
output_path.grid(row=2, column=1)

name_img = tk.Entry(window, width=35)
name_img.config(font=("Consolas", 12), bg="#000000", foreground="#9c9c9c", width=50, insertbackground="#ffffff")
name_img.grid(row=3, column=1)

# botones de la ventana
btn_open = tk.Button(window, text=" ", command=open_file, image=photo, anchor="e")
btn_open.config(font=("Arial", 10), bg="#000000", foreground="#ffffff", borderwidth=0)
btn_open.grid(row=1, column=3)

btn_save = tk.Button(window, text=" ", command=open_path, image=file, anchor="e")
btn_save.config(font=("Arial", 10), bg="#000000", foreground="#ffffff", borderwidth=0)
btn_save.grid(row=2, column=3)

btn_remBg = tk.Button(window, text="Eliminar Fondo", command=remove_bg, image=rem, compound="right")
btn_remBg.config(font=("Arial", 10), bg="#000000", foreground="#ffffff")
btn_remBg.grid(row=5, column=1, columnspan=2)

window.mainloop()
