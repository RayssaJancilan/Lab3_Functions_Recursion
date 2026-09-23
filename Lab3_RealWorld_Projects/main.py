

import logic

import functools
import random


# STUDENT-SPECIFIC CONFIGURATION
LAST_NAME = "JANCILAN"
SEED_NUM = "8"
FAVORITE_ARTIST = "THE 1975"

# DECORATOR FOR LOGGING & RECORDING

def log_diagnostic(func):
    """Decorator to record and log the diagnostic process of a function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing: {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} execution completed successfully.\n")
        return result

    return wrapper

# MAIN RUNNER WITH EXCEPTION HANDLING & SUMMARY
@log_diagnostic
def run_diagnostic_system():
    readings_list = logic.generate_equipment_readings(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)

    processed_summary = []
    error_logs = []

    print("--- Starting Equipment Scan ---")
    for item in readings_list:
        eq_id = item["id"]
        val = item["voltage"]

        try:
            logic.validate_reading(val)

            
            dev = logic.calculate_deviation(val)
            condition = logic.classify_condition(dev)

            processed_summary.append(
                {"id": eq_id, "reading": f"{val}V", "deviation": f"{dev:+}V", "status": condition}
            )

        except (TypeError, ValueError) as error:
            error_logs.append({"id": eq_id, "raw_value": val, "reason": str(error)})

    print("\n================ DIAGNOSTIC SUMMARY REPORT ================")
    print(f"Student Meta | Profile: {LAST_NAME} | Seed: {SEED_NUM} | Artist: {FAVORITE_ARTIST}")
    print("-----------------------------------------------------------")
    print(f"{'Equipment ID':<15} | {'Reading':<10} | {'Deviation':<10} | {'Status'}")
    print("-----------------------------------------------------------")

    for report in processed_summary:
        print(
            f"{report['id']:<15} | {report['reading']:<10} | {report['deviation']:<10} | {report['status']}"
        )

    print("\n------------------- SYSTEM ERROR LOGS ---------------------")
    if error_logs:
        for err in error_logs:
            print(f"[WARNING] {err['id']} failed validation (Value: {err['raw_value']}) -> {err['reason']}")
    else:
        print("No errors detected during processing.")
    print("===========================================================")

if __name__ == "__main__":
    run_diagnostic_system()
