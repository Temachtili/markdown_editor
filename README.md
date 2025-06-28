# Markdown Text Editor (Hyperskill Project)

This project is part of the **Python Developer track** on Hyperskill. It is a console-based markdown text editor that supports multiple formatting options and saves the final output to a `.md` file.

## Features

- Text formatters:
  - `plain`
  - `bold`
  - `italic`
  - `header` (levels 1 to 6)
  - `link`
  - `inline-code`
  - `new-line`
  - `unordered-list`
  - `ordered-list`

- Special commands:
  - `!help` — displays the list of available formatters and commands
  - `!done` — exits the editor and saves the output to `output.md`

## How it Works

The program repeatedly prompts the user to choose a text formatter or command. The corresponding formatting is applied and shown in the console. When the user is finished, they can enter `!done` to save the formatted text to a file named `output.md`.

## Example

```
Choose a formatter: bold
Text: Hello
**Hello**
Choose a formatter: !done
```

This will create a file `output.md` with the contents:
```
**Hello**
```

## Usage

Run the `main.py` script and follow the prompts:

```bash
python main.py
```

## Learning Objectives

This project helps to reinforce the following Python concepts:

- Class structure and object-oriented programming
- Handling user input and control flow
- String manipulation and formatting
- File I/O in Python

## 🧠 Author

Angel Gael Aviles Gama  
Linkedin: [@angelavilesgama](https://www.linkedin.com/in/angelavilesgama/)
GitHub: [@temachtili](https://github.com/temachtili)