from stream import Stream
import time
import random

class StreamLine(Stream):
    """
    Implement readln and writeln by using the fgets and fputs functions from the C stdio library.
    These functions implements a buffering mechanism.
    """

    def __init__(self, filename):
        Stream.__init__(self, filename)

    def readln(self):
        """
        Read the next line from the stream
        """
        line = self.file.readline().decode("latin-1")
        if line == "":
            self.eof = True
        return line.strip("\n")

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        res = string + "\n"
        self.file.write(res.encode("latin-1"))

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
        timeTotal = finalTime - startTime
        print("StreamLine : time =", timeTotal)
        return sum, timeTotal

    def randomjump(self, j):
        startTime = time.time()
        self.open()
        sum = 0
        length = len(self.file.read())
        for i in range(j):
            p = random.randint(0, length)
            self.seek(p)
            line = self.readln()
            sum += len(line)
        finalTime = time.time()
        timeTotal = finalTime - startTime
        print("StreamLine : time =", timeTotal)
        return sum, timeTotal