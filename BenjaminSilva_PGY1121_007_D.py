#mascota segura


#funciones
import numpy 
import time 
import os 
import msvcrt


#listas
lista_rut=[]
lista_nombre=[]
lista_identificador=[]
lista_mascota=[]
lista_dia=[]


#acciones
print ("""acciones
1.Grabar
2.Buscar
3.Retirarse
4.Salir""")


#validar opciones
def validar_opcion(): 
    while True:
        try:
            opc = int(input("ingrese opcion"))
            if opc in(1,2,3,4):
                return opc
            else:
                print ("error opcion incorrecta")
        except:
            print("error debe ingresar un numero")


def validar_rut():
    while True:
        try:
            rut=int(input("ingrese rut:"))
            if rut >= 1000000 and rut <= 99999999
                return rut
            else:
                print ("error rut entre 1000000 y 99999999")
        except:
            print("error ingrese un numero entero")


def validar_nombre():
    while True:
        nom=input("ingrese nombre")
        if nom len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("error debe tener al menos 3 letras")
   

def validar_identificador():
    while True:
        identificador = input("ingrese identificador(1,2,3,4,5,6,7,8,9,10):")
        if identificador.upper() in lista_identificador:
            return identificador
        else:
            print("error identificador incorrecto")


def validar_mascota():
    while True:
        mascota=input("ingrese mascota")
        if mascota len(mas.strip()) >= 3 and mascota.isalpha():
            return mascota
        else:
            print("error debe tener al menos 3 letras")


def validar_dia():
    while True:
        try:
            dia=int(input("ingrese dia"))
            if dia >= 1 and dia <= 365
                return dia
            else:
                print("error dia entre 1 y 365")
        except:
            print("error ingrese un numero entero")


