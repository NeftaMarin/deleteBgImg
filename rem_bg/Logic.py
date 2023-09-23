from rembg import remove
from PIL import Image
from tkinter import messagebox as mb


# función para eliminar el fondo de la imagen
def rem_bg(input_path, output_path):
    # Aqui se llama a la funcion remove de la libreria rembg
    with open(input_path, "rb") as i:
        with open(output_path, "wb") as o:
            input_ = i.read()
            output = remove(input_)
            o.write(output)
            mb.showinfo("Éxito!", "El fondo de la imagen se eliminó correctamente.")
            openFile = Image.open(output_path)
            openFile.show()
