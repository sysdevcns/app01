import sys
import subprocess


dir = sys.executable
cmd = ' -m pip install '
nmd = 'openpyxl'
nmd = 'customtkinter'
nmd = 'ttkbootstrap'
nmd = 'extra-streamlit-components'
nmd = 'streamlit-cookies-manager'
nmd = 'freeze > requirements.txt'
nmd = 'psycopg2'
nmd = 'psycopg2-binary'
#nmd = ''



print(dir+cmd+nmd) #Comando que será executado 
subprocess.run(dir+cmd+nmd, shell=True)

#import pandas as pd
#df = pd.read_excel('distratos.xlsx')
#print(df)