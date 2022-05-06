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

  contador=1
  numero_archivo=1

  with open('data_ids.csv') as File:  
      reader = csv.reader(File)
      max_len_csv=len(row_max)
      for row in reader:
        if(contador!=mitad):
          print("Contador: ",contador,"id: ",row)
          f=open("Lote de 500 registros no {}.txt".format(numero_archivo),'a')
          f.write('update suscripcion set estado=False\n')
          f.close()
          contador+=1
        elif(contador==mitad):
          f=open("Lote de 500 registros no {}.txt".format(numero_archivo),'a')
          f.write('update suscripcion set estado=False\n')
          f.close()
          print("Llege al numero de lote {} de 500:".format(numero_archivo))
          numero_archivo+=1
          contador=1
def cada_cien():
  '''
    Genera update cada 100
  '''
  row_max = pd.read_csv('data_ids.csv')
  total=len(row_max)+1
  contador=1
  numero_archivo=1
  with open('data_ids.csv') as File:
    reader = csv.reader(File)
    max_len_csv=len(row_max)
    for row in reader:
      if(contador!=100):
        print("Contador: ",contador,"id: ",row)
        f=open("Lote de 100 registros no {}.txt".format(numero_archivo),'a')
        f.write('update suscripcion set estado=False\n')
        f.close()
        contador+=1
      elif(contador==100):
        f=open("Lote de 100 registros no {}.txt".format(numero_archivo),'a')
        f.write('update suscripcion set estado=False\n')
        f.close()
        print("Contador: ",contador,"id: ",row)
        print("Llege al numero de lote {} de 100:".format(numero_archivo))
        numero_archivo+=1
        contador=1
cada_mitad()
cada_cien()