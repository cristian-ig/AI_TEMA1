import aiml
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
# def learnName(message):
#     message.upper()
#     regex = re.compile("^(Sunt)\\ \\w")
#
#     print(regex.search(message))





kernel.learn("botlogic.xml")

while True:
    internalResponse =False

    message = input("Message >>> ")
    response = kernel.respond(message)
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

    if not internalResponse:
        print()
