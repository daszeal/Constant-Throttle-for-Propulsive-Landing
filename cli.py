import calculator
import sys

def get_input(prompt, input_type=float, default=None):
    """Get validated user input."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input and default is not None:
                return default
            if not user_input:
                print("  Error: Input cannot be empty")
                continue
            value = input_type(user_input)
            if value <= 0:
                print("  Error: Value must be positive")
                continue
            return value
        except ValueError:
            print(f"  Error: Please enter a valid {input_type.__name__}")

def get_mode():
    """Get and validate mode selection."""
    modes = {"1": "earth", "2": "kerbin", "3": "vacuum"}
    print("\nSelect Mode:")
    print("  1. Earth (with atmosphere)")
    print("  2. Kerbin (with atmosphere)")
    print("  3. Vacuum (no atmosphere)")
    while True:
        choice = input("Enter choice (1-3): ").strip()
        if choice in modes:
            return modes[choice]
        print("  Error: Please enter 1, 2, or 3")

def main():
    print("=" * 60)
    print("Landing Burn Calculator (Constant Throttle)")
    print("=" * 60)
    
    try:
        # Get mode
        mode = get_mode()
        
        # Required inputs
        print("\nEnter Spacecraft Parameters:")
        print("(All fields are required unless marked optional)\n")
        
        v0 = get_input("Initial Velocity (m/s): ", float)
        h0 = get_input("Initial Height (m): ", float)
        m0_tons = get_input("Initial Mass (tons): ", float)
        m_dry_tons = get_input("Dry Mass (tons): ", float)
        
        # Validate mass ratio
        if m_dry_tons >= m0_tons:
            print("Error: Dry mass must be less than initial mass")
            return
        
        thrust_max_kN = get_input("Max Thrust (kN): ", float)
        Isp_sl = get_input("Isp (sea level/vacuum): ", float)
        
        # Conditional input based on mode
        if mode == "vacuum":
            diameter = 1.0  # Placeholder for vacuum mode
            print("(Diameter not required for vacuum mode)")
        else:
            diameter = get_input("Diameter (m): ", float)
        
        # Optional inputs with defaults
        print("\nOptional parameters (press Enter to use defaults):\n")
        gravity = get_input("Gravity (m/s²) [default 9.8]: ", float, default=9.8)
        Cd = get_input("Drag Coefficient (Cd) [default 1.0]: ", float, default=1.0)
        
        print("\nCalculating...")
        result = calculator.compute(mode, v0, h0, m0_tons, m_dry_tons, thrust_max_kN, Isp_sl, diameter, gravity, Cd)
        
        # Display results
        print("\n" + "=" * 60)
        print("LANDING BURN CALCULATOR - RESULTS")
        print("=" * 60)
        print(f"\nMode:           {mode.upper()}")
        print(f"Status:         {result['status'].upper()}")
        print(f"\nThrottle:       {result['throttle']} ({result['throttle_percent']}%)")
        print(f"  Kerbal:      {result['throttle_kerbal']} (on 0-15 scale)")
        print(f"\nBurn Time:      {result['burn_time']} seconds")
        print(f"Final Mass:     {result['m_final']} tons")
        print(f"Average Drag:   {result['average_drag']} N")
        
        if result['warnings']:
            print("\n" + "-" * 60)
            print("WARNINGS:")
            for warning in result['warnings']:
                print(f"\n  {warning}")
        
        print("\n" + "=" * 60)
        
    except KeyboardInterrupt:
        print("\n\nCalculation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
