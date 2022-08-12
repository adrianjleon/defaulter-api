import pymysql
import pandas as pd
  
def request_data_from_db(host='localhost', user='root',password = "root", db='house_price'):
    """
     Conection to de DB and fetch data into a DataFrame
     
    """

    #se colocan los parametros de conexión a la BD en MySQL
    conn = pymysql.connect(host= host , user=user, password = password, db=db)
    #se crea el cursor de la conexión que permite ejecutar el query  
    cur = conn.cursor()
    #se ejecuta el query de la tabla en BD
    cur.execute("select * from variables")
    #se guarda en output una tupla de individuos con todas su variables
    output = cur.fetchall()
    #se guarda en des una tupla de descripciones de cada variable donde el 1er elemento es el nombre de la columna
    desc = cur.description
   
    lista_variables = []
    for i in range(len(desc)):
        #agrega a la lista vacia los nombres de las columnas en "desc" 
        lista_variables.append(desc[i][0])
    #se crea el DF con los valores de los individuos y los nombres de las columnas     
    df = pd.DataFrame(list(output),columns=lista_variables)
    print(df)
    #se cierra la conexión 
    conn.close()

    return df

def insertar_datos_bd(df):
    pass

request_data_from_db()