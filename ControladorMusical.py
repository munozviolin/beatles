import random

from midiutil import MIDIFile

MidiFinal = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
degrees = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track = 0
channel = 0
time = 0  # In beats
duration = 1  # In beats
tempo = 60  # In BPM
volume = 100  # 0-127, as per the MIDI standard
pos = 0
fitness = 0
j = 0

# NOTAS
aBem = 56  # Bem = bemol
a = 57
aSus = 58  # Sus = sostenido
bBem = 58
b = 59
cBem = 59
bSus = 60
c = 60
cSus = 61
dBem = 61
d = 62
dSus = 63
eBem = 63
e = 64
fBem = 64
eSus = 65
f = 65
fSus = 66
gBem = 66
g = 67
gSus = 68

# GRADOS SIGUIENTES
sig1M = ["3m", "3bM", "5M", "6m", "7d"]  # grados siguientes del 1er grado Mayor
sig4M = ["5M", "7d"]  # grados siguientes del 4to grado Mayor
sig5M = ["1M", "3bM", "6m", "6bM", "7bM"]  # grados siguientes del 5to grado Mayor
sig6m = ["2m", "2M", "5M", "4M"]  # grados siguientes del 6to grado menor
sig2m = ["1M", "5M", "6m"]  # grados siguientes del 2do grado menor
sig2M = ["1M", "4M", "5M"]  # grados siguientes del 2do grado Mayor
sig7bM = ["1M"]  # grados siguientes del 7mo grado bemol Mayor
sig3m = ["1M", "6m"]  # grados siguientes del 3er grado menor
sig4m = ["1M", "5M"]  # grados siguientes del 4to grado menor
sig3bM = ["1M", "4M", "5M", "7bM"]  # grados siguientes del 3er grado bemol Mayor
sig6M = ["2m", "5M", "4M"]  # grados siguientes del 6to grado Mayor
sig6bM = ["5M", "4M", "7bM"]  # grados siguientes del 6to grado bemol Mayor
sig3M = ["6m", "4M", "7d"]  # grados siguientes del 3er grado Mayor
sig5m = ["1M"]  # grados siguientes del 5to grado menor
sig7d = ["1M", "2m", "4M", "5M", "6m", "6bM"]  # grados siguientes del 7mo grado disminuido
gradosPosibles = ["1M", "4M", "5M", "6m", "2m", "2M", "7bM", "3m", "4m", "3bM", "6M", "6bM", "3M", "5m",
                  "7d"]  # grados posibles en la progresion

arregloC = [c, d, e, f, g, a, b]  # notas basicas de la tonalidad Do Mayor
progresion = []  # cada individuo de la poblacion inicial
progresiones = []  # lista de progresiones que representan la poblacion inicial
fitnessProgresiones = []  # lista con el fitness de cada progresion de la poblacion inicial
fitnessProgresionesHijas = []  # lista con el fitness de cada progresion de la poblacion final
progresionesMasAptas = []  # lista de progresiones con mayor aptitud
progresionesPadres = []  # lista de progresiones que se reproducirán
progresionesHijas = []
progresionesHijas2 = []


# método que construye un grado si es Mayor
def Major(note, where, midi):
    global time
    tonic = note
    mediant = note + 4
    dominant = note + 7
    list = [tonic, mediant, dominant]

    # add some notes
    pitch = list[0]  # C4 (middle C)
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[1]  # E4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[2]  # G4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)
    return


# método que construye un grado si es menor
def minor(note, where, midi):
    global time
    tonic = note
    mediant = note + 3
    dominant = note + 7
    list = [tonic, mediant, dominant]

    # add some notes
    channel = 0
    volume = 100
    pitch = list[0]  # C4 (middle C)
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[1]  # E4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[2]  # G4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)
    return


# método que construye un grado si es aumentado
def Augmented(note, where, midi):
    global time
    tonic = note
    mediant = note + 4
    dominant = note + 8
    list = [tonic, mediant, dominant]

    # add some notes
    channel = 0
    volume = 100
    pitch = list[0]  # C4 (middle C)
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[1]  # E4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[2]  # G4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)
    return


# método que construye un grado si es disminuido
def diminished(note, where, midi):
    global time
    tonic = note
    mediant = note + 3
    dominant = note + 6
    list = [tonic, mediant, dominant]

    # add some notes
    channel = 0
    volume = 100
    pitch = list[0]  # C4 (middle C)
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[1]  # E4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[2]  # G4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)
    return


# método que construye un acorde de sexta bemol (el parametro pasado es tonica de la tonalidad)
def flatSix(note, where, midi):
    global time
    tonic = note - 4
    mediant = tonic + 4
    dominant = tonic + 7
    list = [tonic, mediant, dominant]

    # add some notes
    pitch = list[0]  # C4 (middle C)
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[1]  # E4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[2]  # G4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)
    return


