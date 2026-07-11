def mostrar_menu():
    print("========== MENU PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            op = int(input("Ingrese una opcion: "))
            if 7 > op and op > 0:
                return op
            else:
                print("Debe ingresar valores enteros")
        except ValueError:
            print("Debe ingresar un numero entero")
def buscar_codigo(productos, codigo):
    if codigo.upper() not in productos:
        return False
    else:
        return True
def validar_codigo(codigo):
    if codigo.strip() != "":
        return True
    else:
        return False
def validar_categoria(categoria):
    if categoria.strip() != "":
        return True
    else:
        return False
def validar_nombre(nombre):
    if nombre.strip() != "":
        return True
    else:
        return False
def validar_marca(marca):
    if marca.strip() != "":
        return True
    else:
        return False
def validar_peso(peso_kg):
    if peso_kg>0:
        return True
    else:
        return False
def validar_importado(es_importado):
    if es_importado.lower()=="s" or es_importado.lower()=="n":
        return True
    else:
        return False
def validar_cachorro(es_para_cachorro):
    if es_para_cachorro.lower()=="s" or es_para_cachorro.lower()=="n":
        return True
    else:
        return False
def validar_precio(precio):
    if precio>0:
        return True
    else:
        return False
def validar_unidades(unidades):
    if unidades>=0:
        return True
    else:
        return False
def agregar_producto(productos,codigo,nombre,categoria,marca,peso_kg,es_importado,es_para_cachorro):
    if buscar_codigo(productos,codigo)==True:
        return False
    else:
        if es_importado.lower()=="s":
            es_importado=True
        else:
            es_importado=False
        if es_para_cachorro.lower()=="s":
            es_para_cachorro=True
        else:
            es_para_cachorro=False
        productos[codigo.upper()]=[
                nombre,
                categoria.lower(),
                marca,
                peso_kg,
                es_importado,
                es_para_cachorro
            ]
        return True

def agregar_stock(stock,codigo,precio,unidades):
    if buscar_codigo(stock,codigo)==True:
        return False
    else:
        stock[codigo.upper()]=[
                precio,
                unidades
            ]
        return True

def agregar_productos(productos,stock,codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
    if agregar_producto(productos,codigo,nombre,categoria,marca,peso_kg,es_importado,es_para_cachorro) and agregar_stock(stock,codigo,precio,unidades):
        return True
    else:
        return False
def unidades_categoria(productos,stock,categoria):
    unidad=0
    aparecio=False
    for i in productos:
        if productos[i][1]==categoria.lower():
            if i in stock:
                unidad+=stock[i][1]
                aparecio=True
    if not aparecio:
        print("No existe ningun producto con esa categoria")
    else:
        print(f"El total de unidades disponibles es: {unidad}")

def busqueda_precio(stock,productos,p_min,p_max):
    productos_busqueda=[]
    for i in stock:
        if (stock[i][0]>=p_min and stock[i][0]<=p_max) and stock[i][1]>0:
            productos_busqueda.append(f"{productos[i][0]}--{i}")
    if len(productos_busqueda)>0:
        productos_busqueda.sort()
        print(f"Los productos encontrados dentro del rango de precio, {p_min} y {p_max} son: {productos_busqueda}")
    else:
        print("No hay productos en ese rango de precios.")
    

def actualizar_precio(stock,codigo,precio):
    if buscar_codigo(stock,codigo)==False:
        return False
    else:
        stock[codigo.upper()][0]=precio
        return True


def eliminar_producto(codigo,stock,productos):
    if buscar_codigo(productos,codigo)==True:
        stock.pop(codigo.upper())
        productos.pop(codigo.upper())
        return True
    else:
        return False



def main():

    productos = {}
    stock={}
    while True:

        mostrar_menu()
        op = leer_opcion()

        if op == 1:

            categoria=input("¿Que categoria desea buscar? ")
            if validar_categoria(categoria):
                unidades_categoria(productos,stock,categoria)
            else:
                print("La categoria es invalida")

        elif op == 2:
            while True:
                try:
                    p_max=int(input("Ingrese precio maximo de busqueda"))
                    if p_max>0:
                        break
                    print("Debe ingresar valores enteros")
                except ValueError:
                    print("Debe ingresar valores enteros")
            while True:    
                try:
                    p_min=int(input("Ingrese precio minnimo de busqueda"))
                    if p_min>0 and p_max>p_min:
                        break
                    print("Debe ingresar valores enteros")
                except ValueError:
                    print("Debe ingresar valores enteros")            
            busqueda_precio(stock,productos,p_min,p_max)

        elif op == 3:
            seguir="s"
            while True:
                if seguir.lower()=="n":
                    break
                else:
                    codigo=input("Ingrese codigo del producto a buscar")
                    if validar_codigo(codigo):
                        while True:
                            try:
                                precio=int(input("Ingrese nuevo precio del producto"))
                                break
                            except ValueError:
                                print("Debe ingresar valores enteros")
                        if validar_precio(precio):
                            if actualizar_precio(stock,codigo,precio):
                                print("Precio actualizado")
                            else:
                                print("El código no existe")
                        else:
                            print("El precio es invalido")
                    else:
                        print("El codigo no existe")
                    seguir=input("¿Desea actualizar otro precio (s/n)?: ")

        elif op == 4:
            codigo = input("Ingrese código del producto: ")

            if not validar_codigo(codigo):
                print("Codigo invalido")
            else:
                nombre = input("Ingrese nombre: ")

                if not validar_nombre(nombre):
                    print("Nombre invalido")
                else:
                    categoria = input("Ingrese categoría: ")

                    if not validar_categoria(categoria):
                        print("Categoria invalida")
                    else:
                        marca = input("Ingrese marca: ")

                        if not validar_marca(marca):
                            print("Marca invalida")
                        else:
                            while True:
                                try:
                                    peso_kg = float(input("Ingrese peso (kg): "))                                
                                    break
                                except ValueError:
                                    print("Debe ingresar valores enteros")

                            if not validar_peso(peso_kg):
                                print("Peso invalido")
                            else:
                                es_importado = input("¿Es importado? (s/n): ")

                                if not validar_importado(es_importado):
                                    print("Respuesta invalida")
                                else:
    
                                    es_para_cachorro = input("¿Es para cachorro? (s/n): ")
    
                                    if not validar_cachorro(es_para_cachorro):
                                        print("Respuesta invalida")

                                    else:
                                        while True:
                                            try:
                                                precio = int(input("Ingrese precio: "))
                                                break
                                            except ValueError:
                                                print("Debe ingresar valores enteros")                                            
                                            

                                        if not validar_precio(precio):
                                            print("Precio invalido")
                                        else:
                                            while True:
                                                try:
                                                    unidades = int(input("Ingrese unidades: "))
                                                    break
                                                except ValueError:
                                                    print("Debe ingresar valores enteros")  

                                            if not validar_unidades(unidades):
                                                print("Unidades invalidas")
                                            else:
                                                if not agregar_productos(productos,stock,codigo,nombre,categoria,marca,peso_kg,es_importado,es_para_cachorro,precio,unidades):
                                                    print("El codigo no existe")
                                                else:
                                                    print("Producto agregado")
        elif op == 5:
            codigo=input("Ingresa el codigo del producto que desea eliminar: ")
            if eliminar_producto(codigo,stock,productos):
                print("Producto eliminado")
            else:
                print("El código no existe")

        elif op == 6:

            print("Programa finalizado.")
            break


main()