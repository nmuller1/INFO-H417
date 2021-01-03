import mmap

from streamCharacter import StreamCharacter
from streamBuffer import StreamBuffer
from streamLine import StreamLine
from streamMapping import StreamMapping
from modifiableCycle import ModifiableCycle
import os
import time
import random

def rrmerge(numberStreamR,numberStreamW,filenameW,*files):
    templist = []
    if numberStreamR == 0 :
        
         for f in files:
             temp = StreamCharacter(f)
             temp.open()
             templist.append(temp)
             
    if numberStreamR == 1 :
        
         for f in files:
             temp = StreamBuffer(f,3)
             temp.open()
             templist.append(temp)

    if numberStreamR == 2 :
        
         for f in files:
             temp = StreamLine(f)
             temp.open()
             templist.append(temp)

             
    """if numberStreamR == 3 :
        
         for f in files:
             temp = StreamMap(f)
             temp.open()
             templist.append(temp)"""
        
    listfiles = ModifiableCycle(templist)
    
    
    if numberStreamW == 0 :  
        #"StreamCharachter"
        output_stream = StreamCharacter(filenameW)
        
        
    if numberStreamW == 1 :
        #"StreamBuffer"
        output_stream = StreamBuffer(filenameW,3)
        
    if numberStreamW == 2 :
        #"StreamLine"
        output_stream = StreamLine(filenameW)
        
             
    """if numberStreamW == 3 :
        #"StreamMap"
        output_stream = StreamMap(filenameW)"""


    output_stream.create()

    for f in listfiles:
        #f.seek(0) obligatoire ?
        line = f.readln()
        output_stream.writeln(line)
        if line == "":
            
            listfiles.delete_prev()
            f.close()


def testReadStream(stream):
    """
    Test the read method of a stream
    @param stream:
    @return:
    """
    stream.open()
    stream.seek(0)
    while not stream.end_of_stream():
        print(stream.readln())
    stream.close()

def testWriteStream(writeStream):
    text = ["Ceci est", "un test", "pour le cours", "d'INFO-H417"]
    writeStream.create()
    for line in text:
        writeStream.writeln(line)
    writeStream.close()

def length1(f):
    sum = 0
    for i in range(10):
        readStream = StreamCharacter(f)
        sum += readStream.length()[1]
    sum /= 10
    return sum

def length2(f):
    sum = 0
    for i in range(10):
        readStream = StreamLine(f)
        sum += readStream.length()[1]
    sum /= 10
    return sum

def length3(f,B):
    sum = 0
    for i in range(10):
        readStream = StreamBuffer(f,B)
        sum += readStream.length()[1]
    sum /= 10
    return sum

def length4(f,B):
    sum = 0
    for i in range(10):
        readStream = StreamMapping(f,B)
        sum += readStream.length()[1]
    sum /= 10
    return sum

def random1(f):
    sum = 0
    for i in range(10):
        readStream = StreamCharacter(f)
        sum += readStream.randomjump(200)[1]
    sum /= 10
    return sum

def random2(f):
    sum = 0
    for i in range(10):
        readStream = StreamLine(f)
        sum += readStream.randomjump(200)[1]
    sum /= 10
    return sum

def random3(f,B):
    sum = 0
    for i in range(10):
        readStream = StreamBuffer(f,B)
        sum += readStream.randomjump(200)[1]
    sum /= 10
    return sum

if __name__ == "__main__":
    files = ["imdb/comp_cast_type.csv", "imdb/movie_link.csv", "imdb/aka_title.csv", "imdb/name.csv",
           "imdb/cast_info.csv"]
    B = 1 * mmap.ALLOCATIONGRANULARITY
    readFilename = "../testFiles/link_type.csv"
    readStreams = [StreamCharacter(readFilename), StreamLine(readFilename),
                   StreamBuffer(readFilename, B), StreamMapping(readFilename, B)]

    for i in range(4):
        print(readStreams[i].length())

    readStreams = [StreamCharacter(readFilename), StreamLine(readFilename),
                   StreamBuffer(readFilename, B), StreamMapping(readFilename, B)]

    for i in range(4):
        print(readStreams[i].randomjump(1))


"""
    text = ["Ceci est", "un test", "pour le cours", "d'INFO-H417"]

    if os.path.exists("../testFiles/scratch.txt"):
        os.remove("../testFiles/scratch.txt")
    writeFilename = "scratch.txt"
    writeStream = StreamMapping(writeFilename, 1)
    testWriteStream(writeStream)
    print(length(readFilename))
    randomjump(readFilename, 3)
    rrmerge(1,1,"test1.txt","foo.txt","be.txt","scratch.txt")
"""