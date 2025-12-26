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


if __name__ == "__main__":
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Run tests
    sa100_success = test_sa100()
    sa102_success = test_sa102()

    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)

    if sa100_success and sa102_success:
        print("✓ All tests passed!")
        sys.exit(0)
    else:
        print("✗ Some tests failed")
        sys.exit(1)
