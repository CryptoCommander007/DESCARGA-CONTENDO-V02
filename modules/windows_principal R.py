import tkinter as tk
import os
import requests
import re
import tkinter as tk

#**********************************************************************************#
#**********************************************************************************#
#************************************ARCHIVO FUNTIONS******************************#
#**********************************************************************************#
#**********************************************************************************#

def obtener_y_guardar_html(ruta, archivo_salida):
    print("ejecutando obtener_y_guardar_html()")
    """
    Obtiene el HTML de una URL dada y lo guarda en un archivo.
    """
    try:
        response = requests.get(ruta)
        response.raise_for_status()  # Levanta un error si la solicitud no tuvo éxito
        html = response.text
        with open(archivo_salida, 'w', encoding='utf-8') as file:
            file.write(html)
        print("HTML guardado con éxito en '{}'.".format(archivo_salida))
    except requests.exceptions.RequestException as e:
        print("Ocurrió un error al intentar acceder a la ruta '{}': {}".format(ruta, e))
    except Exception as e:
        print("Ocurrió un error al escribir en el archivo '{}': {}".format(archivo_salida, e))

def filtrar_archivo(archivo_html):
    print("filtrar_archivo()")
    """
    Filtra un archivo HTML y retorna las líneas que contienen '<a href="/videos'.
    """
    lineas_filtradas = []
    try:
        with open(archivo_html, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
        
        for linea in lineas:
            if '<a href="/videos' in linea:
                lineas_filtradas.append(linea)
        
        print("Filtrado completado. Se han encontrado {} líneas que contienen '<a href=\"/videos'.".format(len(lineas_filtradas)))
    except FileNotFoundError:
        print("El archivo '{}' no se encontró.".format(archivo_html))
    except Exception as e:
        print("Ocurrió un error:", e)
    
    return lineas_filtradas

def limpiar_href(archivo_html):
    """
    Extrae las rutas de las etiquetas href de un archivo HTML filtrado y las retorna.
    """
    href_matches = []
    try:
        with open(archivo_html, 'r', encoding='utf-8') as file:
            contenido = file.read()

        # Busca todas las coincidencias de la expresión regular para href="/..."
        href_matches = re.findall(r'href="(/[^"]+)"', contenido)

        print("Extracción completada. Se han encontrado {} rutas.".format(len(href_matches)))
    except FileNotFoundError:
        print("El archivo '{}' no se encontró.".format(archivo_html))
    except Exception as e:
        print("Ocurrió un error:", e)
    
    return href_matches

def limpiar_y_guardar(archivo_entrada):
    """
    Lee un archivo de texto línea por línea, elimina todo lo que sigue al carácter '?' en cada línea (incluido el carácter),
    elimina todos los espacios en blanco de las líneas resultantes, y retorna las líneas modificadas como una lista.
    """
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file:
            lineas = file.readlines()

        lineas_modificadas = []
        for linea in lineas:
            # Encuentra el índice del carácter '?'
            indice_pregunta = linea.find('?')
            if indice_pregunta != -1:
                # Elimina todo lo que sigue al carácter '?', incluido el mismo
                linea = linea[:indice_pregunta]
            # Elimina todos los espacios en blanco de la línea
            linea = linea.replace(" ", "").replace("\t", "")
            lineas_modificadas.append(linea)

        return lineas_modificadas

    except FileNotFoundError:
        print("El archivo '{}' no se encontró.".format(archivo_entrada))
    except Exception as e:
        print("Ocurrió un error:", e)

def cargar_rutas(archivo):
    if os.path.exists(archivo):
        with open(archivo, 'r') as file:
            return file.readlines()
    else:
        return []

def mostrar_mensaje(mensaje):
    popup = tk.Toplevel()
    popup.geometry("200x100")
    popup.title("Mensaje")
    label = tk.Label(popup, text=mensaje)
    label.pack(pady=20)
    popup.mainloop()

def eliminar_lineas_duplicadas(archivo):
    """
    Elimina las líneas duplicadas y las líneas vacías de un archivo y guarda las líneas únicas en el mismo archivo.
    """
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
        
        # Eliminar líneas vacías y duplicadas
        lineas_unicas = list(set(linea for linea in lineas if linea.strip()))
        
        with open(archivo, 'w', encoding='utf-8') as file:
            file.writelines(lineas_unicas)
        
        print("Líneas duplicadas y vacías eliminadas. Archivo guardado como '{}'.".format(archivo))
    except FileNotFoundError:
        print("El archivo '{}' no se encontró.".format(archivo))
    except Exception as e:
        print("Ocurrió un error:", e)


def listar_rutas():
    archivo = 'modules/rutas.txt'
    url = url_entry.get()
    if url:
        with open(archivo, 'a+') as file:
            file.write(url + '\n')
        print("Ruta creada: " + url)  # Mensaje de ruta creada
        url_entry.delete(0, tk.END)
        mostrar_mensaje("Ruta agregada")  # Mostrar ventana emergente con el mensaje
        
        # Obtener y guardar HTML
        obtener_y_guardar_html(url, 'archivo_html.html')
        
        # Filtrar archivo HTML y guardar las líneas filtradas temporalmente
        lineas_filtradas = filtrar_archivo('archivo_html.html')
        with open('salida_filtrada_a_href_videos.html', 'w', encoding='utf-8') as file:
            file.writelines(lineas_filtradas)
        
        # Limpiar href del archivo filtrado
        hrefs = limpiar_href('salida_filtrada_a_href_videos.html')
        
        # Guardar los hrefs en un archivo temporal para limpiar y guardar
        with open('href_salida.txt', 'w', encoding='utf-8') as file:
            for href in hrefs:
                file.write(href + '\n')
        
        # Limpiar y guardar las rutas finales
        lineas_limpias = limpiar_y_guardar('href_salida.txt')
        with open('rutas_finales.txt', 'w', encoding='utf-8') as file:
            for linea in lineas_limpias:
                file.write(linea + '\n')
        
        # Eliminar líneas duplicadas en el archivo final
        eliminar_lineas_duplicadas('rutas_finales.txt')

        print("Proceso completado. Las rutas finales se han guardado en 'rutas_finales.txt'.")
    else:
        print("Por favor ingrese una URL.")

    rutas = cargar_rutas(archivo)
    for ruta in rutas:
        print(ruta.strip())

def descargar_archivo():
    # Aquí irá la lógica para descargar el archivo desde la URL
    pass

def main():
    root = tk.Tk()
    root.title("Mi Proyecto Tkinter")
    root.geometry("1200x800")
    # Evitar que la ventana se agrande
    root.resizable(width=False, height=False)

    # Establecer color de fondo para la ventana
    root.configure(bg="#f0f0f0")  # Gris claro

    # Campo de entrada para la URL
    global url_entry
    url_entry = tk.Entry(root, width=80, bg="#AAA100", bd=2, relief=tk.GROOVE, font=("Arial", 12))  # Ajusta el ancho, alto, color de fondo, borde, relieve y fuente del campo de entrada
    url_entry.grid(row=0, column=0, pady=10, padx=20)
    # Botón para listar
    listar_btn = tk.Button(root, text="Listar", command=listar_rutas, width=80, height=2)  # Ajusta el ancho y largo del botón
    listar_btn.grid(row=1, column=0, pady=10 , padx=120)

    # Botón para descargar
    descargar_btn = tk.Button(root, text="Descargar", width=80, height=2)  # Ajusta el ancho y largo del botón
    descargar_btn.grid(row=2, column=0, pady=10, padx=120)

    root.mainloop()

if __name__ == "__main__":
    main()
