# Landing Burn Calculator

Calculates the constant throttle required for a suicide burn given the velocity, mass, and altitude of the vehicle at the start of engine ignition.

JavaScript based web version on [my website](https://daszeal.github.io/tools/landing-burn-calculator).

## Requirements

- Python 3.8 or higher
- pip (usually comes with Python)

## Installation

1. **Download the code**
   - Click "Code" > "Download ZIP" on GitHub, or clone with Git:
   ```
   git clone <repository-url>
   cd "Landing Burn Constant Throttle"
   ```

2. **Install Python** (if not already installed)
   - Visit https://www.python.org/downloads/
   - Download Python 3.8 or higher
   - During installation, **CHECK the box "Add Python to PATH"**
   - Verify installation by opening a terminal and typing: `python --version`

## Usage

### Option 1: Edit Variables in calculator.py (Recommended for Single Calculations)

1. Open `calculator.py` in a text editor
2. Edit the variables at the top of the file based on the current vehicle status
3. Save the file
4. Open a terminal in the project folder and run:
   ```bash
   python3 calculator.py
   ```
5. Results display in the terminal

### Option 2: Interactive CLI (cli.py)

For interactive prompts, use the CLI version:

#### macOS/Linux
```bash
python3 cli.py
```

#### Windows
Open Command Prompt in the project folder and type:
```
python3 cli.py
```

You'll be prompted to enter each value, with defaults provided for optional parameters.

## Input Parameters

### Required Fields
- **Mode**: Earth, Kerbin, or Vacuum
- **Current Velocity** (m/s): Starting velocity of the vehicle
- **Current Height** (m): Starting altitude
- **Current Mass** (tons): Total mass including current fuel reserves
- **Dry Mass** (tons): Mass with all the tanks empty, measured before launch
- **Max Thrust** (kN): Maximum engine thrust
- **Isp** (s): Engine specific impulse

### Conditional Fields
- **Diameter** (m): Only required for Earth/Kerbin modes (needed for drag calculation)

### Optional Fields
- **Gravity** (m/s²): Defaults to 9.8
- **Drag Coefficient** (Cd): Defaults to 1.0

## Troubleshooting

### "Python not found"
- Verify Python is installed: Open terminal and type `python --version`
- If not installed, download from https://www.python.org
- **Important**: During installation, check "Add Python to PATH"

### "Module not found"
- Make sure `requirements.txt` is in the same folder as the scripts
- Install dependencies: `pip install -r requirements.txt`
- Delete the `__pycache__` folder if it exists and try again

## Files in This Project

- `calculator.py` - Core calculation engine + terminal output (edit variables and run)
- `cli.py` - Interactive command-line interface
- `requirements.txt` - Python dependencies (just numpy)

## Output

The calculator returns:
- **Throttle**: Optimal throttle setting for soft landing
- **Throttle (Kerbal)**: Equivalent navball throttle in Kerbal Space Program 
- **Burn Time**: Duration of burn in seconds
- **Final Mass**: Mass remaining at landing
- **Average Drag**: Average drag force during descent
- **Warnings**: Any issues with the selected parameters

*README produced by Claude Haiku 4.5*