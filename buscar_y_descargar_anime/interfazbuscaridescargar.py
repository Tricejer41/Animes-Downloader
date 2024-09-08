import tkinter as tk
from tkinter import scrolledtext, Listbox, messagebox
import threading
from buscar_y_descargar_anime.buscardescargar import buscar_anime, descargar_anime

# Colores personalizados
COLOR_FONDO = "#2e2e2e"  # Negro claro
COLOR_TEXTO = "#ffffff"  # Blanco para el texto
COLOR_TEXTO_MAGENTA = "#ff00ff"  # Magenta para los títulos
COLOR_BOTON = "#404040"  # Gris oscuro para los botones
COLOR_BOTON_TEXTO = "#ffffff"  # Texto de los botones en blanco
COLOR_ENTRADA = "#303030"  # Fondo para las entradas de texto

# Fuente personalizada
FUENTE_TEXTO = ("Arial", 12)
FUENTE_BOTON = ("Arial", 10, "bold")

# Función para crear la interfaz de Buscar y Descargar
def crear_interfaz_buscar_descargar(ventana):
    # Limpiar la ventana
    for widget in ventana.winfo_children():
        widget.destroy()

    # Configurar el fondo negro claro de la ventana
    ventana.configure(bg=COLOR_FONDO)
    ventana.geometry("600x600")  # Ajustamos el tamaño de la ventana

    ventana.title("Gestor de Animes - Buscar y Descargar")

    # Botón para regresar al menú principal
    boton_volver = tk.Button(ventana, text="Volver al Menú Principal", command=lambda: volver_menu_principal(ventana),
                             bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, font=FUENTE_BOTON)
    boton_volver.pack(pady=10)

    # Etiqueta para el nombre del anime
    etiqueta_busqueda = tk.Label(ventana, text="Nombre del Anime:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TEXTO)
    etiqueta_busqueda.pack(pady=10)

    entrada_busqueda = tk.Entry(ventana, width=50, bg=COLOR_ENTRADA, fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO, font=FUENTE_TEXTO)
    entrada_busqueda.pack(pady=5)

    # Listbox para mostrar los resultados de la búsqueda
    lista_resultados = Listbox(ventana, height=6, width=50, selectmode=tk.SINGLE, 
                               bg=COLOR_ENTRADA, fg=COLOR_TEXTO, font=FUENTE_TEXTO)
    lista_resultados.pack(pady=5)

    # Área de sinopsis del anime seleccionado
    descripcion_anime = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=50, height=10, 
                                                  bg=COLOR_ENTRADA, fg=COLOR_TEXTO, font=FUENTE_TEXTO)
    descripcion_anime.pack(pady=5)
    descripcion_anime.config(state=tk.DISABLED)

    # Lista de enlaces completa
    lista_enlaces = []

    def manejar_busqueda():
        anime = entrada_busqueda.get()
        if anime:
            # Limpiar la lista de resultados anteriores
            lista_resultados.delete(0, tk.END)
            lista_enlaces.clear()  # Limpiamos la lista de descripciones

            # Llamar a la función de buscar en un hilo separado
            threading.Thread(target=buscar_anime, args=(anime, lista_resultados, descripcion_anime, lista_enlaces)).start()

    def mostrar_sinopsis():
        # Mostramos la descripción completa del anime seleccionado
        seleccion = lista_resultados.curselection()
        if seleccion:
            index = seleccion[0]
            descripcion_anime.config(state=tk.NORMAL)
            descripcion_anime.delete(1.0, tk.END)
            descripcion_anime.insert(tk.END, lista_enlaces[index])  # Mostrar la descripción completa (sinopsis)
            descripcion_anime.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Error", "Por favor selecciona un anime de la lista para ver la sinopsis.")

    def manejar_siguiente():
        # Aquí iría el código para la futura interfaz de descarga del anime seleccionado
        seleccion = lista_resultados.curselection()
        if seleccion:
            anime_seleccionado = lista_resultados.get(seleccion[0])
            print(f"Ir a la interfaz de descarga para: {anime_seleccionado}")
            # Aquí puedes implementar la lógica para llevar a la interfaz de descarga
            # donde se podrán seleccionar temporadas, idiomas, etc.
        else:
            messagebox.showerror("Error", "Por favor selecciona un anime de la lista para continuar.")

    # Frame para los botones
    frame_botones = tk.Frame(ventana, bg=COLOR_FONDO)
    frame_botones.pack(pady=10)

    # Botón para buscar animes
    boton_buscar = tk.Button(frame_botones, text="Buscar", command=manejar_busqueda, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, font=FUENTE_BOTON)
    boton_buscar.grid(row=0, column=0, padx=10)

    # Botón para ver la sinopsis del anime seleccionado
    boton_ver_descripcion = tk.Button(frame_botones, text="Ver Sinopsis", command=mostrar_sinopsis, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, font=FUENTE_BOTON)
    boton_ver_descripcion.grid(row=0, column=1, padx=10)

    # Botón para ir a la interfaz de descarga
    boton_siguiente = tk.Button(frame_botones, text="Siguiente", command=manejar_siguiente, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, font=FUENTE_BOTON)
    boton_siguiente.grid(row=0, column=2, padx=10)

# Función para volver al menú principal
def volver_menu_principal(ventana):
    from gestor_animes import crear_menu_principal
    crear_menu_principal(ventana)
