import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python bmi.py (1) Metric (m, kg) or (2) Non-Metric (ft, pounds)")
        sys.exit(1)

    chosen_system = sys.argv[1]
    if chosen_system not in ['1', '2']:
        print("Invalid choice. Please choose (1) Metric (m, kg) or (2) Non-Metric (ft, pounds)")
        sys.exit(1)

    # Rest of your code here
    print(f"You have chosen: {'Metric' if chosen_system == '1' else 'Non-Metric'}")

if __name__ == "__main__":
    main()
