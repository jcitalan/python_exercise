import pandas as pd 
from os.path import exists
import os
import csv
import time


def cada_mitad():
  '''
    Genera update cada mitad
  '''
  row_max = pd.read_csv('data_ids.csv')
  mitad=int((len(row_max)+1)/2)


  contador=0
  print("La mitad es {}".format(mitad))
  with open('data_ids.csv') as File:  
      reader = csv.reader(File)
      max_len_csv=len(row_max)
      print(max_len_csv)
      with open("sentencias_sql_uno.txt", 'w') as f:
        with open("sentencias_sql_dos.txt", 'w') as d:
          for x,row in enumerate(reader):
            if(mitad<=x):
              f.write('update suscripcion set estado=False'+'\n')
              if(x<=(mitad+mitad)-1):
                  d.write('update suscripcion set estado=False'+'\n')
def escribe_txt(name,sql):
  with open(name, 'w') as f:
    for row in range(0,100):
      f.write(sql)

def cada_cien():
  '''
    Genera update cada 100
  '''
  row_max = pd.read_csv('data_ids.csv')
  total=len(row_max)+1
  # print(total)
  contador=1
  numero_archivo=1

  print("La mitad es {}".format(total))
  with open('data_ids.csv') as File:
    reader = csv.reader(File)
    max_len_csv=len(row_max)
    print(max_len_csv)
    for x,row in enumerate(reader):
      if(contador!=100):
        print("index:",x,"Contador: ",contador,"id: ",row)
        contador+=1
      elif(contador==100):
        escribe_txt("Lote numero {}.txt".format(numero_archivo),'update suscripcion set estado=False\n')
        print("index:",x,"Contador: ",contador,"id: ",row)
        print("Llege al primero lote de 100 del archivo no:",numero_archivo)
        numero_archivo+=1
        contador=1
cada_mitad()
cada_cien()