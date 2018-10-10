import aiml
import ast
import re

kernel = aiml.Kernel()

materii = ['Matematica', 'Structuri de date', 'Logica pentru informatica', 'Limba engleza 1',
           'Arhitectura calculatoarelor si sisteme de operare', 'Introducere in programare', 'Proiectarea algoritmilor',
           'Probabilitati si statistica', 'Sisteme de operare', 'Limba engleza 2', 'Programare orientata-obiect',
           'Fundamente algebrice ale informaticii', 'Algoritmica grafurilor', 'Retele de calculatoare',
           'Limbaje formale, automate si compilatoare', 'Limba engleza 3', 'Algoritmi genetici', 'Baze de date',
           'Ingineria programarii', 'Practica SGBD', 'Tehnologii WEB', 'Limba engleza 4', 'Programare avansata',
           'Modele continue si Matlab']

materii_an_curent =['Invatare automata', 'Inteligenta artificeala', 'Python',
            'Securitatea informatiei', 'Arhitectura software specifica automotive',
            'Dezvoltarea sistemelor fizice utilizand microprocesoare','Calcul numeric',
            'Grafica pe calculator', 'Cloud Computing', 'Android', 'Smart Cards']

materii_semestru = {'Matematica': 1, 'Structuri de date': 1, 'Logica pentru informatica': 1, 'Limba engleza 1': 1,
                    'Arhitectura calculatoarelor si sisteme de operare': 1, 'Introducere in programare': 1,
                    'Proiectarea algoritmilor': 2, 'Probabilitati si statistica': 2, 'Sisteme de operare': 2,
                    'Limba engleza 2': 2, 'Programare orientata-obiect': 2, 'Fundamente algebrice ale informaticii': 2,
                    'Algoritmica grafurilor': 3, 'Retele de calculatoare': 3,
                    'Limbaje formale, automate si compilatoare': 3, 'Limba engleza 3': 3, 'Algoritmi genetici': 3,
                    'Baze de date': 3, 'Ingineria programarii': 4, 'Practica SGBD': 4, 'Tehnologii WEB': 4,
                    'Limba engleza 4': 4, 'Programare avansata': 4, 'Modele continue si Matlab': 4}

materii_an = {'Matematica': 1, 'Structuri de date': 1, 'Logica pentru informatica': 1, 'Limba engleza 1': 1,
              'Arhitectura calculatoarelor si sisteme de operare': 1, 'Introducere in programare': 1,
              'Proiectarea algoritmilor': 1, 'Probabilitati si statistica': 1, 'Sisteme de operare': 1,
              'Limba engleza 2': 1, 'Programare orientata-obiect': 1, 'Fundamente algebrice ale informaticii': 1,
              'Algoritmica grafurilor': 2, 'Retele de calculatoare': 2,
              'Limbaje formale, automate si compilatoare': 2, 'Limba engleza 3': 2, 'Algoritmi genetici': 2,
              'Baze de date': 2, 'Ingineria programarii': 2, 'Practica SGBD': 2, 'Tehnologii WEB': 2,
              'Limba engleza 4': 2, 'Programare avansata': 2, 'Modele continue si Matlab': 2}

materii2note = {'Matematica': 6, 'Structuri de date': 8, 'Logica pentru informatica': 8, 'Limba engleza 1': 10,
                'Arhitectura calculatoarelor si sisteme de operare': 9, 'Introducere in programare': 10,
                'Proiectarea algoritmilor': 7, 'Probabilitati si statistica': 8, 'Sisteme de operare': 8,
                'Limba engleza 2': 10, 'Programare orientata-obiect': 9, 'Fundamente algebrice ale informaticii': 4,
                'Algoritmica grafurilor': 6, 'Retele de calculatoare': 8,
                'Limbaje formale, automate si compilatoare': 8, 'Limba engleza 3': 10, 'Algoritmi genetici': 9,
                'Baze de date': 10, 'Ingineria programarii': 9, 'Practica SGBD': 8, 'Tehnologii WEB': 8,
                'Limba engleza 4': 10, 'Programare avansata': 9, 'Modele continue si Matlab': 10}


materii_restante = ["Fundamente algebrice ale informaticii"]

materii_preferate = ['Retele de Calculatoare', 'Programare avansata','Ingineria programarii']

