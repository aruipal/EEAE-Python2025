'''Diseña una clase AnalizadorTexto con un atributo para una cadena de texto.
Implementa un método que cuente cuántas vocales (a, e, i, o, u) hay en el texto.'''

class AnalizadorTexto:
    
    def __init__(self,cadena):
        self.cadena = cadena
        
    def contador(self):
        contador = 0
        for i in self.cadena:
            if i in "aeiouAEIOU":
                contador = contador + 1
        return contador
            
texto = input("\nCONTADOR DE VOCALES\n- Introduce un texto: ")            
cadena1 = AnalizadorTexto(texto)
print(f"La cadena de texto contiene {cadena1.contador()} vocales.")