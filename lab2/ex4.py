class File:
    def __init__(self, f):
        self.f = f

    def characters(self):
        self.f.seek(0)
        value = 0
        for item in self.f:
            c = item.replace(" ", "")
            value += len(c)
        return value

    def words(self):
        self.f.seek(0)
        value = 0
        for item in self.f:
            w = item.split()
            value += len(w)
        return value

    def sentences(self):
        self.f.seek(0)
        value = 0
        for item in self.f:
            s = item.split(".")
            value += len(s)
        return value


file = open("text.txt", "r")
file1 = File(file)
print("File has:")
print(file1.characters(), "character(s)")
print(file1.words(), "word(s)")
print(file1.sentences(), "sentence(s)")
file.close()