def calculateIntegralist():
    integralistSemester =[1,2,3,4]
    for materie in materii:
        if materii2note[materie] < 5:
            if materii_semestru[materie] in integralistSemester:
                integralistSemester.remove(materii_semestru[materie])
    if len(integralistSemester) > 1:
        print("Am fost integralist in semestrele "+str(integralistSemester))
    elif len(integralistSemester) is 1:
        print("Am fost integralist in semestrul "+str(integralistSemester))
    else:
        print("Nu am fost integralist in nici un semestru")

def calculateAniRestante():
    ani = []
    for materie,nota in materii2note.items():
        if nota < 5:
            if materii_an[materie] not in ani:
                ani.append(materii_an[materie])
    if len(ani)>1:
        print("Am avut restante in anii "+str(ani))
    elif len(ani) is 1:
        print("Am avut restante in anul "+str(ani))
    else:
        print("Nu am avut nici o restanta")

def calculateRestanteSem():

    sem = []
    for materie,nota in materii2note.items():
        if nota < 5:
            if materii_semestru[materie] not in sem:
                sem.append(materii_semestru[materie])
    if len(sem)>1:
        print("Am avut restante in semestrele "+str(sem))
    elif len(sem) is 1:
        print("Am avut restante in semestrul "+str(sem))
    else:
        print("Nu am avut nici o restanta")

def materiiPreferate():

    print("Materiile mele preferate sunt "+str(materii_preferate))

def materiiAnCurent():

    print("Materiile de anul acesta sunt "+str(materii_an_curent))

def enumerareRestante():

    if len(materii_restante) > 1:
        print("Am restante la materiile "+str(materii_restante))
    elif len(materii_restante) is 1:
        print("Am rastanta la "+str(materii_restante))
    else:
        print("Nu am nici o restanta")

def worstbestgrade(message):
    message.upper()
    if message == "_CEAMAIMICANOTADINFIECARESEMESTRU_":
        max1= 11
        max2= 11
        max3= 11
        max4= 11
        materi1 = None
        materi2 = None
        materi3 = None
        materi4 = None

        for materie,semestru in materii_semestru.items():
            if semestru is 1:
                if materii2note[materie]< max1:
                    max1 = materii2note[materie]
                    materi1 = materie
            elif semestru is 2:
                if materii2note[materie] < max2:
                    max2 = materii2note[materie]
                    materi2 = materie
            elif semestru is 3:
                if materii2note[materie] < max3:
                    max3 = materii2note[materie]
                    materi3 = materie
            elif semestru is 4:
                if materii2note[materie] < max4:
                    max4 = materii2note[materie]
                    materi4 = materie
        print("In semestrul 1 am avut nota " + str(max1) + " la materia " + str(
            materi1) + ", in semestrul 2 am avut nota " + str(max2) + " la " + str(materi2) + ", in semestrul 3 " + str(
            max3) + " la " + str(materi3) + "iar in semestrul 4 " + str(max4) + " la " + str(materi4))
        pass
    elif message == "_CEAMAIMARENOTADINFIECARESEMESTRU_":
        max1= -10
        max2= -10
        max3= -10
        max4= -10
        materi1 = None
        materi2 = None
        materi3 = None
        materi4 = None

        for materie,semestru in materii_semestru.items():
            if semestru is 1:
                if materii2note[materie]> max1:
                    max1 = materii2note[materie]
                    materi1 = materie
            elif semestru is 2:
                if materii2note[materie] > max2:
                    max2 = materii2note[materie]
                    materi2 = materie
            elif semestru is 3:
                if materii2note[materie] > max3:
                    max3 = materii2note[materie]
                    materi3 = materie
            elif semestru is 4:
                if materii2note[materie] > max4:
                    max4 = materii2note[materie]
                    materi4 = materie
        print("In semestrul 1 am avut nota " + str(max1) + " la materia " + str(
            materi1) + ", in semestrul 2 am avut nota " + str(max2) + " la " + str(materi2) + ", in semestrul 3 " + str(
            max3) + " la " + str(materi3) + "iar in semestrul 4 " + str(max4) + " la " + str(materi4))
        pass
    elif message == "_CEAMAIMICANOTADINFIECAREAN_":
        max1 = 11
        max2 = 11
        materie1 = None
        materie2 = None
        for materie,an in materii_an.items():
            if an is 1:
                if materii2note[materie]<max1:
                    max1 = materii2note[materie]
                    materie1 = materie
            else:
                if materii2note[materie]<max2:
                    max2= materii2note[materie]
                    materie2 = materie
        print("In primul an am luat "+str(max1)+" la "+str(materie1)+" iar in anul 2 "+str(max2)+" la "+str(materie2))
        pass
    elif message == "_CEAMAIMARENOTADINFIECAREAN_":
        max1 = -11
        max2 = -11
        materie1 = None
        materie2 = None
        for materie, an in materii_an.items():
            if an is 1:
                if materii2note[materie] >max1:
                    max1 = materii2note[materie]
                    materie1 = materie
            else:
                if materii2note[materie] > max2:
                    max2 = materii2note[materie]
                    materie2 = materie
        print(
            "In primul an am luat " + str(max1) + " la " + str(materie1) + " iar in anul 2 " + str(max2) + " la " + str(
                materie2))
        pass

