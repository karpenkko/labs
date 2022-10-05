class File:
    def __init__(self, name):
        self.f = f

    def show(self):
        print(self.f.read())

    def characters(self):
        self.f.seek(0)
        data = self.f.read().replace(" ", "")
        return len(data)

    def words(self):
        self.f.seek(0)
        data = self.f.read()
        words = data.split()
        return len(words)

    def sentences(self):
        self.f.seek(0)
        data = 0
        for line in self.f:
            data += line.count(".")
        return data


f = open("text.txt", "r")
file = File(f)
# file.show()
print("File has:")
print(file.characters(), "character(s)")
print(file.words(), "word(s)")
print(file.sentences(), "sentence(s)")
f.close()
