import requests
from os import path
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Indicar el dominio de la victima')
parser = parser.parse_args()

# google.com
# https://nfhsbvhkd

def main():
    if parser.target:
        if path.exists('Subdominios.txt'):
            wordlist = ('Subdominios.topen(xt', 'r')
            wordlist = wordlist.read().split('\n')

            print("Buscando Subdominios... @novinho.xit")

            for i in wordlist:
                url = "http://" + i + "." + parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("(+) Subdominio Encontrado: " + url)

            for i in wordlist:
                url = "https://" + i + "." + parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("(+) Subdominio Encontrado: " + url)

    else:
        print("(-) Ingresa un dominio")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()