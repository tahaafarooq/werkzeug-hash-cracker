import argparse
from simplifiers.simplifier import SimplifierSingle, SimplifierFile


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Werkzeug Security Hash Cracker")

    parser.add_argument('--single', nargs=2, metavar=('hash', 'wordlist'), help='Crack a single hash string')
    parser.add_argument('--file', nargs=2, metavar=('hashfile', 'wordlist'), help='Crack a file with multiple hashes')
    parser.add_argument('--help', action='store_true', help='Print help information about this script')
    parser.add_argument('--about', action='store_true', help='Print core information about the script and developer')

    args = parser.parse_args()

    if args.help:
        parser.print_help()
    elif args.about:
        about = """
        Werkzeug Hash Cracker: Is a minimal script that cracks hashes which are generated from werkzeug.security library in python\n
        About Developer: Tahaa Farooq is a cybersecurity professional with a passion in programming. Check his github for more information (https://github.com/tahaafarooq)"""
        print(about)
    elif args.single:
        hash_string, wordlist_file = args.single
        simple_crack = SimplifierSingle(hash_string, wordlist_file)
        simple_crack.crack_single_hash()
    elif args.file:
        hash_file, wordlist_file = args.file
        simple_crack = SimplifierFile(hash_file, wordlist_file)
        interpreter = simple_crack.interprete_hash_file()
        if interpreter == "Saved The Hashes":
            check_crack = simple_crack.crack_hash_file()
            if check_crack == "Cracked Hash(es)":
                print(simple_crack.check_results())
            else:
                print("No Hash Cracked")
        else:
            print("Unable To Read")
    else:
        parser.print_help()
