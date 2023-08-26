import pandas as pd


archivo = "http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2013.csv"
df = pd.read_csv(archivo, sep=";")

print(df[(df.acu_cal_cla == "Siempre") & (df.acu_id_culp == "Nunca")])

class Cargar_conjunto_datos:

    referencia = ""
    nombre = ""    
     
    def calcular_promedio(self):
        pass

    def calcular_suma(self):
        pass
    
    