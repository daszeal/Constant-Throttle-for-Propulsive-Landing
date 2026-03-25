import numpy as np

# VARIABLES - User Input
# Edit these values to change the calculation

## Required
mode = "earth" # "vacuum", "earth", or "kerbin"
v0 = 250 # m/s
h0 = 1500 # m
m0_tons = 30 # tons
m_dry_tons = 20 # tons
thrust_max_kN = 845 # kN
Isp_sl = 282 # sec

## Conditional
diameter = 3.7 # m

## Optional
gravity = 9.8 # m/s^2
Cd = 1.1 # Drag coefficient

# COMPUTATION FUNCTION
def compute(mode, v0, h0, m0_tons, m_dry_tons, thrust_max_kN, Isp_sl, diameter, gravity, Cd):
    
    dt = 0.02 
    max_time = 120.0 
    g0 = 9.80665 
    
    m0 = m0_tons * 1000 
    m_dry = m_dry_tons * 1000 
    thrust_max = thrust_max_kN * 1000
    
    A = np.pi * (diameter / 2)**2 
    
    def atm(h): 
        
        if mode == "vacuum":
            return 0.0
        
        elif mode == "earth":
            return 1.225 * np.exp(-h / 8500)
        
        elif mode == "kerbin":
            return 1.225 * np.exp(-h / 5000)
        
    def simulate(throttle):
        h = h0
        v = v0
        m = m0
        t = 0.0
        drag_impulse = 0.0 

        while h > 0 and t < max_time:
            rho = atm(h)
            drag = 0.5 * rho * Cd * A * v**2 

            thrust = throttle * thrust_max 
            mdot = thrust / (Isp_sl * g0) if thrust > 0 else 0 

            a = gravity - (thrust + np.sign(v) * drag) / m 

            delta_v = v + a * dt 
            delta_h = h - (v + delta_v) / 2 * dt

            drag_impulse += drag * dt 

            m = max(m - mdot * dt, m_dry) 

            v = delta_v
            h = delta_h
            t += dt

        if h <= 0:
            avg_v = (v + delta_v) / 2
            vf = v - (h / avg_v) * a if avg_v != 0 else v
        else:
            vf = v

        avg_drag = drag_impulse / t if t > 0 else 0

        return vf, avg_drag, t, m

    low = 0.0
    high = 1.0

    for _ in range(50):
            mid = (low + high) / 2
            vf, _, _, _ = simulate(mid)
            if vf > 0:
                low = mid
            else:
                high = mid

    best_throttle = (low + high) / 2
    vf, avg_drag, burn_time, final_mass = simulate(best_throttle)

    warnings = []

    if best_throttle < 0.4:
        warnings.append("WARNING: LOW THROTTLE\n"
                        "Most real life engines cannot throttle this low.\n"
                        "Use at your own risk.")

    vf_at_max, _, _, _ = simulate(1.0)
    if vf_at_max > 0:
        warnings.append("CRITICAL WARNING: THRUST TOO LOW!\n"
                        "Firing engines at full throttle will still result in lithobreaking :(\n"
                        "Prepare for a Rapid Unscheduled Disassembly.")

    final_mass_tons = final_mass / 1000

    result = {
            "throttle": round(best_throttle, 3),
            "throttle_percent": round(best_throttle * 100, 1),
            "throttle_kerbal": round(best_throttle * 15, 2),
            "burn_time": round(burn_time, 1),
            "m_final": round(final_mass_tons, 0),
            "average_drag": round(avg_drag, 0), 
            "warnings": warnings,
            "status": "success" if not warnings else "warning"
        }

    return result

# RESULT DISPLAY
if __name__ == "__main__":

    result = compute(mode, v0, h0, m0_tons, m_dry_tons, thrust_max_kN, Isp_sl, diameter, gravity, Cd)
    
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