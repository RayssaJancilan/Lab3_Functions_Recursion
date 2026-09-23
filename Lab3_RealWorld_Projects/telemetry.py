# telemetry_generator.py
import random

class InvalidTelemetryError(Exception):
    """Custom exception for invalid or corrupted telemetry values."""
    pass

def generate_telemetry(last_name: str, seed_num: int, favorite_artist: str):
    """
    Requirement 1 & 3: Generates student-specific telemetry using a generator.
    Produces values one by one without storing the complete stream in memory.
    """
   
    unique_seed = sum(ord(c) for c in last_name + favorite_artist) + int(8)
    random.seed(unique_seed)
    
    print(f"[INFO] Initializing telemetry stream with seed modifier: {unique_seed}")
    
    
    for i in range(1, 21):
        roll = random.random()
        
        if roll < 0.15:
            yield "CORRUPTED_DATA"
        elif roll < 0.35:
            yield random.randint(150, 200)
        else:
            yield random.randint(20, 100)
