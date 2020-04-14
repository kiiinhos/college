# -*- coding: utf-8 -*-
import sys
import biblioteca

def menu():
    print ("Conversor de Medidas")
    print (" ")
    print ("Digite a opção desejada: ")
    print (" ")
    print ("1 Conversão de pes para jardas\n")
    print ("2 Conversão de polegadas para centimetros\n")
    print ("3 Conversão de jardas para metros\n")
    print ("4 Conversão de milhas para kms\n")
    print ("0 para sair") 
    print (" ")

    c = input("Digite a opção desejada: ")
    d = float(input("Digite a distância: "))

    if c == '1':
        print("Conversão de pes para jardas : ", biblioteca.pesMetros(d))
        
        
        

    elif c == '2':
        print("Conversão de polegadas para centimetros: ", biblioteca.polegadasCentimetro(d))
       

    elif c == '3':
        print("Conversor de jardas para metros ", biblioteca.jardasMetros(d))
     

    elif c =='4':
        print("Converso de milhas para kms: ", biblioteca.milhasQuilometros(d))
       

    elif c == '0':
        sys.exit()

    else:
        print("Digite a opção certa!")
        menu()
    menu()
menu()