import mmap
import os
from src.stream import Stream
import time
import random

class StreamMapping(Stream):
    """
    Implement readln and writeln by mapping and unmapping B characters of the file into internal memory through memory mapping.
    Whenever you need to read/write outside of the mapped portion, the next B element portion of the file is mapped.
    """

    def __init__(self, filename, mmapSize):
        Stream.__init__(self, filename)
        self.endofmap = False
        self.mmapSize = mmapSize
        self.count = 0
        
    def open(self):
        """
        Open an existing file for reading
        """
        self.file = open(self.filename, 'rb')
        self.size = os.stat(self.filename).st_size
        self.modulosize = self.size % self.mmapSize
        if self.size < self.mmapSize:
            self.mmapSize = self.size
        self.map = mmap.mmap(self.file.fileno(), length=self.mmapSize, offset=0, access=mmap.ACCESS_READ)

    def seek(self, pos):
        """
        Move the file cursor to pos so that a subsequent readln reads from position pos to the next end of line
        @param pos: position in the file where we want to move the cursor
        """
        self.file.seek(pos)
        self.count = pos//self.mmapSize

        seek = pos % self.mmapSize
        self.cleanMap()
        self.map = mmap.mmap(self.file.fileno(), length=self.mmapSize*self.count, offset=0, access=mmap.ACCESS_READ)
        self.map.read(seek)

    def create(self):
        """
        Open an existing file for reading
        """
        self.file = open(self.filename, 'wb')
        self.map = mmap.mmap(-1, length=self.mmapSize, access=mmap.ACCESS_WRITE)
    
    def close(self):
        """
        Close the stream
        """
        self.file.close()

    def readln(self):
        """
        Read the next line from the stream
        """
        char = " ".encode("latin-1")
        line = ""
        while not self.eof and char.decode("latin-1") != "\n":
            while not self.endOfReading():
                char = self.map.read(1)
                if char.decode("latin-1") == "\n":
                    break
                line += str(char.decode("latin-1"))
            if not self.endofmap and self.endOfReading():
                self.count += 1
                self.mapNextPortion()
            elif self.endofmap and self.endOfReading():
                self.eof = True
        return line

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        i = 0
        while i < len(string):
            while not self.endOfReading():
                self.map[i:i+1] = string[i].encode("latin-1")
                i += 1
                if i == len(string):
                    break
            self.file.write(self.map[0:i])
            self.cleanMap()
        self.file.write("\n".encode("latin-1"))

    def endOfReading(self):
        """
        Checks if the buffer is full
        @return: True if the buffer is full and False if not
        """
        return self.map.tell() == self.mmapSize

    def cleanMap(self):
        """
        Empty the buffer
        """
        self.map.flush()
    
    def mapNextPortion(self):
        """
        Empty the buffer
        """
        offset = self.mmapSize * self.count +1
        length = self.mmapSize
        if self.mmapSize * (self.count+1) >= self.size:
            length = self.modulosize
            self.endofmap = True
        self.cleanMap()
        self.map = mmap.mmap(self.file.fileno(), length=length, offset=offset, access=mmap.ACCESS_READ)

    def length(self):
        """
        Sequential reading
        @return: sum of the length of each line
        """
        startTime = time.time()
        self.open()
        sum = 0
        while not self.end_of_stream():
            sum += len(self.readln())
        finalTime = time.time()
        print("StreamMapping: time = ", finalTime-startTime)
        return sum

    def randomjump(self, j):
        self.open()
        sum = 0
        length = len(self.file.read())
        for i in range(j):
            random.seed(1)
            p = random.randint(0, length)
            print("p =", p)
            self.seek(p)
            line = self.readln()
            sum += len(line)
        return sum