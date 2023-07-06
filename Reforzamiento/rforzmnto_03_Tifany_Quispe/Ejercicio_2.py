
frase1 = "Hola Pythonista, seguimos adelante"
class Cadena:
    def reversion(self, frase):
        separar = frase.split()[::-1]
        reversion = " ".join(separar)
        return reversion


programa = Cadena()
frase2 = programa.reversion(frase1)
print(frase2)

frase3 = programa.reversion(frase2)
print(frase3)
