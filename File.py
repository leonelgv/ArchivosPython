from Circulo import *

class Archivos:

    def leerArchivo(self, archivo):
        f = open(archivo,'r')
        lineas_archivo = []
        for linea in f.readlines():
            lineas_archivo.append(linea.replace('\n', ''))
        f.close()
        return lineas_archivo

    def convertirStringANumeros(self, archivo):
        lineas_archivo = []
        try:
            for a in range(0, len(archivo)):
                lineas_archivo.append(int(archivo[a]))
        except ValueError:
            lineas_archivo.append(0)
        return lineas_archivo

    def escribirArchivo(self, archivo, lista):
        file = open(archivo, 'w')
        for f in range(0, len(lista)):
            linea = str(lista[f][0]) + ',' + str(lista[f][1]) + ',' + str(lista[f][2]) + '\n'
            file.write(linea)
        file.close()

def main():
    archivo = Archivos()
    circulo = Circulo()
    arreglo = []
    radios = []
    resultados = []
    arreglo = archivo.leerArchivo('radios.txt')
    radios = archivo.convertirStringANumeros(arreglo)

    for c in range(0, len(radios)):
        area = circulo.calcularArea(radios[c])
        perimetro = circulo.calcularPerimetro(radios[c])
        resultados.append([radios[c], area, perimetro])
    archivo.escribirArchivo('resultados.csv',resultados)
    #print(resultados)

if __name__==  '__main__':
   main()
