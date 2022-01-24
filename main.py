from random import choice

def generate(characters, length):
    pw = ""
    for i in range(length):
        pw += choice(characters)
    return pw

if __name__ == "__main__":
    
    import argparse
    from string import ascii_uppercase, ascii_lowercase, digits, punctuation

    desc = "password generator"
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument(
        "-l", "--length", 
        type=int, 
        nargs="?", 
        metavar="N", 
        default=4, 
        help="set password length"
        )

    parser.add_argument(
        "-c", "--char", 
        type=str, 
        nargs="?", 
        metavar="C", 
        default="d", 
        help=
        """
        set characters in password
        (l -> lowercase)
        (u -> uppercase)
        (d -> digits)
        (s -> symbols)
        """
        )

    args = parser.parse_args()

    chars = ""

    if "l" in args.char or "L" in args.char:
        chars += ascii_lowercase
    if "u" in args.char or "U" in args.char:
        chars += ascii_uppercase
    if "d" in args.char or "D" in args.char:
        chars += digits
    if "s" in args.char or "S" in args.char:
        chars += punctuation

    pw = generate(chars, args.length)
    print(pw)
