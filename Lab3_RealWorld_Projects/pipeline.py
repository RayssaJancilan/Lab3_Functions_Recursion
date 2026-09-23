# pipeline_monitor.py
import time
import telemetry

def monitor_performance(func):
    """Decorator that measures execution time and logs function activity."""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"\n[DECORATOR] Starting processing via function: '{func.__name__}'")
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"[DECORATOR] Finished '{func.__name__}' in {end_time - start_time:.6f} seconds.")
        return result
    return wrapper


def trace_abnormal_chain(reading, history_list, depth=0):
    """
    Recursively analyzes a chain of abnormal behavior or logs diagnostic depth.
    Base condition: stops when depth reaches a threshold or reading normalizes.
    """
    
    if depth >= 3:
        return f"Critical Alert: Persistent abnormal condition verified at depth {depth}."
    
    if reading > 150:
        history_list.append(f"Level-{depth} Check: Value {reading} exceeds standard thresholds.")
        return trace_abnormal_chain(reading - 10, history_list, depth + 1)
    else:
        return "Abnormal surge resolved during standard validation trace."


@monitor_performance 
def run_equipment_pipeline(last_name: str, seed_num: int, favorite_artist: str):
    """
    Requirement 2 & 8: Coordinates the modular pipeline, tracks metrics,
    and returns a final structured diagnostic report dictionary.
    """
    
    metrics = {
        "processed": 0,
        "valid": 0,
        "invalid": 0,
        "abnormal_detected": 0
    }
    
    diagnostic_logs = []
    normalize_value = lambda val: val * 1.05 
    
    telemetry_stream = telemetry.generate_telemetry(last_name, seed_num, favorite_artist)
    
    for raw_data in telemetry_stream:
        metrics["processed"] += 1
        
        try:
            if isinstance(raw_data, str):
                raise telemetry.InvalidTelemetryError(f"Unexpected string signature encountered: {raw_data}")
            
            metrics["valid"] += 1
            
            processed_val = normalize_value(raw_data)
            
            if processed_val > 120:
                metrics["abnormal_detected"] += 1
                trace_history = []
                
                alert_msg = trace_abnormal_chain(processed_val, trace_history)
                diagnostic_logs.append({
                    "reading_index": metrics["processed"],
                    "value": processed_val,
                    "status": "ABNORMAL",
                    "trace": trace_history,
                    "summary": alert_msg
                })
            else:
                diagnostic_logs.append({
                    "reading_index": metrics["processed"],
                    "value": processed_val,
                    "status": "NORMAL"
                })
                
        except telemetry.InvalidTelemetryError as e:
            metrics["invalid"] += 1
            diagnostic_logs.append({
                "reading_index": metrics["processed"],
                "value": raw_data,
                "status": f"INVALID_ERROR: {e}"
            })

    return metrics, diagnostic_logs


if __name__ == "__main__":
    STUDENT_LAST_NAME = "JANCILAN"
    STUDENT_SEED_NUM = "8"
    STUDENT_FAVORITE_ARTIST = "THE 1975"
    
    metrics_summary, logs = run_equipment_pipeline(
        last_name=STUDENT_LAST_NAME,
        seed_num=STUDENT_SEED_NUM,
        favorite_artist=STUDENT_FAVORITE_ARTIST
    )
    
    print("\n" + "="*50)
    print("           FINAL DIAGNOSTIC REPORT")
    print("="*50)
    print(f"Total Processed Readings : {metrics_summary['processed']}")
    print(f"Valid Readings Recorded  : {metrics_summary['valid']}")
    print(f"Invalid Readings Deflected: {metrics_summary['invalid']}")
    print(f"Abnormal Events Flagged   : {metrics_summary['abnormal_detected']}")
    print("="*50)
    
    print("\nDetailed Diagnostic Log Preview:")
    for log in logs[:10]:
        if "INVALID" in log['status'] or log['status'] == "ABNORMAL":
            print(f" -> Item {log['reading_index']}: [{log['status']}] - Val: {log['value']}")
            if "trace" in log:
                for step in log['trace']:
                    print(f"    └── {step}")
                print(f"    └── Result: {log['summary']}")
        else:
            print(f" -> Item {log['reading_index']}: [NORMAL] - Regulated Val: {log['value']:.2f}")
