import Lab2.bmi as bmi
import pytest
from Lab2.bmi import calculate_bmi

def test_bmi_under_weight():
    # Test case for underweight classification
    bmi_value, classification = bmi.calculate_bmi(weight=50, height=1.8)  # BMI = 15.43
    assert classification == -1, f"Expected -1 for underweight, but got {classification}"

def test_bmi_normal_weight():
    # Test case for normal weight classification
    bmi_value, classification = bmi.calculate_bmi(weight=70, height=1.75)  # BMI = 22.86
    assert classification == 0, f"Expected 0 for normal weight, but got {classification}"

def test_bmi_over_weight():
    # Test case for overweight classification
    bmi_value, classification = bmi.calculate_bmi(weight=85, height=1.75)  # BMI = 27.76
    assert classification == 1, f"Expected 1 for overweight, but got {classification}"
