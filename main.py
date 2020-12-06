from streamCharacter import StreamCharacter
from streamBuffer import StreamBuffer
from streamLine import StreamLine
from streamMapping import StreamMapping
import os
import random

def length(f):
    """
    Sequential reading
    @param f: csv file to read
    @return: sum of the length of each line
    """
    stream = StreamBuffer(f, 3)
    stream.open()
    sum = 0
    while not stream.end_of_stream():
        sum += len(stream.readln())
    return sum

def randomjump(f,j):
    stream = StreamBuffer(f, 3)
    stream.open()
    sum = 0
    length = len(stream.file.read())
    for i in range(j):
        p = random.randint(0, length)
        stream.seek(p)
        line =stream.readln()
        sum += len(line)
    print(sum)
    return(sum)

def testReadStream(stream):
    stream.open()
    stream.seek(0)
    while not stream.end_of_stream():
        print(stream.readln())
    stream.close()


def testWriteStream(stream):
    writeStream.create()
    for line in text:
        writeStream.writeln(line)
    writeStream.close()

if __name__ == "__main__":
    readFilename = "test.txt"
    readStream = StreamBuffer(readFilename, 7)
    #testReadStream(readStream)

    text = ["Ceci est", "un test", "pour le cours", "d'INFO-H417"]

    if os.path.exists("scratch.txt"):
        os.remove("scratch.txt")
    writeFilename = "scratch.txt"
    writeStream = StreamBuffer(writeFilename,3)
    #testWriteStream(writeStream)
    print(length(readFilename))
    #randomjump(readFilename, 3)
