from stream import Stream


class StreamCharacter(Stream):
    """
    Implement readln and writeln by reading / writing one character at a time.
    We continue reading characters (and collecting the characters read so far) until we read the end-of-line symbol
    """

    def __init__(self, filename):
        Stream.__init__(self, filename)

    def readln(self):
        """
        Read the next line from the stream
        """
        char = " "
        while char != "\n":
            char = self.file.read(1)
            print(char, end="")
            if not char:
                self.eof = True
                break

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        for char in string:
            self.file.write(char)
        self.file.write("\n")
