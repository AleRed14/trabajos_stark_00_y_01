# Desafío #01:

from funciones_stark import *
from data_stark import lista_personajes

lista_opciones = ["A. Imprimir heroes.","B. Imprimir heroe mujeres.","C. Determinar heroe mas alto.",
                  "D. Determinar heroe mujer mas alta.","E. Determinar heroe mas bajo.",
                  "F. Determinar heroe mujer mas baja.","G. Determinar altura promedio heroes.",
                  "H. Determinar altura promedio heroes mujer.","I. Mostrar los nombres.",
                  "J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.",
                  "K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.",
                  "L. Determinar cuántos superhéroes tienen cada tipo de inteligencia.",
                  "M. Listar todos los superhéroes agrupados por color de ojos.",
                  "N. Listar todos los superhéroes agrupados por color de pelo.",
                  "O. Listar todos los superhéroes agrupados por tipo de inteligencia.","P. Salir."]

def menu(lista:list,lista_ops:list):
    seguir = True
    bandera_heroe_mas_alto = False
    bandera_heroe_mujer_mas_alta = False
    bandera_heroe_mas_bajo = False
    bandera_heroe_mujer_mas_baja = False
    bandera_promedio_altura_heroes = False
    bandera_promedio_altura_heroe_mujeres = False
    lista_heroes = filter_list(lambda her: her["genero"] == "M",lista)
    lista_heroe_mujeres = filter_list(lambda her: her["genero"] == "F",lista)
    while seguir:
        match menu_con_lista(lista_ops):
            case "a":
                print()
                mostrar_nombres_heroes(lista_heroes)
                print()
            case "b":
                print()
                mostrar_nombres_heroes(lista_heroe_mujeres)
                print()
            case "c":
                heroe_mas_alto = buscar_max_min_dict(lista_heroes,"altura",float)
                bandera_heroe_mas_alto = True
            case "d":
                heroe_mujer_mas_alta = buscar_max_min_dict(lista_heroe_mujeres,"altura",float)
                bandera_heroe_mujer_mas_alta = True
            case "e":
                heroe_mas_bajo = buscar_max_min_dict(lista_heroes,"altura",float,False)
                bandera_heroe_mas_bajo = True
            case "f":
                heroe_mujer_mas_baja = buscar_max_min_dict(lista_heroe_mujeres,"altura",float,False)
                bandera_heroe_mujer_mas_baja = True
            case "g":
                promedio_altura_heroes = promedio_dict(lista_heroes,"altura")
                bandera_promedio_altura_heroes = True
            case "h":
                promedio_altura_heroe_mujeres = promedio_dict(lista_heroe_mujeres,"altura")
                bandera_promedio_altura_heroe_mujeres= True
            case "i":
                print()
                if bandera_heroe_mas_alto:
                    print("El heroe mas alto es:")
                    mostrar_nombre_heroe(heroe_mas_alto)
                else:
                    print("No se calculo el heroe mas alto.")
                print("-----------------------------------------------------")
                if bandera_heroe_mujer_mas_alta:
                    print("La heroe mujer mas alta es:")
                    mostrar_nombre_heroe(heroe_mujer_mas_alta)
                else:
                    print("No se calculo la heroe mujer mas alta.")
                print("-----------------------------------------------------")
                if bandera_heroe_mas_bajo:
                    print("El heroe mas bajo es:")
                    mostrar_nombre_heroe(heroe_mas_bajo)
                else:
                    print("No se calculo el heroe mas bajo.")
                print("-----------------------------------------------------")
                if bandera_heroe_mujer_mas_baja:
                    print("La heroe mujer mas baja es:")
                    mostrar_nombre_heroe(heroe_mujer_mas_baja)
                else:
                    print("No se calculo la heroe mujer mas baja.")
                print("-----------------------------------------------------")
                if bandera_promedio_altura_heroes:
                    print("El promedio de altura de los heroes es:")
                    mostrar_nombre_heroe(promedio_altura_heroes)
                else:
                    print("No se calculo el promedio de altura de los heroes.")
                print("-----------------------------------------------------")
                if bandera_promedio_altura_heroe_mujeres:
                    print("El promedio de altura de las heroe mujeres es:")
                    mostrar_nombre_heroe(promedio_altura_heroe_mujeres)
                else:
                    print("No se calculo el promedio de altura de las heroe mujeres.")
                print("-----------------------------------------------------")
                print()
            case "j":
                mostrar_cantidad_elementos_de_un_dato(lista_personajes,"color_ojos")
            case "k":
                mostrar_cantidad_elementos_de_un_dato(lista_personajes,"color_pelo")
            case "l":
                mostrar_cantidad_elementos_de_un_dato(lista_personajes,"inteligencia")
            case "m":
                mostrar_personajes_x_dato(lista,"color_ojos")
            case "n":
                mostrar_personajes_x_dato(lista,"color_pelo")
            case "o":
                mostrar_personajes_x_dato(lista,"inteligencia")
            case "p":
                seguir = pedir_confirmacion("Quiere salir? s/n: ")
                continue
        pausar()
menu(lista_personajes,lista_opciones)
