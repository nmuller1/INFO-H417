import mmap
from stream import Stream

class StreamMapping(Stream):
    """
    Implement readln and writeln by mapping and unmapping B characters of the file into internal memory through memory mapping.
    Whenever you need to read/write outside of the mapped portion, the next B element portion of the file is mapped.
    """

    def __init__(self, filename, mmapSize):
        Stream.__init__(self, filename)
        self.mmapSize = mmapSize
        

    def readln(self):
        """
        Read the next line from the stream
        """
        char = " "
        line = ""
        self.map = mmap.mmap(self.file.fileno(), self.mmapSize)
        while char and char != "\n":
            while not self.mapIsFull():
                line += self.map.read(1)
                if not char:
                    self.eof = True
                    break
                if char == "\n":
                    break
            self.cleanMap()
            self.map = mmap.mmap(self.file.fileno(), self.mmapSize)
        self.cleanMap()
        self.map.close()
        return line

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
    
        i = 0
        self.map = mmap.mmap(self.file.fileno(), self.mmapSize)
        while i < len(string):
            while not self.mapIsFull():
                i += 1
                if i == len(string):
                    break
            for j in self.map:
                self.map.write(j)
            self.cleanMap()
        self.map.write("\n")

    def mapIsFull(self):
        """
        Checks if the buffer is full
        @return: True if the buffer is full and False if not
        """
        return self.map.size() == self.mmapSize
    
    def cleanMap(self):
        """
        Empty the buffer
        """
        self.map.flush()