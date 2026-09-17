   # File Risk Analyzer

A simple Python script that evaluates the security risk level of a file based on its size, entropy, and source trustworthiness.

## Bug Fix Alert
The original script contained logical bugs where `file_size` was incorrectly compared against string values (`"no"` and `"high"`) instead of checking the `source_trusted` and `entropy` variables. This README reflects the corrected logic.

## Risk Logic Matrix

| Criteria | Condition | Risk Points |
| :--- | :--- | :--- |
| **File Size** | > 500 MB | +1 Point |
| **Untrusted Source** | `"no"` | +2 Points |
| **High Entropy** | `"high"` | +2 Points |

### Risk Classification
* **High Risk:** $\ge$ 4 Points
* **Medium Risk:** 2 to 3 Points
* **Low Risk:** < 2 Points

## Corrected Implementation

```python
# User Input
file_name = input("Enter file name: ")
file_size = int(input("Enter file size (MB): "))
entropy = input("Enter Entropy (Low / High): ").lower()
source_trusted = input("Is this source trusted (Yes / No): ").lower()

# Display Input Details
print("\n--- File Summary ---")
print("File name:", file_name)
print("Size:", file_size, "MB")
print("Trusted source:", source_trusted)
print("Entropy:", entropy)

# Risk Calculation Logic
risk_score = 0

if file_size > 500:
    risk_score += 1

if source_trusted == "no":
    risk_score += 2

if entropy == "high":
    risk_score += 2

# Evaluation
print("\n--- Risk Assessment ---")
if risk_score >= 4:
    print("Result: High Risk")
elif risk_score >= 2:
    print("Result: Medium Risk")
else:
    print("Result: Low Risk")
```

## How to Run
1. Ensure you have **Python 3.x** installed.
2. Save the code into a file named `risk_analyzer.py`.
3. Run the script via your terminal:
   ```bash
   python risk_analyzer.py
   ```
