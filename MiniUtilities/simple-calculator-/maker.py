import time

# ANSI color codes for terminal styling
GREEN = "\033[92m"  # Bright green text
RESET = "\033[0m"  # Reset to default terminal color


class Signature:
    """
    A class to generate and display a custom 3D ASCII art signature logo.

    This signature can be used as a branding element for projects,
    GitHub profiles, or terminal applications. It features a 3D cube
    design with personalized branding text.

    Attributes:
        None (all data is generated dynamically in methods)
    """

    def sig(self):
        """
        Generates a 3D ASCII art cube with personalized branding.

        The cube contains:
        - Username 'HAASHIRAAA' displayed prominently
        - GitHub handle '@Haashiraaa'
        - Twitter/X handle '@Haashiraaa'

        Returns:
            str: A multiline string containing the 3D ASCII art signature
        """
        three_d_cube = """


              /----------------/
             /|@@@@@@@@@@@@@@@/|
            / |##############/ |
           /  |#############/  |
          /   |############/   |
         /____|___________/    |
         |    |           |    |
         |    |***********|    |
         |    |HAASHIRAAA |    |  Main username
         |    |***********|    |
         |    |___________|____|
         |   /Github:     |   /
         |  /@Haashiraaa  |  /   GitHub profile
         | /X:            | /
         |/@Haashiraaa    |/     Twitter/X profile
         -----------------

        """
        return three_d_cube

    def print_slowly(self, art, delay=0.1, color=GREEN):
        """
        Prints ASCII art line by line with a typing animation effect.

        This creates a dramatic reveal for the signature logo, making it
        more engaging when displayed in terminals or during project startup.

        Args:
            art (str): The ASCII art string to print
            delay (float, optional): Seconds between each line. Defaults to 0.1
            color (str, optional): ANSI color code. Defaults to GREEN

        Example:
            >>> sign = Signature()
            >>> sign.print_slowly(sign.signature(), delay=0.2)
        """
        # Split the art into lines and print each one with delay
        for line in art.splitlines():
            print(color + line + RESET)  # Apply color and reset after each line
            time.sleep(delay)


