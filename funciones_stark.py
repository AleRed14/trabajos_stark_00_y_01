#*****************************************************************************

# Imprimir

def mostrar_nombre_heroe(heroe:dict) -> None:
    if len(heroe) == 0:
        raise ValueError("Dict is empty")
    print(f"Nombre: {heroe['nombre']}")

def mostrar_nombres_heroes(lista:list) -> None:
    if len(lista) == 0:
        raise ValueError("List is empty")
    for heroe in lista:
        mostrar_nombre_heroe(heroe)

def mostrar_nombre_altura_heroe(heroe:dict)->None:
    if len(heroe) == 0:
        raise ValueError("Dict is empty")
    print(f"{heroe["nombre"]:^20}| {heroe["altura"]:^6.6}")

def mostrar_nombre_altura_heroes(lista:list)->None:
    if len(lista) == 0:
        raise ValueError("List is empty")
    print("      Nombre        | Altura")
    print("----------------------------------")
    for heroe in lista:
        mostrar_nombre_altura_heroe(heroe)

def mostrar_heroe_solo(heroe:dict)->None:
    for key in heroe:
        print(f"{key.capitalize()}: {heroe[key]}")

def limpiar_pantalla()->None:
    """Limpia la pantalla
    """
    import os #Viene de sistema operativo
    os.system("cls") # Se encarga de limpiar la pantalla de todo lo de atras

def pausar()->None:
    """Pausa el programa para leerlo
    """
    import os #Viene de sistema operativo
    os.system("pause") # Pausa el programa hasta que se toque alguna tecla, 
                       #sirve para que no se borre insantaneamente lo mostrado

def mostrar_personajes_x_dato(lista:list,llave:str)->None:
    """Muestra el nombre del heroe segun el dato target que le pasemos

    Args:
        lista (list): lista con los heroes
        llave (str): llave a buscar
    """
    lista_datos = mapear_lista(lambda her: her[llave],lista)
    lista_datos = set(lista_datos)
    lista_datos = list(lista_datos)
    ordenar_lista(lambda dat_ant, dat_act: dat_ant > dat_act,lista_datos)
    for dato in lista_datos:
        if dato == "":
            print(f"No tiene:")
        else:           
            print(f"{dato}:")
        
        for e in lista:
            if e[llave] == dato:
                print(f"    {e["nombre"]}")

def mostrar_cantidad_elementos_de_un_dato (lista:list,llave:str)->None:
    """Muestra la cantidad de elementos que tienen un mismo valor de una llave

    Args:
        lista (list): lista con diccionarios
        llave (str): llave a buscar
    """
    lista_datos = mapear_lista(lambda her: her[llave],lista)
    lista_datos = set(lista_datos)
    lista_datos = list(lista_datos)
    ordenar_lista(lambda dat_ant, dat_act: dat_ant > dat_act,lista_datos)
    lista_contador = []
    for dato in lista_datos:
        lista_contador.append(0)
        for e in lista:
            if e[llave] == dato:
                lista_contador[-1] += 1
    for i in range(len(lista_datos)):
        if lista_datos[i] == "":
            lista_datos[i] = "No tiene"
        print(f"La cantidad de {lista_datos[i]} es: {lista_contador[i]}")

#*****************************************************************************

# Ecuaciones

def reduce_lista(funcion, lista:list):
    ant = lista[0]
    for i in range(1,len(lista)):
        ant = funcion(ant,lista[i])
    return ant

def promedio(dividendo, divisor)->float:
    return dividendo / divisor

def acumular_datos(lista:list,key:str):
    acumulador = 0
    tam = len(lista)
    for i in range(tam - 1):
        numero = lista[i][key]
        if validar_entero(numero):
            acumulador += int(numero)
        elif validar_flotante(numero):
            acumulador += float(numero)
        else:
            raise TypeError(f"{numero} no es ni un entero ni un flotante.")
    return acumulador



def promedio_dict(lista:list, key:str):
    acumulador = acumular_datos(lista,key)
    return acumulador / len(lista)


#*****************************************************************************

# Validaciones

def validar_entero(numero_a_probar:str) -> bool:
    """Valida que el numero sea un entero

    Args:
        numero_a_probar (str): cadena a validar

    Returns:
        bool: True si el texto es un entero, false en caso contrario
    """
    return numero_a_probar.isalnum()

