import re
cadena = "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"
cadenaminmayus = "a", "b", "c", "d", "e", "l", "A", "B", "C", "D", "E"
cadenamodif = cadena.split("\n")
cadenafirst = []
antecedentes = []
variable = []
FIRST = []

"""        First           """

"""     First de los que el primer valor en el consecuente es un Terminal o lambda      """
for x in range(len(cadenamodif)):
    if cadenamodif[x] is not None:
        antecedentes.append(cadenamodif[x][0])
        variable = re.findall(r':.', cadenamodif[x])
        if variable[0] == ':l':
            variable2 = re.findall(r':......', cadenamodif[x])
            if variable2[0] == ':lambda':
                FIRST.append('lambda')
            else:
                FIRST.append(variable[0][1])
        else:
            if (ord(variable[0][1]) > 32 and ord(variable[0][1]) < 65) or (ord(variable[0][1]) > 90 and ord(variable[0][1]) < 127):
                FIRST.append(variable[0][1])

"""     Calcula los First de los que el primer valor en el consecuente es un No Terminal  """
for x in range(0, len(cadenamodif)):
    variable = re.findall(r':.', cadenamodif[x])
    co = 1
    let = ''
    ban = 0
    while ban == 0:
        if (ord(variable[0][co]) > 64) and (ord(variable[0][co]) < 91):
            variable2 = variable[0][co]
            co = 1
            for y in range(0, len(antecedentes)):
                if variable2 == antecedentes[y]:
                    if FIRST[y] == 'lambda':
                        co = co + 2
                    else:
                        band = 0
                        ban = 1
                        for z in range(len(let)):
                            if FIRST[y] == let[z]:
                                band = 1
                                break
                        if band == 0:
                            let = let + FIRST[y]
        else:
            ban = 1
    if let != '':
        FIRST.insert(x, let)

print(FIRST)
print(antecedentes)

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

