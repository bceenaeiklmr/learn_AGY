"""
Deterministic Python Test Runner Script for Agy Skills.
Executes pytest and outputs a clean JSON summary for agent digestion.
"""

import json
import subprocess
import sys
from pathlib import Path


def run_tests(target_dir: str = ".") -> int:
    cmd = [sys.executable, "-m", "pytest", target_dir, "-q", "--tb=short"]
    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60,
        )
        passed = proc.returncode == 0
        summary = {
            "status": "PASS" if passed else "FAIL",
            "returncode": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
        }
        print(json.dumps(summary, indent=2))
        return proc.returncode
    except subprocess.TimeoutExpired:
        print(json.dumps({"status": "TIMEOUT", "error": "Tests exceeded 60s limit"}, indent=2))
        return 124
    except Exception as e:
        print(json.dumps({"status": "ERROR", "error": str(e)}, indent=2))
        return 1


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(run_tests(target))
