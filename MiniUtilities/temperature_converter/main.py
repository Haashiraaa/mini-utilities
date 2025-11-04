# main.py

import sys
import os
from converter import Converter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from icecream import ic
import json

# Toggle debugging easily
DEBUG = False
if not DEBUG:
    ic.disable()
else:
    ic.enable()

# Global variables
convert_history = {}
END = "\n[Program finished.]"
APP_NAME = "MyTemp"
AUTHOR = "Haashiraaa"


def clear_screen():
    """Clears the terminal window depending on the OS."""
    os.system("cls" if os.name == "nt" else "clear")


def again():
    """
    Ask the user if they want to perform another conversion.
    Keeps asking until a valid response (y/n) is given.
    """
    while True:
        print("\nWould you like to carry out another conversion?")
        try_again = input("(y/n): ").lower().strip()
        if not try_again:
            continue
        if try_again == "y":
            return True
        elif try_again == "n":
            return False
        else:
            print("\nDidn't quite catch that.")


def make_entry(crr_u, crr_v, cvrt_u, cvrt_v):
    """
    Creates a new temperature conversion entry.

    Each entry includes:
      - Current temperature (unit + value)
      - Converted temperature (unit + value)
      - Timestamp (in Nigeria's timezone)
    """
    nigeria_time = datetime.now(timezone.utc) + timedelta(hours=1)
    timestamp = nigeria_time.strftime("%Y-%m-%d %H:%M:%S")

    convert_history[timestamp] = {
        "curr_temp": {"unit": crr_u, "value": crr_v},
        "cvrt_temp": {"unit": cvrt_u, "value": cvrt_v},
    }


def save(fn):
    """
    Saves the conversion history as a JSON file.

    If the file doesn't exist, it creates one.
    If it exists, new data is appended in a new line.
    """
    path = Path("convert_history.json")
    if not os.path.exists(path):
        with path.open("w", encoding="utf-8") as f:
            f.write(json.dumps(fn, indent=4) + "\n")
    else:
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(fn, indent=4) + "\n")


def main():
    """Main function that runs the temperature conversion app."""
    clear_screen()
    print("=" * 7, APP_NAME, "=" * 7)
    cvrt = Converter()
    result = None

    while True:
        try:
            # Show available temperature units
            print("\nUnits\n")
            for i, (k, v) in enumerate(cvrt.temp_dict.items(), start=1):
                print(f"{i}. {v} --> {k}")

            # Get the current temperature unit
            current_temp_unit = input("\ncurrent temp. unit: ").upper().strip()
            if not current_temp_unit:
                continue

            # Get the temperature value
            value = float(input("value: ").strip())

            # Ask which unit to convert to
            print("\n\tConvert to..\n")
            temp_unit = input(">>> ").upper().strip()
            if not temp_unit:
                continue

            # Handle conversions based on the unit provided
            if current_temp_unit == cvrt.unit_list[0]:
                result = cvrt.cvrt_kelvin(value, temp_unit)
            elif current_temp_unit == cvrt.unit_list[1]:
                result = cvrt.cvrt_celsius(value, temp_unit)
            elif current_temp_unit == cvrt.unit_list[2]:
                result = cvrt.cvrt_fahrenheit(value, temp_unit)
            else:
                print(cvrt.INVALID)
                continue

            if result == cvrt.INVALID:
                print(result)
                continue

            # Display the result
            print(result)

            # Log conversion to history
            make_entry(current_temp_unit, value, temp_unit, cvrt.result)

            # Ask if user wants to continue
            if again():
                continue
            else:
                save(convert_history)
                clear_screen()
                print(f"\nThanks for using {APP_NAME}\nAuthor --> {AUTHOR}")
                print(END)
                sys.exit()

        except ValueError:
            print("\nOops! Enter a number.")
            continue
        except KeyboardInterrupt:
            print("\n", END)
            sys.exit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()