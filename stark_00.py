# Desafío #00:

from data_stark import lista_personajes
from funciones_stark import *

def mostrar_heroe_mas_alto(lista:list)->None:
    heroe_mas_alto = reduce_lista(lambda heroe_ant,heroe_act:heroe_ant if 
                        float(heroe_ant["altura"]) > float(heroe_act["altura"]) 
                        else heroe_act,lista)
    print(f"El superhéroe más alto es:")
    mostrar_heroe_solo(heroe_mas_alto)
    print()


def mostrar_heroe_mas_bajo(lista:list)->None:
    heroe_mas_bajo = reduce_lista(lambda heroe_ant,heroe_act:heroe_ant if 
                        float(heroe_ant["altura"]) < float(heroe_act["altura"]) 
                        else heroe_act,lista)
    print(f"El superhéroe más bajo es:")
    mostrar_heroe_solo(heroe_mas_bajo)
    print()

def mostrar_promedio_altura_heroes(lista:list)->None:
    acumulador_altura = acumular_datos(lista,"altura")
    promedio_altura = acumulador_altura / len(lista)

    print(f"El promedio de altura de todos los héroes es de: {promedio_altura}")

def mostrar_heroe_mas_pesado(lista:list)->None:
    heroe_mas_pesado = reduce_lista(lambda heroe_ant,heroe_act:heroe_ant if 
                        float(heroe_ant["peso"]) > float(heroe_act["peso"]) 
                        else heroe_act,lista)

    print(f"El superhéroe más pesado es:")
    mostrar_heroe_solo(heroe_mas_pesado)
    print()

def mostrar_heroe_menos_pesado(lista:list)->None:
    heroe_menos_pesado = reduce_lista(lambda heroe_ant,heroe_act:heroe_ant if 
                        float(heroe_ant["peso"]) < float(heroe_act["peso"]) 
                        else heroe_act,lista)


    print(f"El superhéroe menos pesado es:")
    mostrar_heroe_solo(heroe_menos_pesado)
    print()

lista_opciones = ["A. Mostrar todos los nombres de los heroes.","B. Mostrar "
                  "nombre y altura de todos los heroes.","C. Mostrar superhéroe más alto.",
                  "D. Mostrar superhéroe más bajo.","E. Mostrar altura promedio de los superhéroes.",
                  "F. Mostrar superhéroe más pesado.", "G. Mostrar superhéroe menos pesado.",
                  "H. Salir."]
def menu_superheroes(lista:list, opciones_lista:list)->None:
    seguir = True
    while seguir:
        match menu_con_lista(opciones_lista):
            
            case "a":
                print()
                mostrar_nombres_heroes(lista)
                print()
            case "b":
                print()
                mostrar_nombre_altura_heroes(lista)
                print()
            case "c":
                print()
                mostrar_heroe_mas_alto(lista)
            case "d":
                print()
                mostrar_heroe_mas_bajo(lista)
            case "e":
                print()
                mostrar_promedio_altura_heroes(lista)
            case "f":
                print()
                mostrar_heroe_mas_pesado(lista)
            case "g":
                print()
                mostrar_heroe_menos_pesado(lista)
            case "h":
                print()
                seguir = not pedir_confirmacion("¿Quieres salir? s/n: ")
                continue
        pausar()
menu_superheroes(lista_personajes,lista_opciones)