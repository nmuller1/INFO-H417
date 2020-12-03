
class StreamBuffer:
    """
    Streams are equiped with a buffer of size B in internal memory.
    Whenever the buffer becomes empty/full the next B characters are read/written from/to the file.
    """

    def __init__(self):
        pass

    def open(self):
        """
        Open an existing file for reading
        """
        pass

    def readln(self):
        """
        Read the next line from the stream
        """
        pass

    def seek(self, pos):
        """
        Move the file cursor to pos so that a subsequent readln reads from position pos to the next end of line
        @param pos: position in the file where we want to move the cursor
        """
        pass

    def end_of_stream(self):
        """
        Checks if the end of stream has been reached
        @return: True if the end of stream has been reached and False otherwise
        """
        pass

    def create(self):
        """
        Create a new file
        """
        pass

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        pass

    def close(self):
        """
        Close the stream
        """
        pass