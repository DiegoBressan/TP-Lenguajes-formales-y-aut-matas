import re
#cadena = "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"
cadena = "A:b\nA:e\nB:d\nB:lambda\nB:A p\nA:lambda\nC:f\nC:lambda\nS:A B C c"
cadenaminmayus = "a", "b", "c", "d", "e", "l", "A", "B", "C", "D", "E"
cadenamodif = cadena.split("\n")
cadenafirst = []
antecedentes = []
NoTerminales = []
variable = []
FIRST = []
FOLLOWS = []

"""     First de los que el primer valor en el consecuente es un Terminal o lambda      """
for x in range(len(cadenamodif)):
    if cadenamodif[x] is not None:
        antecedentes.insert(x, cadenamodif[x][0])
        variable = re.findall(r':.', cadenamodif[x])
        if variable[0] == ':l':
            variable2 = re.findall(r':......', cadenamodif[x])
            if variable2[0] == ':lambda':
                FIRST.insert(x, 'lambda')
            else:
                FIRST.insert(x, variable[0][1])
        else:
            if (ord(variable[0][1]) > 32 and ord(variable[0][1]) < 65) or (ord(variable[0][1]) > 90 and ord(variable[0][1]) < 127):
                FIRST.insert(x, variable[0][1])
            else:
                FIRST.insert(x, '-')

"""     Calcula los First de los que el primer valor en el consecuente es un No Terminal  """
conta = 0
while conta != 2:
    conta = conta + 1
    for x in range(0, len(cadenamodif)):
        variable = cadenamodif[x]
        co = 2
        let = ''
        ban = 0
        if (ord(variable[co]) > 64) and (ord(variable[co]) < 91):
            while ban == 0:
                if (ord(variable[co]) > 64) and (ord(variable[co]) < 91):
                    for y in range(0, len(antecedentes)):
                        if variable[co] == antecedentes[y]:
                            if FIRST[y] == 'lambda':
                                co = co + 2
                                ban = 0
                                break
                            else:
                                if FIRST[y] != '-':
                                    band = 0
                                    ban = 1
                                    for z in range(len(let)):
                                        if FIRST[y] == let[z]:
                                            band = 1
                                            conta = 2
                                            break
                                    if band == 0:
                                        let = let + FIRST[y]
                else:
                    ban = 1
                    let = let + variable[co]
        if let != '':
            FIRST[x] = let

print(FIRST)
print(antecedentes)

# Follows
# Guardo los no terminales
co = 0
for x in range(len(cadenamodif)):
    variable = cadenamodif[x]
    if co == 0:
        co = 1
        NoTerminales.append(variable[0])
        FOLLOWS.append('$')
    else:
        ban = 0
        for z in range(len(NoTerminales)):
            if NoTerminales[z] == variable[0]:
                ban = 1
                break
        if ban == 0:
            NoTerminales.append(variable[0])

print(NoTerminales)

# Calculo los Follows
for x in range(len(NoTerminales)):
    for y in range(len(cadenamodif)):
        variable = cadenamodif[y]
        co = 2
        aux = (len(cadenamodif[y])) - 1
        while co <= aux:
            if NoTerminales[x] == variable[co]:
                if (co + 2) > aux:
                    for z in range(len(NoTerminales)):
                        if NoTerminales[z][0] == variable[0]:
                            let = let + FOLLOWS[z]
                            break
                else:
                    if (ord(variable[co+2]) > 32 and ord(variable[co+2]) < 65) or (ord(variable[co+2]) > 90 and ord(variable[co+2]) < 127):
                        let = let + variable[co+2]
                    else:
                        for z in range(len(antecedentes)):
                            if antecedentes[z] == variable[co+2]:
                                if FIRST[z] != 'lambda':
                                    let = let + FIRST[z]
                                else:
                                    let = let #Falta hacer que pasa si el NT es lambda
            co = co + 2
    FOLLOWS.insert(x, let)

print(FOLLOWS)

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

