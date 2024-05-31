def filtrar_archivo(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
        
        # Eliminar líneas vacías y mantener el formato
        lineas_filtradas = [linea for linea in lineas if linea.strip()]
        
        with open(archivo_salida, 'w', encoding='utf-8') as file:
            file.writelines(lineas_filtradas)
        
        print("Líneas vacías eliminadas. Archivo guardado como '{}'.".format(archivo_salida))
    except FileNotFoundError:
        print("El archivo '{}' no se encontró.".format(archivo_entrada))
    except Exception as e:
        print("Ocurrió un error:", e)

def eliminar_lineas_duplicadas(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
        
        # Eliminar líneas duplicadas y mantener el formato
        lineas_unicas = list(set(linea.strip() for linea in lineas if linea.strip()))
        
        with open(archivo_salida, 'w', encoding='utf-8') as file:
            file.writelines(linea + '\n' for linea in lineas_unicas)
        
        print("Líneas duplicadas eliminadas. Archivo guardado como '{}'.".format(archivo_salida))
    except FileNotFoundError:
        print("El archivo '{}' no se encontró.".format(archivo_entrada))
    except Exception as e:
        print("Ocurrió un error:", e)

# Filtrar archivo para eliminar líneas vacías
filtrar_archivo('rutas_completas.txt', 'rutas_completas_filtro1.txt')

# Eliminar líneas duplicadas del archivo filtrado
eliminar_lineas_duplicadas('rutas_completas_filtro1.txt', 'rutas_completas_filtro2.txt')
