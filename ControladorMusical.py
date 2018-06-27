from midiutil import MIDIFile

degrees = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track = 0
channel = 0
time = 0  # In beats
duration = 1  # In beats
tempo = 60  # In BPM
volume = 100  # 0-127, as per the MIDI standard

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

arregloC = [c,d,e,f,g,a,b]
arregloNotas = []
arregloOctavas = []
arregloRitmos = []
arregloVelocidades = []
arregloVolumenes = []
arregloGrados = []
arregloValores = []
arregloDuraciones = []


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
def augmented(note, where, midi):
    global count
    tonic = note
    mediant = note+4
    dominant = note+8
    list = [tonic, mediant, dominant]

    # add some notes
    channel = 0
    volume = 100
    pitch = list[0]  # C4 (middle C)
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[1]  # E4
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[2]  # G4
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)
    return

#método que construye un grado si es disminuido
def diminished(note, where, midi):
    global count
    tonic = note
    mediant = note+3
    dominant = note+6
    list = [tonic, mediant, dominant]

    # add some notes
    channel = 0
    volume = 100
    pitch = list[0]  # C4 (middle C)
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[1]  # E4
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    midi.addNote(track, channel, pitch, time, duration, volume)

    pitch = list[2]  # G4
    count = where  # start on beat 4
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

def construirProgresion():
    global primerAcorde
    from random import randint
    if (randint(0, 2) == 0):
        primerAcorde = "5M"
    else:
        primerAcorde = "1M"
    print(primerAcorde)




MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
MyMIDI.addTempo(track, time, tempo)

minor6(c, 0, MyMIDI)
construirProgresion()

with open("aa.mid", 'wb') as output_file:
    try:
        MyMIDI.writeFile(output_file)
    finally:
        output_file.close()

#for i, pitch in enumerate(degrees):
    #MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

#with open("a.mid", "wb") as output_file:
    #MyMIDI.writeFile(output_file)
    #MyMIDI.close()



# GRADOS SIGUIENTES
# sig1 = [1,2,3,4,5,6,7] #grados siguientes del 1er grado
# sig2 = [1,2,5,6] #grados siguientes del 2do grado
# sig3 = [3,6,4,7] #grados siguientes del 3er grado
# sig4 = [1,4,5,7,6,2] #grados siguientes del 4to grado
# sig5 = [1,5,6,2,4] #grados siguientes del 5to grado
# sig6 = [6,2,5,4,7] #grados siguientes del 6to grado
# sig7 = [1,2,4,5,6] #grados siguientes del 7mo grado
#
# Variables
# progresion = []
#
# mf = MIDIFile(1)  # only 1 track
