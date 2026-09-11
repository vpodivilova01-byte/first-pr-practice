"""Simple temperature conversion helpers."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert degrees Celsius to degrees Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert degrees Fahrenheit to degrees Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius: float) -> float:
    """Convert degrees Celsius to kelvin."""
    return celsius + 273.15
