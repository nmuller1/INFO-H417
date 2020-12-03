class StreamCharacter:
    """ Implement readln and writeln by reading / writing one character at a time. We continue reading characters (and collecting the characters read so far) until we read the end-of-line symbol """
    def __init__(self, fileName):
        self.filename = fileName
        self.eof = False
        pass

    def open(self):
        """
        Open an existing file for reading
        """
        self.file = open(self.filename, "r")

    def readln(self):
        """
        Read the next line from the stream
        """
        char = " "
        while char != "\n":
            char = self.file.read(1)
            print(char)
            if not char:
                self.eof = True
                break

    def seek(self, pos):
        """
        Move the file cursor to pos so that a subsequent readln reads from position pos to the next end of line
        @param pos: position in the file where we want to move the cursor
        """
        self.file.seek(pos)

    def end_of_stream(self):
        """
        Checks if the end of stream has been reached
        @return: True if the end of stream has been reached and False otherwise
        """
        return self.eof

    def create(self):
        """
        Create a new file
        """
        self.file = open(self.filename, "x")

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        for char in string:
            self.file.write(char)
        self.file.write("\n")

    def close(self):
        """
        Close the stream
        """
        self.file.close()