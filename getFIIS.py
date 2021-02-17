from urllib.request import urlopen, Request
from pyquery import PyQuery as pq
import lxml, lxml.html
import os
import datetime
from bs4 import BeautifulSoup
import pandas
import mysql.connector

##mydb = mysql.connector.connect(
##  host="localhost",
##  user="root",
##  password="",
##  database="fii-data"
##)

##carrega os papeis de stocksList.csv
stocksList = open('FIIsList_Carteira.csv', 'r')
#papeis = stocksList.read().split(';')
#print(papeis)
#papeis = ["xppr11"]
stocksList.close()

def getpapel(papel_):
    try:
                    url = "https://statusinvest.com.br/fundos-imobiliarios/"
                    #print(papel+": "+str(content.code))
                    r = Request(url+papel_, headers={'User-Agent': 'Mozilla/5.0'})
                    html = urlopen(r).read()
                    soup = BeautifulSoup(html, 'html.parser')
                    #print(soup.prettify())
                    result = soup.find_all('table')
                    #print(result)

                    #cabecalho
                    table_head = result[0].find_all('th')

                    #for row in table_head:
                        #print (row.getText().strip())

                    #dados    
                    table_body = result[0].find_all('tr')
                    for row in table_body:
                        dados = row.find_all('td')
                        result = papel_+"*"
                        for dado in dados:
                            result = result+(dado.getText().strip())+"*"
                            #print(dado.getText().strip())
                        print(result)

                        
                    #for row in alldata:
                        #print(papel_+" - "+row[1]+" - "+row[4])
                        #data_atual = datetime.datetime.strptime(row[1], "%d/%m/%y")
                        #INICIO grava no banco de dados
                        #mycursor = mydb.cursor()
                        #sql = "INSERT INTO `dividendo-data`(`fii_nome`, `data_pagamento`, `valor_dividendo`) VALUES (%s, %s, %s)"
                        #val = (papel_,data_atual, float(row[4].replace(",",".")))
                        #mycursor.execute(sql, val)
                        #mydb.commit()
                        #FIM grava no banco de dados
                        #print(data_atual.month)

                    print("Removendo o papel "+papel_+" Faltam "+str(len(papeis)))
                    papeis.remove(papel_)
                    
                    
    except Exception as e:
        print("#ERRO: ",papel_," ", str(e))
        print("Removendo o papel "+papel_+" Faltam "+str(len(papeis)))
        papeis.remove(papel_)
        #print(papeis)
    
while len(papeis)>0:
    for papel in papeis:
        getpapel(papel)

            


