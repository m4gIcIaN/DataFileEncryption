import hashlib

class HashEncryptor:

    def __init__(self, file):
        self.file = file

    def setFile(self, fileInput):
        self.file = fileInput

    def getFile(self):
        return self.file

    def encrypt_Sha1(self):
        try:
            # Creates files that will be read from, and wrote to
            infile = open(self.file, "r")
            outfile = open("Encryption_Results.txt", "w")

            # Creates hashing Object
            hasher = hashlib.sha1()

            # Creates empty list that will contain hashed lines
            listHashedLines = []

            # Hashes every line in the infile
            for lines in infile:
                # Checks when the file ends
                if lines == "":
                    break;
                else:
                    hasher.update(lines.encode())
                    hashedLine = hasher.hexdigest()
                    listHashedLines.append(hashedLine)

            # Writes hashed results into Encryption_Results.txt
            for results in listHashedLines:
                outfile.write(results)
                outfile.write("\n")

            # Closes both input and output files
            infile.close()
            outfile.close()

            # Verifies end of encryption
            print("Encryption Successful")
        except:
            # Gives warning that something went wrong
            print("An error has occurred")

    def encrypt_Sha256(self):
        try:
            # Creates files that will be read from, and wrote to
            infile = open(self.file, "r")
            outfile = open("Encryption_Results.txt", "w")

            # Creates hashing Object
            hasher = hashlib.sha256()

            # Creates empty list that will contain hashed lines
            listHashedLines = []

            # Hashes every line in the infile
            for lines in infile:
                # Checks when the file ends
                if lines == "":
                    break;
                else:
                    hasher.update(lines.encode())
                    hashedLine = hasher.hexdigest()
                    listHashedLines.append(hashedLine)

            # Writes hashed results into Encryption_Results.txt
            for results in listHashedLines:
                outfile.write(results)
                outfile.write("\n")

            # Closes both input and output files
            infile.close()
            outfile.close()

            # Verifies end of encryption
            print("Encryption Successful")
        except:
            # Gives warning that something went wrong
            print("An error has occurred")

    def encrypt_Sha224(self):
        try:
            # Creates files that will be read from, and wrote to
            infile = open(self.file, "r")
            outfile = open("Encryption_Results.txt", "w")

            # Creates hashing Object
            hasher = hashlib.sha224()

            # Creates empty list that will contain hashed lines
            listHashedLines = []

            # Hashes every line in the infile
            for lines in infile:
                # Checks when the file ends
                if lines == "":
                    break;
                else:
                    hasher.update(lines.encode())
                    hashedLine = hasher.hexdigest()
                    listHashedLines.append(hashedLine)

            # Writes hashed results into Encryption_Results.txt
            for results in listHashedLines:
                outfile.write(results)
                outfile.write("\n")

            # Closes both input and output files
            infile.close()
            outfile.close()

            # Verifies end of encryption
            print("Encryption Successful")
        except:
            # Gives warning that something went wrong
            print("An error has occurred")

    def encrypt_Sha384(self):
        try:
            # Creates files that will be read from, and wrote to
            infile = open(self.file, "r")
            outfile = open("Encryption_Results.txt", "w")

            # Creates hashing Object
            hasher = hashlib.sha384()

            # Creates empty list that will contain hashed lines
            listHashedLines = []

            # Hashes every line in the infile
            for lines in infile:
                # Checks when the file ends
                if lines == "":
                    break;
                else:
                    hasher.update(lines.encode())
                    hashedLine = hasher.hexdigest()
                    listHashedLines.append(hashedLine)

            # Writes hashed results into Encryption_Results.txt
            for results in listHashedLines:
                outfile.write(results)
                outfile.write("\n")

            # Closes both input and output files
            infile.close()
            outfile.close()

            # Verifies end of encryption
            print("Encryption Successful")
        except:
            # Gives warning that something went wrong
            print("An error has occurred")

    def encrypt_Sha512(self):
        try:
            # Creates files that will be read from, and wrote to
            infile = open(self.file, "r")
            outfile = open("Encryption_Results.txt", "w")

            # Creates hashing Object
            hasher = hashlib.sha512()

            # Creates empty list that will contain hashed lines
            listHashedLines = []

            # Hashes every line in the infile
            for lines in infile:
                # Checks when the file ends
                if lines == "":
                    break;
                else:
                    hasher.update(lines.encode())
                    hashedLine = hasher.hexdigest()
                    listHashedLines.append(hashedLine)

            # Writes hashed results into Encryption_Results.txt
            for results in listHashedLines:
                outfile.write(results)
                outfile.write("\n")

            # Closes both input and output files
            infile.close()
            outfile.close()

            # Verifies end of encryption
            print("Encryption Successful")
        except:
            # Gives warning that something went wrong
            print("An error has occurred")

    def encrypt_Blake2b(self):
        try:
            # Creates files that will be read from, and wrote to
            infile = open(self.file, "r")
            outfile = open("Encryption_Results.txt", "w")

            # Creates hashing Object
            hasher = hashlib.blake2b()

            # Creates empty list that will contain hashed lines
            listHashedLines = []

            # Hashes every line in the infile
            for lines in infile:
                # Checks when the file ends
                if lines == "":
                    break;
                else:
                    hasher.update(lines.encode())
                    hashedLine = hasher.hexdigest()
                    listHashedLines.append(hashedLine)

            # Writes hashed results into Encryption_Results.txt
            for results in listHashedLines:
                outfile.write(results)
                outfile.write("\n")

            # Closes both input and output files
            infile.close()
            outfile.close()

            # Verifies end of encryption
            print("Encryption Successful")
        except:
            # Gives warning that something went wrong
            print("An error has occurred")

    def encrypt_Blake2s(self):
        try:
            # Creates files that will be read from, and wrote to
            infile = open(self.file, "r")
            outfile = open("Encryption_Results.txt", "w")

            # Creates hashing Object
            hasher = hashlib.blake2s()

            # Creates empty list that will contain hashed lines
            listHashedLines = []

            # Hashes every line in the infile
            for lines in infile:
                # Checks when the file ends
                if lines == "":
                    break;
                else:
                    hasher.update(lines.encode())
                    hashedLine = hasher.hexdigest()
                    listHashedLines.append(hashedLine)

            # Writes hashed results into Encryption_Results.txt
            for results in listHashedLines:
                outfile.write(results)
                outfile.write("\n")

            # Closes both input and output files
            infile.close()
            outfile.close()

            # Verifies end of encryption
            print("Encryption Successful")
        except:
            # Gives warning that something went wrong
            print("An error has occurred")

    def encrypt_Md5(self):
        try:
            # Creates files that will be read from, and wrote to
            infile = open(self.file, "r")
            outfile = open("Encryption_Results.txt", "w")

            # Creates hashing Object
            hasher = hashlib.md5()

            # Creates empty list that will contain hashed lines
            listHashedLines = []

            # Hashes every line in the infile
            for lines in infile:
                # Checks when the file ends
                if lines == "":
                    break;
                else:
                    hasher.update(lines.encode())
                    hashedLine = hasher.hexdigest()
                    listHashedLines.append(hashedLine)

            # Writes hashed results into Encryption_Results.txt
            for results in listHashedLines:
                outfile.write(results)
                outfile.write("\n")

            # Closes both input and output files
            infile.close()
            outfile.close()

            # Verifies end of encryption
            print("Encryption Successful")
        except:
            # Gives warning that something went wrong
            print("An error has occurred")

# Warns that this Class is specifically made for creating Objects
def warning():
    print("This is not meant to function alone")

# Checks Validity
if __name__ == "__main__":
    warning()
