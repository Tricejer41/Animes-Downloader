import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import config

# Configuración de Telethon
api_id = config.API_ID
api_hash = config.API_HASH
phone = config.PHONE_NUMBER
channel_name = config.CHANNEL_NAME

# Crear cliente de Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def buscar_anime_telegram(anime, lista_resultados, resultado_widget, lista_enlaces):
    try:
        print("Iniciando sesión en Telegram...")
        await client.start(phone)
        print("Sesión iniciada.")

        if not await client.is_user_authorized():
            print("Autorizando usuario...")
            try:
                await client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Por favor ingresa tu contraseña de 2FA: ')
                await client.sign_in(password=password)
        
        # Obtener la entidad del canal
        print(f"Obteniendo el canal: {channel_name}...")
        channel = await client.get_entity(channel_name)
        print(f"Conectado al canal: {channel.title}")
        resultado_widget.insert('end', f"Buscando '{anime}' en los mensajes del canal '{channel.title}'...\n")
        
        # Lista para guardar los mensajes encontrados
        contador_resultados = 0

        # Usar la búsqueda nativa de Telegram con el término ingresado (similar a la lupa en Telegram)
        print(f"Buscando mensajes que coincidan con '{anime}'...")
        async for message in client.iter_messages(channel, search=anime, limit=5):
            if message.message:
                # Extraer solo el título y el año de lanzamiento
                linea_titulo = None
                for line in message.message.splitlines():
                    if line.startswith("🍿 Título :"):
                        linea_titulo = line
                        break

                if linea_titulo:
                    # Extraemos solo el nombre del anime y el año
                    titulo_y_ano = linea_titulo.replace("🍿 Título :", "").strip().split("(")
                    nombre_anime = titulo_y_ano[0].strip()
                    ano_anime = titulo_y_ano[1].replace(")", "").strip() if len(titulo_y_ano) > 1 else ""

                    titulo_final = f"{nombre_anime} ({ano_anime})"
                    
                    # Añadimos el título a la lista de resultados
                    resultado_widget.insert('end', f"Título encontrado: {titulo_final}\n")
                    lista_resultados.insert('end', titulo_final)  # Mostrar una vista previa en la lista
                    
                    # Buscar la sinopsis
                    sinopsis = None
                    for line in message.message.splitlines():
                        if "Sinopsis" in line:  # Hacemos la búsqueda más flexible
                            sinopsis = line.replace("📝 Sinopsis :", "").strip()
                            break
                    lista_enlaces.append(sinopsis if sinopsis else "Sin sinopsis disponible.")
                    contador_resultados += 1

        # Verificar si se encontraron resultados
        if contador_resultados == 0:
            resultado_widget.insert('end', "No se encontraron resultados para la búsqueda.\n")
        else:
            resultado_widget.insert('end', "Búsqueda completada.\n")
    
    except Exception as e:
        print(f"Error durante la búsqueda: {e}")
        resultado_widget.insert('end', f"Error durante la búsqueda: {e}\n")

def buscar_anime(anime, lista_resultados, resultado_widget, lista_enlaces):
    asyncio.run(buscar_anime_telegram(anime, lista_resultados, resultado_widget, lista_enlaces))

def descargar_anime(anime_seleccionado, resultado_widget):
    print(f"Iniciando la descarga del anime seleccionado: {anime_seleccionado}")
    resultado_widget.insert('end', f"Iniciando la descarga de '{anime_seleccionado}'...\n")
    
    # Simulación de descarga (esto debería cambiarse para manejar la descarga real)
    resultado_widget.insert('end', "Descarga completada.\n")
    print("Descarga completada.")
