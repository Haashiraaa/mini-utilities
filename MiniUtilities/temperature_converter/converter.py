# converter.py

class Converter:
    """
    Handles temperature conversions between Kelvin, Celsius, and Fahrenheit.
    Each method converts from one base unit to another.
    """

    def __init__(self):
        # Maps temperature names to their short unit symbols
        self.temp_dict = {"Kelvin": "K", "Celsius": "C", "Fahrenheit": "F"}
        self.unit_list = [u for u in self.temp_dict.values()]

        self.INVALID = "\nInvalid unit!"
        self.result = 0  # stores last conversion result

        # Conversion formulas (Kelvin)
        self.kel_cel = lambda val: val - 273.15
        self.kel_fah = lambda val: (val - 273.15) * (9 / 5) + 32

        # Conversion formulas (Celsius)
        self.cel_kel = lambda val: val + 273.15
        self.cel_fah = lambda val: (val * 9 / 5) + 32

        # Conversion formulas (Fahrenheit)
        self.fah_kel = lambda val: (val - 32) * (5 / 9) + 273.15
        self.fah_cel = lambda val: (val - 32) * 5 / 9


    def cvrt_kelvin(self, val, tmp_u):
        """
        Converts a given Kelvin value to Celsius or Fahrenheit.
        Args:
            val (float): The temperature value in Kelvin.
            tmp_u (str): The unit to convert to ('C' or 'F').
        Returns:
            str: Converted temperature with appropriate symbol or invalid message.
        """
        try:
            if tmp_u == self.unit_list[1]:
                self.result = round(self.kel_cel(val), 2)
                return f"\n= {self.result}°C"
            elif tmp_u == self.unit_list[2]:
                self.result = round(self.kel_fah(val), 2)
                return f"\n= {self.result}°F"
            else:
                return self.INVALID
        except ValueError:
            pass


    def cvrt_celsius(self, val, tmp_u):
        """
        Converts a given Celsius value to Kelvin or Fahrenheit.
        Args:
            val (float): The temperature value in Celsius.
            tmp_u (str): The unit to convert to ('K' or 'F').
        Returns:
            str: Converted temperature with appropriate symbol or invalid message.
        """
        try:
            if tmp_u == self.unit_list[0]:
                self.result = round(self.cel_kel(val), 2)
                return f"\n= {self.result}K"
            elif tmp_u == self.unit_list[2]:
                self.result = round(self.cel_fah(val), 2)
                return f"\n= {self.result}°F"
            else:
                return self.INVALID
        except ValueError:
            pass


    def cvrt_fahrenheit(self, val, tmp_u):
        """
        Converts a given Fahrenheit value to Kelvin or Celsius.
        Args:
            val (float): The temperature value in Fahrenheit.
            tmp_u (str): The unit to convert to ('K' or 'C').
        Returns:
            str: Converted temperature with appropriate symbol or invalid message.
        """
        try:
            if tmp_u == self.unit_list[0]:
                self.result = round(self.fah_kel(val), 2)
                return f"\n= {self.result}K"
            elif tmp_u == self.unit_list[1]:
                self.result = round(self.fah_cel(val), 2)
                return f"\n= {self.result}°C"
            else:
                return self.INVALID
        except ValueError:
            pass