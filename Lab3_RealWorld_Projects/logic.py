
import random


def generate_equipment_readings(last_name, seed_num, favorite_artist):
    """Generates student-specific mock equipment readings based on inputs."""
    combined_seed = sum(ord(char) for char in last_name + favorite_artist) + int(8)
    random.seed(combined_seed) 

    raw_data = [
        {"id": f"EQ-{i+101}", "voltage": random.choice([210, 220, 230, 245, "invalid", 180, None])} # type: ignore
        for i in range(7)
    ]
    return raw_data


def validate_reading(reading):
    """Validates if the reading format and values are correct.

    Raises custom exceptions if invalid data is found.
    """
    if not isinstance(reading, (int, float)):
        raise TypeError(f"Invalid data type encountered: {type(reading).__name__}")

    if reading < 190 or reading > 240:
        raise ValueError(f"Reading {reading}V is outside safe operational boundaries (190V-240V).")

    return True


def calculate_deviation(reading, standard=220):
    """Calculates the voltage deviation from a standard reference level (220V)."""
    return reading - standard


def classify_condition(deviation):
    """Classifies the equipment condition based on voltage deviation."""
    if abs(deviation) == 0:
        return "Optimal"
    elif abs(deviation) <= 10:
        return "Normal"
    else:
        return "Critical Attention Required"
