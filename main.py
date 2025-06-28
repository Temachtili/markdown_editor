# write your code here
class Editor:

    FORMATTERS = {
        "plain": "",
        "bold": "**",
        "italic": "*",
        "header": "#",
        "link": ("[]", "()"),
        "inline-code": "`",
        "new-line": "\n",
        "unordered-list": "*",
        "ordered-list": ".",
    }
    COMMANDS = ["!help", "!done"]

    def __init__(self):
        self.marked_text = []

    def menu(self):
        while True:
            command = input("Choose a formatter: ")
            if self.is_not_valid_formatter(command):
                print("Unknown formatting type or command")
            if command in self.FORMATTERS:
                self.formatter_manager(command)
            if command in self.COMMANDS:
                match command:
                    case "!help":
                        print("Available formatters:", ' '.join(self.FORMATTERS))
                        print("Special commands:", ' '.join(self.COMMANDS))
                    case "!done":
                        self.save_file()
                        exit()

    def save_file(self):
        with open("output.md", "w") as f:
            f.write(''.join(self.marked_text))

    def is_not_valid_formatter(self, command):
        return command not in self.FORMATTERS and command not in self.COMMANDS

    def apply_format(self, formatter, level=1):
        if formatter == "new-line":
            self.marked_text.append("\n")
        elif formatter == "link":
            self.build_link()
        elif formatter == "header":
            text = input("Text: ")
            self.build_header(text, formatter, level)
        elif formatter == "ordered-list" or formatter == "unordered-list":
            self.build_list(formatter)
        else:
            text = input("Text: ")
            self.marked_text.append(self.FORMATTERS[formatter])
            self.marked_text.append(text)
            self.marked_text.append(self.FORMATTERS[formatter])

        print(''.join(self.marked_text))

    def build_list(self, formatter):
        while True:
            try:
                rows = int(input("Number of rows: "))
                if rows <= 0:
                    print("The number of rows should be greater than zero")
                    continue
                for i in range(0, rows):
                    if formatter == "ordered-list":
                        self.marked_text.append(f"{i + 1}")
                    self.marked_text.append(self.FORMATTERS[formatter])
                    self.marked_text.append(" ")
                    self.marked_text.append(input(f"Row #{i + 1}: "))
                    self.marked_text.append("\n")
                break
            except ValueError:
                print("Please enter a valid number")

    def build_header(self, text, formatter, level):
        if len(self.marked_text) > 0:
            self.marked_text.append("\n")
        self.marked_text.append(self.FORMATTERS[formatter] * level)
        self.marked_text.append(" ")
        self.marked_text.append(text)
        self.marked_text.append("\n")

    def build_link(self):
        label = input("Label: ")
        url = input("URL: ")
        link = f"{self.FORMATTERS['link'][0][0]}{label}{self.FORMATTERS['link'][0][1]}{self.FORMATTERS['link'][1][0]}{url}{self.FORMATTERS['link'][1][1]}"
        self.marked_text.append(link)

    def formatter_manager(self, formatter):
        match formatter:
            case "header":
                self.apply_format("header", self.get_level())
            case "bold":
                self.apply_format("bold")
            case "plain":
                self.apply_format("plain")
            case "italic":
                self.apply_format("italic")
            case "link":
                self.apply_format("link")
            case "inline-code":
                self.apply_format("inline-code")
            case "new-line":
                self.apply_format("new-line")
            case "unordered-list":
                self.apply_format("unordered-list")
            case "ordered-list":
                self.apply_format("ordered-list")
            case _:
                print("Unknown formatting type or command")

    @staticmethod
    def get_level():
        while True:
            try:
                level = int(input("Level: "))
                if 1 <= level <= 6:
                    return level
                else:
                    print("The level should be within the range of 1 to 6")
            except ValueError:
                print("Please enter a valid number")

    def main(self):
        self.menu()


if __name__ == "__main__":
    Editor().main()