# método que construye un acorde de septima bemol (el parametro pasado es tonica de la tonalidad)
def flatSeven(note, where, midi):
    global time
    tonic = note - 2
    mediant = tonic + 4
    dominant = tonic + 7
    list = [tonic, mediant, dominant]

    # add some notes
    pitch = list[0]  # C4 (middle C)
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[1]  # E4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[2]  # G4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)
    return


# método que construye un acorde de septima bemol (el parametro pasado es tonica de la tonalidad)
def flatThree(note, where, midi):
    global time
    tonic = note + 3
    mediant = tonic + 4
    dominant = tonic + 7
    list = [tonic, mediant, dominant]

    # add some notes
    pitch = list[0]  # C4 (middle C)
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[1]  # E4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[2]  # G4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)
    return


# método que construye un grado si es Mayor
def Major7(note, where, midi):
    global time
    tonic = note
    mediant = note + 4
    dominant = note + 7
    seventh = dominant + 3
    list = [tonic, mediant, dominant, seventh]

    # add some notes
    pitch = list[0]  # C4 (middle C)
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[1]  # E4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[2]  # G4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[3]  # G4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)
    return


# método que construye un grado si es menor
def minor7(note, where, midi):
    global time
    tonic = note
    mediant = note + 3
    dominant = note + 7
    seventh = dominant + 3
    list = [tonic, mediant, dominant, seventh]
    # random.shuffle(beats)

    # add some notes
    channel = 0
    volume = 100
    pitch = list[0]  # C4 (middle C)
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[1]  # E4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[2]  # G4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[3]  # G4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)
    return


# método que construye un acorde Mayor en 1era inversion
def Major6(note, where, midi):
    global time
    tonic = note + 12  # una 8va arriba
    mediant = note + 4
    dominant = note + 7
    list = [tonic, mediant, dominant]

    # add some notes
    pitch = list[0]  # C4 (middle C)
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[1]  # E4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[2]  # G4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)
    return


# método que construye un acorde menor en 1era inversion
def minor6(note, where, midi):
    global time
    tonic = note + 12
    mediant = note + 3
    dominant = note + 7
    list = [tonic, mediant, dominant]

    # add some notes
    channel = 0
    volume = 100
    pitch = list[0]  # C4 (middle C)
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[1]  # E4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[2]  # G4
    time = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)
    return

def tipoAcorde(chord, midi, tieneSetima):
    global pos
    if (chord[1] == "M"):
        numero = int(chord[0]) - 1
        notaEncontrada = arregloC[numero]
        if (tieneSetima == 1):
            Major7(notaEncontrada, pos, midi)
        else:
            Major(notaEncontrada, pos, midi)
    elif (chord[1] == "m"):
        numero = int(chord[0]) - 1
        notaEncontrada = arregloC[numero]
        if (tieneSetima == 0):
            minor7(notaEncontrada, pos, midi)
        else:
            minor(notaEncontrada, pos, midi)
    elif (chord[1] == "A"):
        numero = int(chord[0]) - 1
        notaEncontrada = arregloC[numero]
        Augmented(notaEncontrada, pos, midi)
    elif (chord[1] == "d"):
        numero = int(chord[0]) - 1
        notaEncontrada = arregloC[numero]
        diminished(notaEncontrada, pos, midi)
    elif (chord[1] == "b"):
        numero = int(chord[0])
        if (numero == 3):
            flatThree(c, pos, midi)
        elif (numero == 6):
            flatSix(c, pos, midi)
        elif (numero == 7):
            flatSeven(c, pos, midi)
    pos += 1


