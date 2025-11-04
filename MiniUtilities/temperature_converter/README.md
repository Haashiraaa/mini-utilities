# Temperature Converter (MiniUtilities/temperature_converter)

A small, interactive CLI utility to convert temperatures between Kelvin (K), Celsius (C) and Fahrenheit (F).  
Designed for learning and quick utility use — minimal dependencies and a compact codebase.

## Features
- Convert between K, C and F.
- Interactive prompt with unit selection and input validation.
- Conversion history saved to disk.
- Simple, single-file launcher to start the app.

## Requirements
- Python 3.8+ (3.10 recommended)
- Optional dev dependency for debug output: `icecream` (only used for debugging lines)
  - Install: `pip install icecream`

## Quick start

1. Clone the repository (or navigate into your local copy).
2. Run the app from the temperature_converter directory:

```bash
cd MiniUtilities/temperature_converter
python launcher.py
```

(If you prefer, run `main.py` directly: `python main.py`.)

## Usage example (interactive)
- Program shows supported units (K, C, F).
- Enter the current unit (e.g., `K`) and the numeric value, then the target unit (e.g., `C`).
- The program prints the converted value (rounded to 2 decimals), logs the conversion, and asks whether to continue.

Sample session:
```text
Units

1. K --> Kelvin
2. C --> Celsius
3. F --> Fahrenheit

current temp. unit: K
value: 300
Convert to..
>>> C

= 26.85°C
```

## Conversion semantics
- Conversions use conventional formulas (Kelvin offset = 273.15; Celsius ↔ Fahrenheit uses 9/5, 5/9 factors).
- The app rounds displayed results to 2 decimal places.

## History / output file
Conversion attempts are recorded using `save()` to `convert_history.json` (in the working directory). Note:
- Current behavior appends JSON dumps of the in-memory history each time the program exits; this leads to multiple JSON objects appended across runs (not a single valid JSON array). Treat the file as an append-based log rather than a strict JSON array.

## Contributing
- Fixes and improvements welcome. Please include unit tests where appropriate.
- If you open PRs, explain the behavior change and include before/after examples for CLI output and saved history.

## Author & License
Author: Haashiraaa  
