import mmap

class StreamMapping:
    """ Read and write is performed by mapping and unmapping B characters of the file into internal memory through memory mapping. Whenever you need to read/write outside of the mapped portion, the next B element portion of the file is mapped. """
    def __init__(self, fileName, buffer):
        self.filename = filename
        self.eof = False
        pass

    def open(self):
        self.file = open(self.filename, "r")
        pass

    def readIn(self):
        self.map = mmap.mmap(sel.file.fileno(), 0)
        pass

    def seek(self, pos):
        self.map.seek(pos)
        pass

    def end_of_stream(self):
        return self.eof

    def create(self):
        self.file = open(self.filename, "x")

    def writeIn(self):
        for char in string:
            self.map.write(char)
        self.map.write("\n")

    def close(self):
        self.file.close()


"""if __name__ == "__main__":"""