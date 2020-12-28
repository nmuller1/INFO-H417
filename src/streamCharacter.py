from src.stream import Stream
import time
import random

class StreamCharacter(Stream):
    """
    Implement readln and writeln by reading / writing one character at a time.
    We continue reading characters (and collecting the characters read so far) until we read the end-of-line symbol
    """

    def __init__(self, filename):
        Stream.__init__(self, filename)

    def open(self):
        """
        Open an existing file for reading
        """
        self.file = open(self.filename, "rb", buffering=0)

    def readln(self):
        """
        Read the next line from the stream
        @return: read line
        """
        line = ""
        char = self.file.read(1).decode("latin-1")
        while not self.eof and char != "\n":
            line += char
            char = self.file.read(1)
            char = char.decode("latin-1")
            if not char:
                self.eof = True
        return line

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        for char in string:
            self.file.write(char.encode("latin-1"))
        self.file.write("\n".encode("latin-1"))

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
        print("StreamCharacter : time=", finalTime-startTime)
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