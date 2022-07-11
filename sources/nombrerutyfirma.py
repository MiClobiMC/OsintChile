import requests
import argparse
import json
from utils import rut as rutUtils
from bs4 import BeautifulSoup
import codecs

def busqueda(rut):
    busquedaNombrerutyFirma(rut)

def busquedaNombrerutyFirma(rut):
    params = {'term': rutUtils.formatRut(rut)}

    urlNryfRoted = 'uggcf://jjj.abzoerehglsvezn.pbz/ehg'
    urlNryf = codecs.decode(urlNryfRoted, 'rot_13')

    page = requests.post(url=urlNryf, params=params)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        tabla = soup.find('tr', tabindex='1')
        if tabla:
            datosTD = tabla.find_all('td')
            print('Nombre completo          :', datosTD[0].get_text())
            print('RUT                      :', datosTD[1].get_text())
            print('Sexo                     :', datosTD[2].get_text())
            print('Direccion                :', datosTD[3].get_text())
            print('Ciudad/Comuna            :', datosTD[4].get_text())
            print(" ")

        else:
            print('  No hay datos')
    else:
        print("  Error en request:", page.status_code)      

if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')