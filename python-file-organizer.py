import os
import shutil

# 1. Configura la ruta de la carpeta que quieres limpiar (ejemplo: Descargas)
ruta_origen = 'C:\\Users\\Lenovo T470\\Downloads' #Aqui poner la ruta de la carpeta que quieres limpiar

# 2. Diccionario para organizar por categorías
extensiones = {
    '.jpg': 'Imagenes',
    '.png': 'Imagenes',
    '.pdf': 'Documentos',
    '.docx': 'Documentos',
    '.txt': 'Documentos',
    '.zip': 'Comprimidos'
}

def organizar():
    # Listar todos los archivos en la carpeta
    for archivo in os.listdir(ruta_origen):
        nombre, extension = os.path.splitext(archivo)
        
        # Si la extensión está en nuestro diccionario
        if extension in extensiones:
            carpeta_destino = os.path.join(ruta_origen, extensiones[extension])
            
            # Crear la carpeta si no existe
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
            
            # Mover el archivo
            shutil.move(os.path.join(ruta_origen, archivo), 
                        os.path.join(carpeta_destino, archivo))
            print(f"Movido: {archivo} -> {extensiones[extension]}")

            

if __name__ == "__main__":
    organizar()

    
