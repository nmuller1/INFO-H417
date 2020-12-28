import mmap

from src.streamCharacter import StreamCharacter
from src.streamBuffer import StreamBuffer
from src.streamLine import StreamLine
from src.streamMapping import StreamMapping
from src.modifiableCycle import ModifiableCycle
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
    writeStream.create()
    for line in text:
        writeStream.writeln(line)
    writeStream.close()

if __name__ == "__main__":
    files = ["imdb/comp_cast_type.csv", "imdb/movie_link.csv", "imdb/aka_title.csv", "imdb/name.csv",
           "imdb/cast_info.csv"]
    B = 1 * mmap.ALLOCATIONGRANULARITY
    readFilename = "imdb/movie_link.csv"
    readStreams = [StreamCharacter(readFilename), StreamLine(readFilename),
                   StreamBuffer(readFilename, B), StreamMapping(readFilename, B)]
    #for i in range(4):
        #print(readStreams[i].length())

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