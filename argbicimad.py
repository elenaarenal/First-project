#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#terminal: python nombre del arhivo.py. Se ejecuta desde la terminal de arriba a abajo
#Es pasar argumentos al código desde la terminal para que el código haga algo.


# In[8]:


import argparse
import pandas as pd


# In[11]:


parser=argparse.ArgumentParser(description='bicimad')


#argumentos de entrada (defino). Los voy a escribir en la terminal

parser.add_argument('-t', '--titulo', type=str, help='Instalación accesible no municipal, input todos para listado completo')


#Inicio del parser

parser_args=parser.parse_args()

titulo=parser_args.titulo


df = pd.read_csv('bicimad_final2.csv')


instalacion=df[df['titulo']==titulo]


    
if titulo.lower()=='todos' or 'todas':
    print(df)

else:
    for index, row in instalacion.iterrows():
            print(f"La estación más cercana es: {row['name']}, ubicada en: {row['address']}, y se encuentra a: {row['distancia']} metros")



# In[ ]:





# In[ ]:




