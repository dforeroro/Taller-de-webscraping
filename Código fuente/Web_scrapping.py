def leer_libros():
    
    """

    Esta función lee los libros y crea listas segun las categorias, ademas de clasificar los datos individuales de los textos
    :return: Lista categorias

    """
    
    from io import open
    prueba_imagenes=[]    

    libros=["prueba_imagenes.txt"]
    categorias=[prueba_imagenes]

    for i in range(len(libros)):
        archivo=open(libros[i],"r",encoding="utf-8") 
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            campos = linea.split(";")
            libro = {"codigo":campos[0], "autor":campos[1], "fecha":campos[2], "titulo":campos[3], "lugar":campos[4], "editorial":campos[5], "cantidad":campos[6], "cita":campos[7], "link_img":campos[8]}
            categorias[i].append(libro)

    return categorias

def busqueda_link_libro(busqueda):
    
    """

    Esta función busca el link del libro solicitado en la lista de diccionarios de los libros para después llamar a la función 'extrae_link' y así extraer el link de la imagen de su caratula.
    :return: link (l_imagen), diccionario biblioteca.

    """
    
    link_libro = ''
    biblioteca=leer_libros()
    for elemento in biblioteca:
        for l in elemento:
            if l["titulo"] == busqueda:
                link_libro=l["link_img"]
                codigo=l["codigo"]
    if link_libro == '':
        link_libro = 'http://libgen.rs/book/index.php?md5=B1F3ECA175474231AC9C2B13CF4E232C'

    l_imagen = extraer_link(link_libro)
    
    return l_imagen, codigo, biblioteca

def extraer_link(link_libro_1):
        
    """

    Esta función extrae el link de la imagen de la caratula del libro solicitado desde el link de la información del mismo.
    :return: Lista categorias

    """
    
    from bs4 import BeautifulSoup
    from urllib.request import urlopen

    url = link_libro_1
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    imagenes = soup.find_all("img")
    imagen = imagenes[0]["src"]
    link_imagenes="http://library.lol" + imagen
    
    return link_imagenes
    
def descarga_imagen(link_imagen, busqueda):
        
    """

    Esta función descarga la imagen teniendo en cuanta el link de la caratula.
    :return: None

    """
    
    import requests
    url = link_imagen
    nombre_local_imagen = busqueda + ".jpg"
    imagen = requests.get(url).content
    with open(nombre_local_imagen, 'wb') as handler:
        foto = handler.write(imagen)                  
    
    return                      

def main():
    busqueda=input('Ingrese titulo: ')
    link_de_la_imagen, numero, biblioteca = busqueda_link_libro(busqueda)
    portada = descarga_imagen(link_de_la_imagen, busqueda)

main()
