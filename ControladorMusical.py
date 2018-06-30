from midiutil import MIDIFile
import random

degrees = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track = 0
channel = 0
time = 0  # In beats
duration = 1  # In beats
tempo = 60  # In BPM
volume = 100  # 0-127, as per the MIDI standard
pos = 0

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
sig1M = ["3m", "3bM", "5M", "6m", "7d"] #grados siguientes del 1er grado Mayor
sig4M = ["5M", "7d"] #grados siguientes del 4to grado Mayor
sig5M = ["1M", "3bM", "6m", "6bM", "7bM"] #grados siguientes del 5to grado Mayor
sig6m = ["2m", "2M", "5M", "4M"] #grados siguientes del 6to grado menor
sig2m = ["1M", "5M", "6m"] #grados siguientes del 2do grado menor
sig2M = ["1M", "4M", "5M"] #grados siguientes del 2do grado Mayor
sig7bM = ["1M"] #grados siguientes del 7mo grado bemol Mayor
sig3m = ["1", "6m"] #grados siguientes del 3er grado menor
sig4m = ["1M", "5M"] #grados siguientes del 4to grado menor
sig3bM = ["1M", "4M", "5M", "7bM"] #grados siguientes del 3er grado bemol Mayor
sig6M = ["2m", "5M", "4M"] #grados siguientes del 6to grado Mayor
sig6bM = ["5M", "4M", "7bM"] #grados siguientes del 6to grado bemol Mayor
sig3M = ["6m", "4M", "7d"] #grados siguientes del 3er grado Mayor
sig5m = ["1M"] #grados siguientes del 5to grado menor
sig7d = ["1M", "2m", "4M", "5M", "6m", "6bM"] #grados siguientes del 7mo grado disminuido

#sig1 = ["2m", "3m", "4M", "5M", "6m", "7d"] #grados siguientes del 1er grado
#sig2 = ["1M", "5M", "6m"] #grados siguientes del 2do grado
#sig3 = ["6m", "4M", "7d"] #grados siguientes del 3er grado
#sig4 = ["1M", "5M", "7d", "6m", "2m"] #grados siguientes del 4to grado
#sig5 = ["1M", "6m", "2m", "4M"] #grados siguientes del 5to grado
#sig6 = ["2m", "5M", "4M", "7d"] #grados siguientes del 6to grado
#sig7 = ["1M", "2m", "4M", "5M", "6m"] #grados siguientes del 7mo grado

arregloC = [c, d, e, f, g, a, b]
progresion = []


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

#método que construye un grado si es menor
def minor(note, where, midi):
    global time
    tonic = note
    mediant = note+3
    dominant = note+7
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

#método que construye un grado si es aumentado
def Augmented(note, where, midi):
    global time
    tonic = note
    mediant = note+4
    dominant = note+8
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

#método que construye un grado si es disminuido
def diminished(note, where, midi):
    global time
    tonic = note
    mediant = note+3
    dominant = note+6
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

#método que construye un grado si es menor
def minor7(note, where, midi):
    global time
    tonic = note
    mediant = note+3
    dominant = note+7
    seventh = dominant + 3
    list = [tonic, mediant, dominant, seventh]
    #random.shuffle(beats)

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
    tonic = note + 12 # una 8va arriba
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

#método que construye un acorde menor en 1era inversion
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

def tipoAcorde(chord, midi):
    global pos
    if (chord[1] == "M"):
        numero = int(chord[0])-1
        notaEncontrada = arregloC[numero]
        Major(notaEncontrada, pos, midi)
    elif (chord[1] == "m"):
        numero = int(chord[0])-1
        notaEncontrada = arregloC[numero]
        minor(notaEncontrada, pos, midi)
    elif (chord[1] == "A"):
        numero = int(chord[0])-1
        notaEncontrada = arregloC[numero]
        Augmented(notaEncontrada, pos, midi)
    elif (chord[1] == "d"):
        numero = int(chord[0])-1
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

def construirProgresion(midi):
    global pos
    acorde = ""
    from random import randint
    if (randint(0, 3) == 0):
        acorde = "5M"
        Major(g, pos, midi)
    elif (randint(0, 3) == 1):
        acorde = "6m"
        minor(a, pos, midi)
    else:
        acorde = "1M"
        Major(c, pos, midi)
    pos += 1
    progresion.append(acorde)

    while(len(progresion) < 6):
        if (acorde == "1M"):
            acorde = random.choice(sig1M)
        elif (acorde == "2m"):
            acorde = random.choice(sig2m)
        elif (acorde == "2M"):
            acorde = random.choice(sig2M)
        elif (acorde == "3m"):
            acorde = random.choice(sig3m)
        elif (acorde == "3M"):
            acorde = random.choice(sig3M)
        elif (acorde == "3bM"):
            acorde = random.choice(sig3bM)
        elif (acorde == "4m"):
            acorde = random.choice(sig4m)
        elif (acorde == "4M"):
            acorde = random.choice(sig4M)
        elif (acorde == "5m"):
            acorde = random.choice(sig5m)
        elif (acorde == "5M"):
            acorde = random.choice(sig5M)
        elif (acorde == "6m"):
            acorde = random.choice(sig6m)
        elif (acorde == "6M"):
            acorde = random.choice(sig6M)
        elif (acorde == "6bM"):
            acorde = random.choice(sig6bM)
        elif (acorde == "7d"):
            acorde = random.choice(sig7d)
        elif (acorde == "7bM"):
            acorde = random.choice(sig7bM)
        tipoAcorde(acorde, midi)
        progresion.append(acorde)

def leerProgresion(midi):
    global pos
    global progresion
    for i in progresion:
        tipoAcorde(i, midi)


MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
MyMIDI.addTempo(track, time, tempo)

construirProgresion(MyMIDI)
#progresion = ["1M", "4m", "7d", "5M", "4M", "7d"]
#leerProgresion(MyMIDI)
print('[%s]' % ', '.join(map(str, progresion)))

with open("zn.mid", 'wb') as output_file:
    try:
        MyMIDI.writeFile(output_file)
    finally:
        output_file.close()#

# Variables
# progresion = []
#
# mf = MIDIFile(1)  # only 1 track