#def construirProgresion(midi, progresion):
def construirProgresion(progresion):
    global progresiones
    global pos
    acorde = ""
    from random import randint
    if (randint(0, 3) == 0):
        acorde = "5M"
        #Major(g, pos, midi)
    elif (randint(0, 3) == 1):
        acorde = "6m"
        #minor(a, pos, midi)
    else:
        acorde = "1M"
        #Major(c, pos, midi)
    pos += 1
    progresion.append(acorde)

    while (len(progresion) < 5):
        if (acorde == "1M" or acorde == "1M7"):
            acorde = random.choice(sig1M)
        elif (acorde == "2m" or acorde == "2m7"):
            acorde = random.choice(sig2m)
        elif (acorde == "2M" or acorde == "2M7"):
            acorde = random.choice(sig2M)
        elif (acorde == "3m" or acorde == "3m7"):
            acorde = random.choice(sig3m)
        elif (acorde == "3M" or acorde == "3M7"):
            acorde = random.choice(sig3M)
        elif (acorde == "3bM"):
            acorde = random.choice(sig3bM)
        elif (acorde == "4m" or acorde == "4m7"):
            acorde = random.choice(sig4m)
        elif (acorde == "4M" or acorde == "4M7"):
            acorde = random.choice(sig4M)
        elif (acorde == "5m" or acorde == "5m7"):
            acorde = random.choice(sig5m)
        elif (acorde == "5M" or acorde == "5M7"):
            acorde = random.choice(sig5M)
        elif (acorde == "6m" or acorde == "6m7"):
            acorde = random.choice(sig6m)
        elif (acorde == "6M" or acorde == "6M7"):
            acorde = random.choice(sig6M)
        elif (acorde == "6bM"):
            acorde = random.choice(sig6bM)
        elif (acorde == "7d"):
            acorde = random.choice(sig7d)
        elif (acorde == "7bM"):
            acorde = random.choice(sig7bM)

        tamAcorde = len(acorde) - 1
        if acorde != "3bM" and acorde != "6bM" and acorde != "7bM" and (acorde[tamAcorde] == 'M') or (
                acorde[tamAcorde] == 'm'):
            if (random.randint(0, 2) == 0):
                acorde += '7'
                #tipoAcorde(acorde, midi, 1)  # tiene 7ma
            #else:
                #tipoAcorde(acorde, midi, 0)  # no tiene 7ma
        #else:
            #tipoAcorde(acorde, midi, 0)  # no tiene 7ma
        progresion.append(acorde)
    progresiones.append(progresion)
    # print('[%s]' % ', '.join(map(str, progresion)))


def leerProgresion(prog, midi):
    global pos
    pos = 0
    # global progresion
    for acorde in prog:
        tamAcorde = len(acorde) - 1
        if (acorde[tamAcorde] == "7"):
            tipoAcorde(acorde, midi, 1)
        else:
            tipoAcorde(acorde, midi, 0)


def generarProgresiones(cantidad):
    global pos
    global progresion
    global time
    i = 0
    while (i < cantidad):
        pos = 0
        time = 0
        progresion = []
        #MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
        ##MyMIDI.addTempo(track, time, tempo)
        construirProgresion(progresion)
        #construirProgresion(MyMIDI, progresion)
        i += 1

        #with open("zn.mid", 'wb') as output_file:
        #    try:
        #        MyMIDI.writeFile(output_file)
        #    finally:
        #        output_file.close()


def evaluarFitness(progresionesEval):
    global fitness
    for progr in progresionesEval:
        fitness = 0
        contadorPrimerosGrados = 0
        contadorGradosEspeciales = 0

        # cadencia
        ultimoAcorde = len(progr) - 1
        penultimoAcorde = ultimoAcorde - 1
        antepenultimoAcorde = penultimoAcorde - 1

        # cadencia terminada en I
        if (progr[ultimoAcorde] == "1M") and (progr[penultimoAcorde] == "7bM") and (
                (progr[antepenultimoAcorde] == "5M") or (progr[antepenultimoAcorde] == "5M7")):  # V-bVII-I
            fitness += 7
        elif (progr[ultimoAcorde] == "1M") and (
                (progr[penultimoAcorde] == "5M") or (progr[penultimoAcorde] == "5M7")) and (
                progr[antepenultimoAcorde] == "7bM"):  # bVII-V-I
            fitness += 7
        elif (progr[ultimoAcorde] == "1M") and (
                (progr[penultimoAcorde] == "5M") or (progr[penultimoAcorde] == "5M7")) and (
                progr[antepenultimoAcorde] == "2M"):  # II-V-I
            fitness += 5
        elif (progr[ultimoAcorde] == "1M") and (progr[penultimoAcorde] == "2M"):  # II-I
            fitness += 4
        elif (progr[ultimoAcorde] == "1M") and (progr[penultimoAcorde] == "6bM") and (
                (progr[antepenultimoAcorde] == "5M") or (progr[antepenultimoAcorde] == "5M7")):  # V-bVI-I
            fitness += 7
        # cadencia terminada en V
        elif (progr[ultimoAcorde] == "5M") or (progr[ultimoAcorde] == "5M7"):
            fitness += 15
        # cadencia terminada en VI
        elif progr[ultimoAcorde] == "6M":
            fitness += 20
        # cadencia terminada en vi
        elif progr[ultimoAcorde] == "6m":
            fitness += 30
        # cualquier otro caso
        else:
            fitness += 5

        # buscar que no empiece con 1er grado
        if (progr[0] != "1M") or (progr[0] != "1M7"):
            fitness += 10

        # buscador de primeros grados y grados especiales
        for chord in progr:
            if (chord == "1M") or (chord == "1M7"):
                contadorPrimerosGrados += 1
            if (chord == "6bM") or (chord == "4m") or (chord == "4m7") or (chord == "6M") or (chord == "6M7") or (chord == "7bM") or (chord == "5m") or (chord == "5m7") or (chord == "3bM"):
                contadorGradosEspeciales += 1

        # buscar que la progresion no tenga mas de un 1er grado
        if contadorPrimerosGrados <= 1:
            fitness += 10

        # depende de cuantos grados especiales tiene asi aumenta su fitness
        if contadorGradosEspeciales == 1:
            fitness += 25
        elif contadorGradosEspeciales == 2:
            fitness += 40

        fitnessProgresiones.append(fitness)
        if fitness >= 65:
            progresionesMasAptas.append(progr)


