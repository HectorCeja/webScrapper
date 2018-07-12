import requests as rqst
from bs4 import BeautifulSoup
import pandas as pnd
import numpy as np
import html5lib as html
import logging

logging.basicConfig(level=logging.INFO)

def webScrapper():
    logging.info('INICIANDO WEB SCRAPPER')
    logging.info('#' * 50)
    urlGeneral = 'https://catalog.data.gov/dataset'
    logging.info('Haciendo peticion a ' + str(urlGeneral))
    page = rqst.get(urlGeneral)
    strHTML = page.text
    soup = BeautifulSoup(strHTML,'html5lib')

    h3s = soup.find_all("h3", class_="dataset-heading")
    logging.info('Obteniendo h3 de la página ')
    for h3 in h3s:
        logging.info('#' * 100)

        urlH = urlGeneral + h3.find('a')['href']
        logging.info('Nueva URL obtenida: ' + urlH)
        #print(urlH)
        requestH3 =  rqst.get(urlH)
        strHTML_H3 =  requestH3.text
        soup_H3 = BeautifulSoup(strHTML_H3,'html5lib')
        a_s = soup_H3.find_all('a', {"data-format": 'csv'})
        logging.info('Obteniendo elementos a')
        for i, a in enumerate(a_s):
            url_download = a.get('href')

            if url_download is not None:
                logging.info('Enlace de descarga final ' + final_download)
                df = pnd.read_csv(url_download)
                df.to_csv(str(i) + ".csv")





    logging.info('Termina proceso de WEB SCRAPPER')


if __name__ == "__main__":
    webScrapper()
