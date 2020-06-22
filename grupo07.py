import re
#cadena = "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"
#cadena = "S:A B C c\nA:b\nA:e\nB:d\nB:lambda\nB:A p\nA:lambda\nC:f\nC:lambda"
cadenamodif = []

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
        cadenamodif = gramatica.split("\n")
        self.gramatica = cadenamodif
        self.antecedentes = Gramatica.calculo_antecedente(self.gramatica)
        self.select = Gramatica.calculo_select(self.gramatica)

    def isLL1(self):
        """Verifica si una gramática permite realizar derivaciones utilizando
           la técnica LL1.

        Returns
        -------
        resultado : bool
            Indica si la gramática es o no LL1.
        """

        SELECT = self.select
        antecedentes = self.antecedentes
        buleano = True
        for x in range(len(SELECT) - 1):
            for y in range(len(SELECT) - 1):
                if y >= x:
                    if antecedentes[x] == antecedentes[y + 1]:
                        aux1 = len(SELECT[x])
                        aux2 = len(SELECT[y+1])
                        for t in range(aux1):
                            for z in range(aux2):
                                if SELECT[x][t] == SELECT[y+1][z]:
                                    buleano = False
                                    break
                            if buleano is False:
                                break
                    if buleano is False:
                        break
            if buleano is False:
                break

        return buleano

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
        SELECT = self.select
        antecedentes = self.antecedentes
        cadenamodif = self.gramatica
        regla = []

        if g.isLL1(): # Controla si la gramatica es LL1, sino no realiza el parser
            regla.append(cadenamodif[0])
            cont = 0
            p = len(cadena)
            x = 0
            while x < p:
                aux = ''
                if cadena[x] == '$': #Cuando encuentra el final, corta, si quedaron variables NoTerminales que son lambda los borra
                    ban = 0
                    variable2 = ''
                    for h in range(len(regla[cont])):
                        if ban == 1:
                            variable2 = variable2 + regla[cont][h]
                            if (ord(regla[cont][h]) < 65) or (ord(regla[cont][h]) > 90):
                                aux = aux + regla[cont][h]
                        else:
                            if (regla[cont][h] == ':') or (regla[cont][h] == '>'):
                                ban = 1
                    if aux != variable2:
                        variable = variable2 + '=>' + aux
                        regla.append(variable)
                    x = p
                else:
                    if ord(cadena[x]) != 32: # Controla que el caracter que se compara no sea un espacio
                        ban = 0
                        for q in range(len(regla[cont])):
                            if ban == 1:
                                aux = aux + regla[cont][q]
                            else:
                                if (regla[cont][q] == ':') or (regla[cont][q] == '>'):
                                    ban = 1
                        bandera = 0
                        for q in range(len(aux)):
                            for r in range(len(antecedentes)):
                                if bandera == 1:
                                    break
                                else:
                                    if (aux[q] == antecedentes[r]) and (cadena[x] in SELECT[r]):
                                        variable = aux + '=>'
                                        variable2 = ''
                                        ban = 0
                                        for z in range(len(regla[cont])):
                                            if ban == 1:
                                                if regla[cont][z] == antecedentes[r]:
                                                    band = 0
                                                    for t in range(len(cadenamodif[r])):
                                                        if band == 1:
                                                            variable2 = variable2 + cadenamodif[r][t]
                                                        else:
                                                            if (cadenamodif[r][t] == ':') or (cadenamodif[r][t] == '>'):
                                                                band = 1
                                                    variable = variable + variable2
                                                    if cadena[x] in cadenamodif[r]:
                                                        x = x + 1
                                                else:
                                                    variable = variable + regla[cont][z]
                                            else:
                                                if (regla[cont][z] == ':') or (regla[cont][z] == '>'):
                                                    ban = 1
                                        regla.append(variable)
                                        bandera = 1
                                        break
                        cont = cont + 1
                    else:
                        x= x + 1

        retornar = ''
        for x in range(len(regla)):
            if x == 0:
                retornar = regla[x]
            else:
                retornar = retornar + ' => ' + regla[x]

        return retornar

    def calculo_antecedente(cadenamodif):

        antecedentes = []
        for x in range(len(cadenamodif)):
            if cadenamodif[x] is not None:
                antecedentes.append(cadenamodif[x][0])

        return antecedentes

    def calculo_select(cadenamodif):
        NoTerminales = []
        FIRST = []
        FOLLOWS = []
        SELECT = []
        lista_antecedentes = Gramatica.calculo_antecedente(cadenamodif)

        # First de los que el primer valor en el consecuente es un Terminal o lambda
        for h in range(len(cadenamodif)):  # elimina espacio en blanco luego del :
            if ord(cadenamodif[h][2]) == 32:
                cadenamodif[h] = re.sub(r':.', '', cadenamodif[h])
                cadenamodif[h] = cadenamodif[h][0:1] + ':' + cadenamodif[h][1:]

        for x in range(len(cadenamodif)):
            if cadenamodif[x] is not None:
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

        # Calcula los First de los que el primer valor en el consecuente es un No Terminal
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
                        if co > len(variable):
                            ban = 1
                        else:
                            if (ord(variable[co]) > 64) and (ord(variable[co]) < 91):
                                for y in range(0, len(lista_antecedentes)):
                                    if variable[co] == lista_antecedentes[y]:
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

        # Calculo los Follows
        ban = 0
        for x in range(len(NoTerminales) - 1):
            FOLLOWS.append('-')

        for x in range(len(NoTerminales)):
            let = ''
            for y in range(len(cadenamodif)):
                variable = cadenamodif[y]
                co = 2
                cont = 0
                aux = (len(cadenamodif[y])) - 1
                while co <= aux:
                    if NoTerminales[x] == variable[co]:             # Si el No Terminal estaultimo guarda los FOLLOWS del No Terminal del antecedente
                        if (co + 2) > aux:
                            for z in range(len(NoTerminales)):
                                if NoTerminales[z][0] == variable[0]:
                                    if FOLLOWS[z] != '-':
                                        let = let + FOLLOWS[z]
                                        break
                                    break
                        else:
                            if (ord(variable[co + 2]) > 32 and ord(variable[co + 2]) < 65) or (ord(variable[co + 2]) > 90 and ord(variable[co + 2]) < 127):
                                if variable[co + 2] not in let:
                                    let = let + variable[co + 2]  # Guarda los datos si es un Terminal
                            else:
                                banderita = 0
                                for z in range(len(lista_antecedentes)):
                                    if lista_antecedentes[z] == variable[co + 2]:
                                        if FIRST[z] != 'lambda':
                                            conta = (len(let)) - 1
                                            ban = 0
                                            for x in range(conta):
                                                if FIRST[z] in let:
                                                    ban = 1
                                                    break
                                            if ban == 0:
                                                let = let + FIRST[z]
                                        else:
                                            banderita = 1
                                if banderita == 1:
                                    banderapatria = 0
                                    for n in range(len(let)):                # Metodo burbuja para eliminar un elemento de la posicion, para que
                                        for m in range(len(FOLLOWS[cont])):  # al transcribir los follows del antecedente se incluyan y no se repitan
                                            if FOLLOWS[cont][m] == let[n]:
                                                aux = FOLLOWS[cont]
                                                del aux[m]
                                                let = let + aux
                                                banderapatria = 1
                                    if banderapatria == 0:
                                        let = let + FOLLOWS[cont]
                    co = co + 2
                    cont = cont + 1
            if let != "":
                FOLLOWS[x] = let

        # SELECT
        # Crea la lista de los SELECT
        for x in range(len(FIRST)):
            if FIRST[x] == 'lambda':
                for y in range(len(NoTerminales)):
                    if NoTerminales[y] == lista_antecedentes[x]:
                        SELECT.append(FOLLOWS[y])
            else:
                SELECT.append(FIRST[x])

        return SELECT

#g = Gramatica('S:A\nA:B A\nA:lambda\nB:a B\nB:b')
#print(g.isLL1())
#print(g.parse('a a a b $'))