# Write a program to check valid C-identifiers


class C_Identifier:
    def __init__(self, string):
        self.string = string
        self.keywords = ["auto", "double", "int", "struct",
                         "break", "else", "long", "switch",
                         "case", "enum", "register", "typedef",
                         "const", "extern", "return", "union",
                         "char", "float", "short", "unsigned",
                         "continue", "for", "signed", "volatile",
                         "default", "goto", "sizeof", "void",
                         "do", "if", "static", "while"
                         ]

    def is_keyword(self):
        if self.string in self.keywords:
            return True
        return False

    def is_valid_identifier(self):
        if self.is_keyword():
            return False
        elif not (self.string[0].isalpha() or self.string[0] == '_'):
            return False

        for x in range(1, len(self.string)):
            if not (self.string[x].isalnum() or self.string[x] == '_'):
                return False
        return True


def main():
    string = input("Enter any string: ")
    check = C_Identifier(string)
    if check.is_valid_identifier():
        print(f"'{string}' is valid C-identifier")
    else:
        print(f"'{string}'' is Invalid identifier")


if __name__ == '__main__':
    main()
