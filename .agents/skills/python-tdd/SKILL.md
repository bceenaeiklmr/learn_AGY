---
name: python-tdd
description: >-
  Use this skill when the user asks to implement a Python feature, fix a bug using test-driven development (TDD), or run automated pytest suites.
---

# Python Test-Driven Development (TDD) Workflow

This skill ensures reliable, regression-free implementation by enforcing a test-first cycle.

## Procedure

1. **Step 1: Write the Failing Test (Red)**
   - Create or update tests in `test_<module>.py`.
   - Explicitly define the expected behavior and edge cases before modifying production code.
   - Run the test runner script:
     ```powershell
     python .agents/skills/python-tdd/scripts/test_runner.py <target_path>
     ```
   - Confirm that the test **fails for the expected reason** (reproduction confirmed).

2. **Step 2: Implement the Minimum Code (Green)**
   - Write the simplest code that makes the test pass.
   - Do not add speculative features or unnecessary abstractions.
   - Re-run the test runner:
     ```powershell
     python .agents/skills/python-tdd/scripts/test_runner.py <target_path>
     ```
   - Confirm all tests pass.

3. **Step 3: Refactor & Clean Up**
   - Clean up any temporary debug code.
   - Verify typing and PEP 8 compliance.
   - Re-run tests to ensure no regressions were introduced.
