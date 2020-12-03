from streamCharacter import StreamCharacter
from streamBuffer import StreamBuffer

import os

text = ["Ceci est", "un test", "pour le cours", "d'INFO-H417"]

if __name__ == "__main__":
    # Reading
    readFilename = "test.txt"
    readStream = StreamBuffer(readFilename, 1)
    readStream.open()
    readStream.seek(0)
    while not readStream.end_of_stream():
        readStream.readln()
    readStream.close()

    # Writing
    if os.path.exists("scratch.txt"):
        os.remove("scratch.txt")
    writeFilename = "scratch.txt"
    writeStream = StreamCharacter(writeFilename)
    writeStream.create()
    for line in text:
        writeStream.writeln(line)
    writeStream.close()
