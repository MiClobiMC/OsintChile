import argparse
import sources.salud as salud
import sources.edadrut as edadrut
import sources.texto as texto
import sources.sii as sii
import sources.volanteomaleta as volanteomaleta

parser = argparse.ArgumentParser(prog='doxingchile', description='Busqueda automatica en fuentes abiertas (y no tan abiertas) de chile')
parser.add_argument('-rut',  type=str, nargs='?', help='Rut de la persona a buscar, con formato: 11111111-1 ')

parametros = parser.parse_args()

parametros.rut = input("Ingrese el rut de la persona: ")

if not(parametros.rut):
    parser.print_help()

if parametros.rut:
    texto.busqueda(rut = parametros.rut)
    salud.busqueda(rut = parametros.rut)
    edadrut.busqueda(rut = parametros.rut)
    sii.busqueda(rut = parametros.rut)
    volanteomaleta.busqueda(rut = parametros.rut)
