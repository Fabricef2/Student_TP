#Importation des modules et pour la connection à mysql
import pandas as pd
import mysql.connector
from mysql.connector import Error

#Chargement des données
student_data = pd.read_excel('student_m.xlsx')
print(student_data.columns)

colonnes = ['school', 'sex', 'age', 'address','famsize', 'pstatus', 'medu', 'fedu', 'mjob', 'fjob', 'reason', 'guardian']
student_data.columns = colonnes 
print('----------------------------------------------------------------')
print(student_data.columns)

# Chargement du dataframe dans MYSQL
try:
    connexion = mysql.connector.connect(host='localhost',
                                       database='db_student',
                                       user='root',
                                       password='')
    if connexion.is_connected():
        print('Connexion à MySQL réussie')
except Error as e:
    print(f"Erreur lors de la connexion à MySQL: {e}")

try:
    cursor = connexion.cursor()

    for i,row in student_data.iterrows():
        sql = """INSERT INTO student (school,sex,age,address,famsize,pstatus,medu,fedu,mjob,fjob,reason,guardian) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        #print(sql)
        cursor.execute(sql, tuple(row))

    connexion.commit()
    connexion.close()
    print("DataFrame chargé dans MySQL avec succès!")
except Exception as e:
    print(f"Erreur lors du chargement du DataFrame dans MySQL: {e}")
