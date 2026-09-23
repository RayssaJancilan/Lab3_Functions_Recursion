import hashlib

# STUDENT CONFIGURATION 
SURNAME = "JANCILAN"
SEED_NUM = "8"
FAVORITE_ARTIST = "THE 1975"

def generate_initial_fault_code(surname: str, seed_num: int, favorite_artist: str) -> int:
    """
    Generates a unique numeric starting fault code based on student inputs.
    """
    combined_input = f"{surname.upper()}_{seed_num}_{favorite_artist.upper()}"
    
    
    hash_object = hashlib.md5(combined_input.encode())
    numeric_code = int(hash_object.hexdigest(), 16) % 90000 + 10000
    return numeric_code

def recursive_fault_trace(fault_code: int, depth: int = 1) -> list:
    """
    Recursively traces the fault code, altering it at each level 
    until a defined termination condition is met.
    """
    print(f"[Level {depth}] Current Fault Code: {fault_code}")
    
    # DEFINED TERMINATION CONDITIONS 
    if fault_code <= 10:
        print(f"--> Target termination reached at Level {depth}! Fault Isolated.")
        return [fault_code]
    
    if depth >= 15:
        print(f"--> Maximum diagnostic depth reached! Truncating trace.")
        return [fault_code]
    
    if fault_code % 2 == 0:
        next_code = fault_code // 2
    else:
        next_code = (fault_code * 3 + 1) // 10  
        
    
    if next_code == fault_code:
        next_code -= 1

    return [fault_code] + recursive_fault_trace(next_code, depth + 1)


print("--- Initializing Control System Diagnostic ---")
start_code = generate_initial_fault_code(SURNAME, SEED_NUM, FAVORITE_ARTIST)
print(f"Generated Student Fault Code: {start_code}\n")

print("--- Starting Recursive Fault Trace ---")
diagnostic_sequence = recursive_fault_trace(start_code)

print("\n--- Final Diagnostic Report ---")
print(f"Complete Fault Path Sequence: {diagnostic_sequence}")
