# Simple Calculator (Refactored)

A small command-line calculator written in Python. It supports the four basic arithmetic operations with a clean, modular, object-oriented structure, a dynamic UI for input, and an optional animated signature on exit.

## Features

- Add, Subtract, Multiply, Divide
- Dynamic UI for user input and menu handling
- Reuse the last result for chaining calculations
- Graceful error handling (invalid input, division by zero)
- Clean OOP design with separated logic and UI modules
- Optional debug mode (powered by `icecream`)
- Custom ASCII signature animation on exit

## Project structure

- simple_calculator/
  - operator_logic.py     — arithmetic operations
  - calculator_ui.py      — user interaction and menu flow
  - maker.py              — generates and displays the signature animation
  - simple_calculator.py  — main program / controller
  - README.md             — project documentation

## Requirements

- Python 3.8+
- Optional: icecream, emoji

install the optional packages with:

```bash
pip install icecream emoji
```

<<<<<<< HEAD
Dynamic UI system for handling user inputs and displaying menus

Last-result reuse — easily chain your previous results into new calculations

Graceful error handling, including invalid inputs and division by zero

Clean OOP design using separated logic and UI modules

Custom ASCII signature animation for branding and creative finish

Optional debug mode (powered by icecream) for development visibility



---

 Project Structure

simple_calculator/<br>
│<br>
├── operator_logic.py     # Handles arithmetic operations<br>
├── calculator_ui.py      # Manages user interaction and menu flow<br>
├── maker.py              # Generates and displays the custom signature<br>
├── simple_calculator.py  # Main entry point (program controller)<br>
└── README.md             # Project documentation<br>


---

 How It Works

1. The main loop (in simple_calculator.py) handles user choices.


2. Each arithmetic operation is delegated to the OperatorLogic class.


3. All user interaction — menus, prompts, and result reuse — is handled by CalculatorUi.


4. The program ends with a custom animated signature from maker.py.




---

 Installation

Make sure you have Python 3.8+ installed.

Clone the repository and install dependencies:<b>

git clone https://github.com/Haashiraaa/simple-calculator-.git<br>
cd simple-calculator-<br>
pip install -r requirements.txt<b>
=======
## Installation

```bash
git clone https://github.com/Haashiraaa/simple-calculator-.git
cd simple-calculator-
```
>>>>>>> 44c2d79 (Updated README)

## Usage

Run the program:

```bash
python simple_calculator.py
```

Main menu options:

1. Add ➕  
2. Subtract ➖  
3. Multiply ✖️  
4. Divide ➗  
5. Quit 🚫

Enter numbers one at a time. Type `=` when you are done entering numbers to see the result.

## Example session

```
Simple Calculator 🔢

Main Menu
1. Add➕
2. Subtract➖
3. Multiply✖️
4. Divide➗
5. Quit🚫

Enter an option from 1 to 5
>>> 1

Enter numbers (enter '=' to see result)
number: 10
number: 5
number: =

= 15
```

## Exit Signature (example)

When the program exits it can display a custom ASCII signature. Example:

<<<<<<< HEAD
/----------------/<br>
             /|@@@@@@@@@@@@@@@/|<br>
            / |##############/ |<br>
           /  |#############/  |<br>
          /   |############/   |<br>
         /____|___________/    |<br>
         |    |HAASHIRAAA |    |<br>
         |    |___________|____|<br>
         |   /Github:     |   /<br>
         |  /@Haashiraaa  |  /<br>
         | /X:            | /<br>
         |/@Haashiraaa    |/<br>
         -----------------<br>
=======
```
/----------------/
             /|@@@@@@@@@@@@@@@/|
            / |##############/ |
           /  |#############/  |
          /   |############/   |
         /____|___________/    |
         |    |HAASHIRAAA |    |
         |    |___________|____|
         |   /Github:     |   /
         |  /@Haashiraaa  |  /
         | /X:            | /
         |/@Haashiraaa    |/
         -----------------
```
>>>>>>> 44c2d79 (Updated README)

## Refactoring notes

- Converted from a single procedural script to an OOP design
- Split concerns into:
  - OperatorLogic (arithmetic)
  - CalculatorUi (input & menus)
  - Maker (signature)
- Added docstrings, PEP 8 improvements, and optional debugging hooks

## License

This project is open-source under the MIT License.
