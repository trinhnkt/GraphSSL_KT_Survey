import os
import re

AUDIT_DIR = os.path.join(os.path.dirname(__file__), '..', 'audit')
STATUS_FILE = os.path.join(os.path.dirname(__file__), '..', 'status', 'ready_for_A15.md')

def get_status(audit_path):
    try:
        with open(audit_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith('**Status:**'):
                    # Extract the word after the colon
                    match = re.search(r'\*\*Status:\*\*\s*(\w+)', line)
                    if match:
                        return match.group(1).upper()
    except Exception:
        pass
    return 'UNKNOWN'

def main():
    # Gather statuses for F1-F9
    results = {}
    for entry in os.listdir(AUDIT_DIR):
        if entry.lower().endswith('.md'):
            path = os.path.join(AUDIT_DIR, entry)
            status = get_status(path)
            results[entry] = status
    all_pass = all(s == 'PASS' for s in results.values())
    # Ensure status directory exists
    os.makedirs(os.path.dirname(STATUS_FILE), exist_ok=True)
    with open(STATUS_FILE, 'w', encoding='utf-8') as out:
        if all_pass:
            out.write('READY_FOR_FINAL_A15 = YES\n')
        else:
            out.write('READY_FOR_FINAL_A15 = NO\n')
            out.write('Failing tasks:\n')
            for file, stat in results.items():
                if stat != 'PASS':
                    out.write(f"- {file}: {stat}\n")
    # Also update the gate audit file status line
    gate_path = os.path.join(AUDIT_DIR, 'F9_PRE_A15_GATE.md')
    if os.path.exists(gate_path):
        # Replace the line with **Status:**
        with open(gate_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        with open(gate_path, 'w', encoding='utf-8') as f:
            for line in lines:
                if line.strip().startswith('**Status:**'):
                    new_status = 'PASS' if all_pass else 'FAIL'
                    f.write(f"**Status:** {new_status}\n")
                else:
                    f.write(line)
    print('Gate check completed. Ready for A15:', 'YES' if all_pass else 'NO')

if __name__ == '__main__':
    main()