def worstbestobject(message):
    message.upper()
    if message == "_MATERIACUNOTACEAMAIMICADINFIECAREAN_":
        materia1 = None
        materia2 = None

        max1 = 11
        max2 = 11
        for materie,an in materii_an.items():
            if an is 1:
                if materii2note[materie]<max1:
                    max1 = materii2note[materie]
                    materia1 = materie
            else:
                if materii2note[materie]<max2:
                    max2 = materii2note[materie]
                    materia2 = materie
        print ("Am avut "+str(max1)+" la "+str(materia1)+" in primul an"+" iar in anul 2 "+str(max2)+" la "+str(materia2))
        pass
    elif message == "_MATERIACUNOTACEAMAIMAREDINFIECAREAN_":
        materia1 = None
        materia2 = None

        max1 = 11
        max2 = 11
        for materie, an in materii_an.items():
            if an is 1:
                if materii2note[materie] > max1:
                    max1 = materii2note[materie]
                    materia1 = materie
            else:
                if materii2note[materie] > max2:
                    max2 = materii2note[materie]
                    materia2 = materie
        print("Am avut " + str(max1) + " la " + str(materia1) + " in primul an" + " iar in anul 2 " + str(
            max2) + " la " + str(materia2))
        pass
    elif message == "_MATERIACUNOTACEAMAIMICADINFIECARESEMESTRU_":
        max1 = 11
        max2 = 11
        max3 = 11
        max4 = 11
        materi1 = None
        materi2 = None
        materi3 = None
        materi4 = None

        for materie, semestru in materii_semestru.items():
            if semestru is 1:
                if materii2note[materie] < max1:
                    max1 = materii2note[materie]
                    materi1 = materie
            elif semestru is 2:
                if materii2note[materie] < max2:
                    max2 = materii2note[materie]
                    materi2 = materie
            elif semestru is 3:
                if materii2note[materie] < max3:
                    max3 = materii2note[materie]
                    materi3 = materie
            elif semestru is 4:
                if materii2note[materie] < max4:
                    max4 = materii2note[materie]
                    materi4 = materie
        print("In semestrul 1 am avut nota " + str(max1) + " la materia " + str(
            materi1) + ", in semestrul 2 am avut nota " + str(max2) + " la " + str(materi2) + ", in semestrul 3 " + str(
            max3) + " la " + str(materi3) + "iar in semestrul 4 " + str(max4) + " la " + str(materi4))
        pass
        pass
    elif message == "_MATERIACUNOTACEAMAIMAREDINFIECARESEMESTRU_":
        max1 = -10
        max2 = -10
        max3 = -10
        max4 = -10
        materi1 = None
        materi2 = None
        materi3 = None
        materi4 = None

        for materie, semestru in materii_semestru.items():
            if semestru is 1:
                if materii2note[materie] > max1:
                    max1 = materii2note[materie]
                    materi1 = materie
            elif semestru is 2:
                if materii2note[materie] > max2:
                    max2 = materii2note[materie]
                    materi2 = materie
            elif semestru is 3:
                if materii2note[materie] > max3:
                    max3 = materii2note[materie]
                    materi3 = materie
            elif semestru is 4:
                if materii2note[materie] > max4:
                    max4 = materii2note[materie]
                    materi4 = materie
        print("In semestrul 1 am avut nota " + str(max1) + " la materia " + str(
            materi1) + ", in semestrul 2 am avut nota " + str(max2) + " la " + str(materi2) + ", in semestrul 3 " + str(
            max3) + " la " + str(materi3) + "iar in semestrul 4 " + str(max4) + " la " + str(materi4))
        pass

