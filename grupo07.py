import re
cadena = "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"
cadenaminmayus = "a", "b", "c", "d", "e", "l", "A", "B", "C", "D", "E"
cadenamodif = cadena.split("\n")
cadenafirst = []
antecedentes = []
variable = []
for x in range(len(cadenamodif)):
    if cadenamodif[x] is not None:
        antecedentes.append((cadenamodif[x])[0])
        co = 0
        for y in range(len(cadenaminmayus)):
            co = co + 1
            if co == 1:
                variable = []
            variable = re.findall(r':.', cadenamodif[x])
            letra = ":" + cadenaminmayus[y]
            if letra == variable[0]:
                cadenafirst.append(cadenaminmayus[y])
            else:
                if variable[0] == ':l':
                    variable2 = re.findall(r':......', cadenamodif[x])
                    if variable2[0] == ':lambda':
                        cadenafirst.append("lambda")
                        break;

print(antecedentes,cadenafirst)

class Gramatica():

    def __init__(self, gramatica):
        """Constructor de la clase.

        Parameters
        ----------
        gramatica : string
            Representación de las producciones de una gramática determinada.

            Ejemplo:
            "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"
        """
        self(gramatica)

        pass

    def isLL1(self, Gramatica):
        """Verifica si una gramática permite realizar derivaciones utilizando
           la técnica LL1.

        Returns
        -------
        resultado : bool
            Indica si la gramática es o no LL1.
        """
        cadena = Gramatica

        cadena.split("/n")
        return

    def parse(self, cadena):
        """Retorna la derivación para una cadena dada utilizando las
           producciones de la gramática y los conjuntos de Fi, Fo y Se
           obtenidos previamente.

        Parameters
        ----------
        cadena : string
            Cadena de entrada.

            Ejemplo:
            babc

        Returns
        -------
        devivacion : string
            Representación de las reglas a aplicar para derivar la cadena
            utilizando la gramática.
        """
        pass

