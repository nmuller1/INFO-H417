from streamCharacter import StreamCharacter
text = ["Ceci est","un test","pour le cours","d'INFO-H417"]

if __name__ == "__main__":
    #Reading
    readFilename = "test.txt"
    readStream = StreamCharacter(readFilename)
    readStream.open()
    readStream.seek(0)
    while not readStream.end_of_stream():
        readStream.readln()
    readStream.close()

    #Writing
    writeFilename = "scratch.txt"
    writeStream = StreamCharacter(writeFilename)
    writeStream.create()
    for line in text:
        writeStream.writeln(line)
    writeStream.close()

