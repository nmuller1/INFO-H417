class StreamCharacter:
    """ Implement readln and writeln by reading / writing one character at a time. We continue reading characters (and collecting the characters read so far) until we read the end-of-line symbol """
    def __init__(self, fileName):
        self.filename = fileName
        self.eof = False
        pass

    def open(self):
        self.file = open(self.filename, "r")
        

    def readln(self):
        char = " "
        while char != "\n":
            char = self.file.read(1)
            print(char)
            if not char:
                self.eof = True
                break

    def seek(self, pos):
        self.file.seek(pos)

    def end_of_stream(self):
        return self.eof

    def create(self):
        self.file = open(self.filename, "x")

    def writeln(self, string):
        for char in string:
            self.file.write(char)
        self.file.write("\n")

    def close(self):
        self.file.close()

"""if __name__ == "__main__":"""
