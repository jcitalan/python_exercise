import pandas as pd 
from os.path import exists
import os
import csv



def cada_mitad():
  '''
    Genera update cada mitad
  '''
  row_max = pd.read_csv('data_ids.csv')
  mitad=int((len(row_max)+1)/2)


  contador=0
  print("La mitad es {}".format(mitad))
  with open("sentencias_sql_uno.txt", 'w') as f:
    with open('data_ids.csv') as File:  
        reader = csv.reader(File)
        max_len_csv=len(row_max)
        print(max_len_csv)
        for x,row in enumerate(reader):
          while(contador<=(mitad-1)):
            f.write('update suscripcion set estado=False'+'\n')
            contador+=1
          print(contador)
          with open("sentencias_sql_dos.txt", 'w') as f:
            while(contador<=((mitad+mitad)-1)):
              f.write('update suscripcion set estado=False'+'\n')
              contador+=1

def cada_cien():
  '''
    Genera update cada 100
  '''
  row_max = pd.read_csv('data_ids.csv')
  mitad=int((len(row_max)+1)/2)


  contador=0
  numero_archivo=1
  print("La mitad es {}".format(mitad))
  with open('data_ids.csv') as File:  
      reader = csv.reader(File)
      max_len_csv=len(row_max)
      print(max_len_csv)
      with open("sentencias_sql_{}.txt".format(numero_archivo), 'w') as f:
        for x,row in enumerate(reader):
          print(contador)
          f.write('update suscripcion set estado=False'+'\n')
          contador=+1
          if contador==100:
            contador=0
            numero_archivo+=1
cada_mitad()
cada_cien()