class File:
    def __init__(self, f):
        self.f = f
        self.data = f.read()

    def show(self):
        print(self.data)

    def characters(self):
        return len(self.data.replace(" ", ""))

    def words(self):
        return len(self.data.split())

    def sentences(self):
        return len(self.data.split("."))


file = open("text.txt", "r")
file1 = File(file)
# file.show()
print("File has:")
print(file1.characters(), "character(s)")
print(file1.words(), "word(s)")
print(file1.sentences(), "sentence(s)")
file.close()
