# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv
import os
from pathlib import Path


def ej3():
    print('Ejercicio de archivos CSV 1º')
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    # tornillos = list(csv.DictReader(f))
    # for tornillo in tornillos:
    #     print(tornillo['tornillos'])

    # f.close()

    '''
    COMENTARIOS ADICIONALES DEL CODIGO
    En el caso de mi pc, necesite utilizar pathlib ya que no me reconocia la ruta 
    donde estaba trabajando el codigo
    '''
    print(os.getcwd()) 
    ruta = 'Modulo_5\\archivos_python'
    archivo = 'stock.csv'

    
    p_def =os.path.join(ruta,archivo)
    print('p_def ', p_def)
    p = Path(p_def)
    if p.is_file():
        print("El Archivo existe!")
        f = open(p, 'r')
        reg_stock = list(csv.DictReader(f))
        tot_reg_stock = 0
        for tornillo in reg_stock:
            # print(tornillo['tornillos'])
            tot_reg_stock += int( tornillo['tornillos'])
        
        f.close()
        print('Stock de tornillos ', tot_reg_stock)
    else:
        print("El archivo no existe o no se encuentra! ha ocurrido un error tipo IOError ")
    

def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    print(os.getcwd()) 
    ruta = 'Modulo_5\\archivos_python'
    

    p_def =os.path.join(ruta,archivo)
    print('p_def ', p_def)
    p = Path(p_def)
    if p.is_file():
        print("El Archivo existe!")
        f = open(p, 'r')
        data = list(csv.DictReader(f))
        # print(data)
        f.close()

        deptos_2_amb = 0
        deptos_3_amb = 0
        for depto in data:
            if depto['tipo_propiedad']== 'Departamento':
                try:
                    if (depto['ambientes'] == '2'):
                        deptos_2_amb +=1
                    elif (depto['ambientes'] == '3'):
                        deptos_3_amb +=1
                except:
                    print('Error, existen departamentos sin ambientes declarados. ')

        print('La cantidad de departamentos de 2 ambientes es: ', deptos_2_amb)
        print('La cantidad de departamentos de 3 ambientes es: ', deptos_3_amb)

            
    else:
        print("El archivo no existe o no se encuentra! ha ocurrido un error tipo IOError ")


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
