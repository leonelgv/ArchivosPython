from Rectangulo import *

class Archivos:
    def leerArchivo(self, archivo):
        file = open(archivo, 'r')
        lineas = []
        lineas_archivo = []
        for linea in file.readlines():
            lineas.append(linea.replace('\n', '').split('#'))
        for f in range(0, len(lineas)):
            try:
                lineas_archivo.append([float(lineas[f][0]), float(lineas[f][1])])
            except ValueError:
                lineas_archivo.append([0.0,0.0])
        return lineas_archivo

    def calcularResultados(self, lista):
        lineas_resultados = []
        rectangulo = Rectangulo()
        for f in range(0, len(lista)):
            area = rectangulo.calcularArea(lista[f][0], lista[f][1])
            perimetro = rectangulo.calcularPerimetro(lista[f][0], lista[f][1])
            lineas_resultados.append([area, perimetro])
        return lineas_resultados

    def guardarResultados(self, elementos, resultados):





def main():
    archivo = Archivos()
    lineas = archivo.leerArchivo('rectangulos.txt')
    resultados = archivo.calcularResultados(lineas)
    print(resultados)

if __name__==  '__main__':
   main()
