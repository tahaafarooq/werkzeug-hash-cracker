from werkzeug.security import check_password_hash


class SimplifierFile(object):
    def __init__(self, hash_file, wordlist):
        self.hash_file = hash_file
        self.wordlist = wordlist
        self.hashes = {}
        self.hashes_cracked = {}

    def interprete_hash_file(self):
        with open(self.hash_file, "r") as hashs:
            for hasho in hashs:
                words = hasho.strip().split()
                for line in words:
                    self.hashes[line] = True
                    return "Saved The Hashes"

    def crack_hash_file(self):
        with open(self.wordlist, "r") as wordlist_file:
            for word in wordlist_file:
                # len_hashes = len(self.hashes)
                words = word.strip().split()
                for line in words:
                    for hasho in self.hashes:
                        check_hash = check_password_hash(hasho, line)
                        if check_hash:
                            print(f"Hash: {hasho} Has Password {line}")
                            self.hashes_cracked[line] = True
                            return "Cracked Hash(es)"
                        else:
                            continue

    def check_results(self):
        if self.hashes_cracked is not None:
            return self.hashes_cracked


class SimplifierSingle(object):
    def __init__(self, hasho, wordlist):
        self.hasho = hasho
        self.wordlist = wordlist

    def crack_single_hash(self):
        with open(self.wordlist, "r") as wordlist_file:
            for word in wordlist_file:
                words = word.strip().split()
                for line in words:
                    check_hash = check_password_hash(self.hasho, line)
                    if check_hash:
                        print(f"Password Is {line}")
                        exit(0)
                    else:
                        continue
