import tkinter as tk
from buscar_y_descargar_anime.interfazbuscaridescargar import crear_interfaz_buscar_descargar

# Colores personalizados
COLOR_FONDO = "#2e2e2e"  # Negro claro
COLOR_TEXTO = "#ff00ff"  # Magenta
COLOR_BOTON = "#404040"  # Gris oscuro para los botones
COLOR_BOTON_TEXTO = "#ffffff"  # Texto de los botones en blanco

# Fuente personalizada
FUENTE_TEXTO = ("Arial", 12)
FUENTE_BOTON = ("Arial", 10, "bold")

# Función para crear el menú principal
def crear_menu_principal(ventana):
    # Limpiar la ventana
    for widget in ventana.winfo_children():
        widget.destroy()

    # Configurar el fondo negro claro de la ventana
    ventana.configure(bg=COLOR_FONDO)

    ventana.title("Gestor de Animes - Menú Principal")

    # Etiqueta principal
    etiqueta_menu = tk.Label(ventana, text="Menú Principal", font=("Arial", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO)
    etiqueta_menu.pack(pady=20)

    # Botón Buscar y Descargar
    boton_buscar_descargar = tk.Button(ventana, text="Buscar y Descargar", width=25, command=lambda: crear_interfaz_buscar_descargar(ventana),
                                       bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, font=FUENTE_BOTON)
    boton_buscar_descargar.pack(pady=10)

    # Botón Renombrar (sin función por ahora)
    boton_renombrar = tk.Button(ventana, text="Renombrar", width=25,
                                bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, font=FUENTE_BOTON)
    boton_renombrar.pack(pady=10)

    # Botón Upload Servidor (sin función por ahora)
    boton_upload = tk.Button(ventana, text="Upload Servidor", width=25,
                             bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, font=FUENTE_BOTON)
    boton_upload.pack(pady=10)

# Función para inicializar la ventana principal
def main():
    ventana = tk.Tk()
    ventana.geometry("500x500")
    crear_menu_principal(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()
