from streamCharacter import StreamCharacter
from streamBuffer import StreamBuffer
from streamLine import StreamLine
from streamMapping import StreamMapping
from modifiableCycle import ModifiableCycle
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
        stream.readln()
    stream.close()


def testWriteStream(writeStream):
    writeStream.create()
    for line in text:
        writeStream.writeln(line)
    writeStream.close()
    
    
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

if __name__ == "__main__":
    readFilename = "test.txt"
    readStream = StreamMapping(readFilename, 1)
    testReadStream(readStream)

    text = ["Ceci est", "un test", "pour le cours", "d'INFO-H417"]

    if os.path.exists("scratch.txt"):
        os.remove("scratch.txt")
    writeFilename = "scratch.txt"
    writeStream = StreamMapping(writeFilename, 1)
    testWriteStream(writeStream)
    print(length(readFilename))
    randomjump(readFilename, 3)
    rrmerge(1,1,"test1.txt","foo.txt","be.txt","scratch.txt")
