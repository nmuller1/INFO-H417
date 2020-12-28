from src.stream import Stream
import time
import random

class StreamBuffer(Stream):
    """
    Streams are equiped with a buffer of size B in internal memory.
    Whenever the buffer becomes empty/full the next B characters are read/written from/to the file.
    """

    def __init__(self, filename, bufferSize):
        Stream.__init__(self, filename)
        self.bufferSize = bufferSize
        self.buffer = ""

    def readln(self):
        """
        Read the next line from the stream
        @return: read line
        """
        endOfLine = False
        line = ""
        while not self.eof and not endOfLine:
            #fill the buffer
            if len(self.buffer) == 0:
                self.buffer = self.file.read(self.bufferSize).decode("latin-1")
                self.buffer = [char for char in self.buffer]
                if len(self.buffer) == 0:
                    self.eof = True
            #read the buffer
            for i in range(len(self.buffer)):
                if self.buffer[0] == "\n":
                    self.buffer.pop(0)
                    endOfLine = True
                    break
                else:
                    line += self.buffer.pop(0)
        return line

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        i = 0
        while i < len(string):
            while not self.bufferIsFull():
                self.buffer += string[i].encode("latin-1")
                i += 1
                if i == len(string):
                    break
            self.file.write(self.buffer)
            self.buffer = ""
        self.file.write("\n".encode("latin-1"))

    def bufferIsFull(self):
        """
        Checks if the buffer is full
        @return: True if the buffer is full and False if not
        """
        return len(self.buffer) == self.bufferSize

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
        print("StreamBuffer : time =", finalTime-startTime)
        return sum

    def randomjump(self, j):
        self.open()
        sum = 0
        length = len(self.file.read())
        for i in range(j):
            random.seed(1)
            p = random.randint(0, length)
            print("p =",p)
            self.seek(p)
            line = self.readln()
            sum += len(line)
        return sum