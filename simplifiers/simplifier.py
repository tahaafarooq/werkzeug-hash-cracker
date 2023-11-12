from werkzeug.security import check_password_hash
from queue import Queue


class SimplifierFile(object):
    def __init__(self, hash_file, wordlist):
        self.hash_file = hash_file
        self.wordlist = wordlist
        self.hashes = {}
        self.hashes_cracked = {}

    def interprete_hash_file(self):
        with open(self.hash_file, "r", encoding="latin-1") as hashs:
            for hasho in hashs:
                words = hasho.strip().split()
                for line in words:
                    self.hashes[line] = True
                    return "Saved The Hashes"

    def crack_hash_file(self):
        with open(self.hash_file, "r") as hasho:
            hasho = hasho.read().split()

        with open(self.wordlist, "r", encoding="latin-1") as wordlist_file:
            raw_words = wordlist_file.read().split()
            words = Queue()

            for word in raw_words:
                words.put(word)

        while not words.empty():
            for i in range(0, len(hasho)):
                password = words.get()
                if check_password_hash(hasho[i], password):
                    print(f"Hash: {hasho[i]} Has Password {password}")
            break
        exit(0)

    def check_results(self):
        if self.hashes_cracked is not None:
            return self.hashes_cracked


class SimplifierSingle(object):
    def __init__(self, hasho, wordlist):
        self.hasho = hasho
        self.wordlist = wordlist

    def crack_single_hash(self):
        with open(self.wordlist, "r", encoding="latin-1") as wordlist_file:
            for word in wordlist_file:
                words = word.strip().split()
                for line in words:
                    check_hash = check_password_hash(self.hasho, line)
                    if check_hash:
                        print(f"Hash: {self.hasho} Has Password {line}")
                        exit(0)
                    else:
                        continue
