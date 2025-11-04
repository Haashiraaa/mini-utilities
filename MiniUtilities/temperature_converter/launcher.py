# launcher.py

"""
Entry point module for the temperature converter app.

This keeps the main logic (in `main.py`) separate,
so you can just run this file to start the program
without exposing all the internal code to the user.
"""

from main import main

try:
    # Launch the app from main.py
    main()
except KeyboardInterrupt:
    # Gracefully handle Ctrl+C interruption
    pass