def validar_flotante(numero_a_probar:str) -> bool:
    """Valida que el numero sea un flotante

    Args:
        numero_a_probar (str): cadena a validar

    Returns:
        bool: True si el texto es un flotante, false en caso contrario
    """
    try:
        float(numero_a_probar)
        retorno = True
    except ValueError:
        retorno = False
    return retorno

def validar_mayor_menor_a_eleccion(valor_1,valor_2,max=True)->bool:
    retorno = False
    if (max and valor_1 > valor_2 or
       (not max and valor_1 < valor_2)):
        retorno = True
    return retorno  

#*****************************************************************************

# Pedir datos

def menu_con_lista(lista:list) -> str:
    """Imprime una lista con las opciones de un menu y pide un string como opcion a elegir

    Args:
        lista (list): Lista con las opciones a mostrar

    Returns:
        str: El string de la opcion elegida
    """
    limpiar_pantalla()
    for opcion in lista:
        print(opcion)
    return input("Ingrese opcion: ").lower()

def pedir_confirmacion(mensaje:str)->bool:
    """Pide confirmacion de salida

    Args:
        mensaje (str): Mensaje a mostrar

    Returns:
        bool: Retorna True si la respuesta es si, false en caso contrario
    """
    rta = input(mensaje).lower()
    return rta == "s"

#*****************************************************************************

# Buscadores

def filter_list(filtradora, lista:list)->list:
    """Filtra una lista con los parametros que le pasemos

    Args:
        filtradora (_type_): funcion que indica si swapear o no el dato
        lista (list): lista a ser filtrada

    Returns:
        list: lista filtrada
    """
    lista_filtrada = []
    for empleado in lista:
        if filtradora(empleado):
            lista_filtrada.append(empleado)
    return lista_filtrada

def buscar_max_min_dict(lista:list,key:str,tipo_dato=str,max:bool=True)->dict:
    """Busca el maximo o minimo de una lista de diccionarios segun le indiquemos

    Args:
        lista (list): Lista con los diccionarios
        key (str): Key del dato a comparar
        tipo_dato (_type_, optional): Tipo de dato a evaluar. Defaults to str.
        max (bool, optional): Booleano para indicar si se busca el maximo o el minimo. Defaults to True.

    Returns:
        dict: Diccionario max/min segun lo pedido
    """
    return reduce_lista(lambda valor_1,valor_2:valor_1 if 
    validar_mayor_menor_a_eleccion(tipo_dato(valor_1[key]),tipo_dato(valor_2[key]),max) else valor_2,lista)

def mapear_lista(mapeadora, lista:list)->list:
    """Se encarga de separar los datos que indiquemos de una lista

    Args:
        mapeadora (_type_): funcion que se encarga de diferenciar que datos queremos
        lista (list): lista a procesar

    Returns:
        list: lista con los datos de una key mapeada
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(mapeadora(el))
    return lista_retorno

#*****************************************************************************

def listar_cada_dato(lista:list, clave:str):
    """
    Recibe una lista y clave del dato a contar

    Inicializa las lista, al recorrerla agregan el dato una sola vez
    si se repite el contador suma uno mas a la segunda lista

    imprime las dos listas en orden
    """

    lista_dato = []
    contador_dato = []
    for elemento in lista:
        
        if elemento[clave] not in lista_dato:
            if elemento[clave] == "":
                elemento[clave] = "No tiene"
            lista_dato.append(elemento[clave])
            contador_dato.append(1)
        elif elemento[clave] in lista_dato:
            for e_dato in range(len(lista_dato)):
                if lista_dato[e_dato] == elemento[clave]:
                    contador_dato[e_dato] += 1
    print(lista_dato)
    print(contador_dato)

def ordenar_lista(criterio, lista:list)->None:
    """Se encarga se ordenar una lista segun queramos

    Args:
        criterio (_type_): Funcion con el criterio de ordenanza
        lista (list): Lista a ordenar
    """
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if criterio(lista[i], lista[j]):
                swap_lista(lista,i,j)

def swap_lista(lista:list, i:int, j:int)->None:
    auxiliar = lista[i]
    lista[i] = lista[j]
    lista[j] = auxiliar    