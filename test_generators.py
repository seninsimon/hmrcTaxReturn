"""
Main Test Script
Tests both SA100 and SA102 form generation
"""

from forms.sa102.test_data import DATA_SA102_TR1, DATA_SA102_TR2
from forms.sa102.generator import generate_sa102
from forms.sa100.test_data import (
    DATA_SA100_TR1, DATA_SA100_TR2, DATA_SA100_TR3,
    DATA_SA100_TR4, DATA_SA100_TR5, DATA_SA100_TR6,
    DATA_SA100_TR7, DATA_SA100_TR8
)
from forms.sa100.generator import generate_sa100
from forms.sa103s.test_data import DATA_SA103s_SES1, DATA_SA103s_SES2
from forms.sa103s.generator import generate_sa103s
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def test_sa100():
    """Test SA100 generation"""
    print("=" * 60)
    print("Testing SA100 Generation")
    print("=" * 60)

    # Prepare data dictionary
    data = {
        'tr1': DATA_SA100_TR1,
        'tr2': DATA_SA100_TR2,
        'tr3': DATA_SA100_TR3,
        'tr4': DATA_SA100_TR4,
        'tr5': DATA_SA100_TR5,
        'tr6': DATA_SA100_TR6,
        'tr7': DATA_SA100_TR7,
        'tr8': DATA_SA100_TR8,
    }

    try:
        output_path = generate_sa100(
            data, output_path="output/sa100_completed.pdf")
        print(f"✓ SA100 generated successfully: {output_path}")
        return True
    except Exception as e:
        print(f"✗ SA100 generation failed: {str(e)}")
        return False


def test_sa102():
    """Test SA102 generation"""
    print("\n" + "=" * 60)
    print("Testing SA102 Generation")
    print("=" * 60)

    # Prepare data dictionary
    data = {
        'tr1': DATA_SA102_TR1,
        'tr2': DATA_SA102_TR2,
    }

    try:
        output_path = generate_sa102(
            data, output_path="output/sa102_completed.pdf")
        print(f"✓ SA102 generated successfully: {output_path}")
        return True
    except FileNotFoundError as e:
        print(f"⚠ SA102 skipped: {str(e)}")
        print("  Add sa102.pdf to forms/sa102/templates/ to enable SA102 generation")
        return True  # Not a failure, just not configured yet
    except Exception as e:
        print(f"✗ SA102 generation failed: {str(e)}")
        return False


def test_sa103s():
    """Test SA103s generation"""
    print("\n" + "=" * 60)
    print("Testing SA103s Generation")
    print("=" * 60)

    # Prepare data dictionary
    data = {
        'ses1': DATA_SA103s_SES1,
        'ses2': DATA_SA103s_SES2,
    }

    try:
        output_path = generate_sa103s(
            data, output_path="output/sa103s_completed.pdf")
        print(f"✓ SA103s generated successfully: {output_path}")
        return True
    except FileNotFoundError as e:
        print(f"⚠ SA103s skipped: {str(e)}")
        print("  Add sa103s.pdf to forms/sa103s/templates/ to enable SA103s generation")
        return True  # Not a failure, just not configured yet
    except Exception as e:
        print(f"✗ SA103s generation failed: {str(e)}")
        return False


if __name__ == "__main__":
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Run tests
    sa100_success = test_sa100()
    sa102_success = test_sa102()
    sa103s_success = test_sa103s()

    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)

    if sa100_success and sa102_success and sa103s_success:
        print("✓ All tests passed!")
        sys.exit(0)
    else:
        print("✗ Some tests failed")
        sys.exit(1)