def processSentence(sentence):
    mistakesFile = open("mistakes.dict",'r')
    mistakes = ast.literal_eval(mistakesFile.readline())

    correctFile = open("correct.dict",'r')
    correct = ast.literal_eval(correctFile.readline())

    mistakesFile.close()
    correctFile.close()

    words = re.split('\s,|\s\\.|\s',sentence)
    print("WORDS "+str(words))
    finalSentence = ""
    for word in words:
        word = word.upper()
        print("WORD:"+word)
        if word not in correct:
            if word not in mistakes.keys():
                print("What did you mean by "+str(word)+"?")
                rsp = input("Please type one word :) >>>")
                rsp_split = re.split('\s,|\s\\.|\s',rsp)
                if len(rsp_split) > 1 or rsp_split[0] is '' :
                    while len(rsp_split) is not 1:
                        print("You did not type one word!")
                        rsp = input("Please type one word :) >>>")
                        rsp_split = re.split('\s,|\s\\.|\s', rsp)
                print("Was that a mistake?")
                resp = input("Yes/No ")
                resp = resp.upper()

                if resp == "YES":
                    mistakes[word] = rsp[:]
                elif resp == "NO":
                    pass
                else:
                    while resp !="YES" or resp !="NO":
                        resp = input("Yes/No ")
                        resp = resp.upper()

                        if resp =="YES":
                            mistakes[word]=rsp[:].upper()
                        elif resp == "NO":
                           pass

                correct.append(rsp[:].upper())
                word = rsp
            else:
                word = mistakes[word]
        finalSentence = finalSentence+" "+word
        finalSentence = finalSentence.upper()


    mistakesFile = open("mistakes.dict", 'w')
    mistakesFile.write(str(mistakes))
    mistakesFile.close()

    correctFile = open("correct.dict", 'w')
    correctFile.write(str(correct))
    correctFile.close()

    return finalSentence

# def learnName(message):
#     message.upper()
#     regex = re.compile("^(Sunt)\\ \\w")
#
#     print(regex.search(message))





def main():
    kernel.learn("botlogic.xml")
    file = open("mistakes.dict","r+")
    r = file.readline()
    d = ast.literal_eval(r)
    print(d.keys())
    file.close()

    while True:
        internalResponse =False

        message = input("Message >>> ")
        message = processSentence(message)
        response = kernel.respond(message)
        response = response.upper()

        print("response: "+response)

        if response == "_INTEGRALIST_":
            calculateIntegralist()
            internalResponse=True
        elif response == "_RESTANTEANI_":
            calculateAniRestante()
            internalResponse=True
        elif response == "_RESTANTESEM_":
            calculateRestanteSem()
            internalResponse=True
        elif response == "_MATERIIPREFERATE_":
            materiiPreferate()
            internalResponse=True
        elif response == "_MATERIIANCURENT_":
            materiiAnCurent()
            internalResponse=True
        elif response == "_ENUMERARERESTANTE_":
            enumerareRestante()
            internalResponse=True
        elif response.upper() == "_CEAMAIMICANOTADINFIECARESEMESTRU_" or response == "_CEAMAIMARENOTADINFIECARESEMESTRU_" or response == "_CEAMAIMICANOTADINFIECARESAN_" or response == "_CEAMAIMARENOTADINFIECAREAN_":
            worstbestgrade(response)
        elif response == "_MATERIACUNOTACEAMAIMICADINFIECAREAN_" or response == "_MATERIACUNOTACEAMAIMAREDINFIECAREAN_" or response == "_MATERIACUNOTACEAMAIMICADINFIECARESEMESTRU_"  or response == "_MATERIACUNOTACEAMAIMAREDINFIECARESEMESTRU_":
            worstbestobject(response)

        if not internalResponse:
            print()

if __name__ == "__main__":
    main()