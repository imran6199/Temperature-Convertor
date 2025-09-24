def celsius_to_fahrenheit(c):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Formula: (°C × 9/5) + 32 = °F
    """
    return (c * 9/5) + 32   


def celsius_to_kelvin(c):
    """
    Convert temperature from Celsius to Kelvin.
    
    Formula: °C + 273.15 = K
    """
    return c + 273.15


def fahrenheit_to_celsius(f):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Formula: (°F - 32) × 5/9 = °C
    """
    return (f - 32) * 5/9


def fahrenheit_to_kelvin(f):
    """
    Convert temperature from Fahrenheit to Kelvin.
    
    Formula: (°F - 32) × 5/9 + 273.15 = K
    """
    return (f - 32) * 5/9 + 273.15


def kelvin_to_celsius(k):
    """
    Convert temperature from Kelvin to Celsius.
    
    Formula: K - 273.15 = °C
    """
    return k - 273.15


def kelvin_to_fahrenheit(k):
    """
    Convert temperature from Kelvin to Fahrenheit.
    
    Formula: (K - 273.15) × 9/5 + 32 = °F
    """
    return (k - 273.15) * 9/5 + 32