def cruzamiento(leido, escrito):
    # global progresionesMasAptas
    global progresionesPadres
    global progresiones
    global j
    progresionesPadres = []
    menosAptos = len(leido) * 0.3
    progresionesPadres = leido.copy()
    i = 0

    while i < menosAptos:
        aleatorio = random.randint(0, len(progresiones) - 1)
        progresionesPadres.append(progresiones[aleatorio])  # selecciona al azar algunas progresiones de la poblacion inicial no necesariamente tan leido, pero que contribuyen a la diversidad de la poblacion
        i += 1

    i = 0
    tam = len(progresionesPadres[0])
    # print(len(progresionesPadres))
    while i < len(progresionesPadres):
        progTemporal = []
        aleatorio = random.randint(0, len(progresionesPadres) - 1)
        progresionAleatoria = progresionesPadres[aleatorio]
        progresionI = progresionesPadres[i]
        if progresionI[1] == progresionAleatoria[1]:
            progTemporal.append(progresionAleatoria[0])
            progTemporal.append(progresionI[1])
            progTemporal.append(progresionI[2])
            progTemporal.append(progresionI[3])
            progTemporal.append(progresionI[4])
        elif progresionI[2] == progresionAleatoria[2]:
            progTemporal.append(progresionAleatoria[0])
            progTemporal.append(progresionAleatoria[1])
            progTemporal.append(progresionI[2])
            progTemporal.append(progresionI[3])
            progTemporal.append(progresionI[4])
        elif progresionI[3] == progresionAleatoria[3]:
            progTemporal.append(progresionI[0])
            progTemporal.append(progresionI[1])
            progTemporal.append(progresionI[2])
            progTemporal.append(progresionAleatoria[3])
            progTemporal.append(progresionAleatoria[4])
        else:
            progTemporal = progresionI.copy()  #

        # mutacion con probabilidad de 0.1
        if random.randint(1, 100) == 1:
            progTemporal[tam - 1] = random.choice(gradosPosibles)
        escrito.append(progTemporal)
        i += 1

    j += 1
    if (j <= 30):
        escrito2 = []
        cruzamiento(escrito, escrito2)
        # escrito = escrito2.copy()
        # j += 1

generarProgresiones(100)
#try:
#    os.remove("zn.mid")
#except OSError:
#    pass

# print('[%s]' % '\n'.join(map(str, progresiones)))
evaluarFitness(progresiones)
print("primera generacion: ", max(fitnessProgresiones))

cruzamiento(progresionesMasAptas, progresionesHijas)
# print('[%s]' % '\n'.join(map(str, progresionesHijas)))

print("__________________________________________________________________________")

fitnessProgresiones = []

evaluarFitness(progresionesHijas)
masApto = max(fitnessProgresiones)
indexMasApto = fitnessProgresiones.index(masApto)
progresionGanadora = progresionesHijas[indexMasApto]
print("segunda generacion: ", masApto)
print("Progresion Ganadora 1: ", '[%s]' % ', '.join(map(str, progresionGanadora)))

progresionGanadora2 = progresionGanadora.copy()
while (progresionGanadora2 == progresionGanadora):
    fitnessProgresiones.remove(masApto)
    progresionesHijas.remove(progresionGanadora)
    masApto2 = max(fitnessProgresiones)
    indexMasApto2 = fitnessProgresiones.index(masApto2)
    progresionGanadora2 = progresionesHijas[indexMasApto2]
print("Progresion Ganadora 2: ", '[%s]' % ', '.join(map(str, progresionGanadora2)))

track = 0
time = 0
MidiFinal = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
MidiFinal.addTempo(track, time, tempo)

leerProgresion(progresionGanadora, MidiFinal)

with open("progresionA.mid", 'wb') as outputf:
    try:
        MidiFinal.writeFile(outputf)
    finally:
        outputf.close()