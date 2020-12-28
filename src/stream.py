class Stream:
    """
    Implements the common methods of the streams
    """
    def __init__(self, filename):
        self.filename = filename
        self.eof = False

    def open(self):
        """
        Open an existing file for reading
        """
        self.file = open(self.filename, "rb")

    def seek(self, pos):
        """ b
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
        self.file = open(self.filename, "xb")

    def close(self):
        """
        Close the stream
        """
        self.file.close()