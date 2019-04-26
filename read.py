class read(object):
    def __new__(cls, filename: str, delim: str = None) -> open:
        if delim != None:
            return cls.fileread(cls, filename).split(delim)
        return cls.fileread(cls, filename)
    def fileread(self, filename: str) -> [open]:
        with open(filename, "rb") as f:
            var = f.read().decode("ISO-8859-1").replace("\r", "").replace("\t", "")
        return var