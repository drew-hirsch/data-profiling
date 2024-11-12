# YData Profiling Script - Instructions

Follow the steps below to install the necessary components and run the **YData Profiling Script (profiling.py)** on both Windows and macOS to generate a summary report of a CSV dataset.

## 1. Install Python

1. Download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).  
2. Follow the installation instructions, and ensure that the option to **"Add Python to PATH"** is checked during installation.  
3. **Verify Python Installation**:
   - Open your terminal (Command Prompt on Windows, Terminal on macOS).
   - Type the following command and hit Enter:
     ```
     python3 --version
     ```
   - If installed correctly, this should display the version number of Python installed (e.g., `Python 3.10.2`).

## 2. Install Required Libraries

### Install Pandas (Python Data Analysis Library)

1. In the terminal, type: pip install pandas
         If you encounter an error, try: pip3 install pandas

### Install YData Profiling

1. In the terminal, type: pip install ydata-profiling
         If you encounter an error, try: pip3 install ydata-profiling

   
## 3. Run the Profiling Script

1. **Download** the `profiling.py` script to your computer.
2. **Run the Script**:
- Open the terminal and type `python` (leave a space after `python`).
- Drag and drop the `profiling.py` script into the terminal window.
  - On macOS, this might look like:
    ```
    python /Users/YourUsername/Downloads/profiling.py
    ```
- Press Enter.

3. **Select Dataset File**: 
- After a few moments, you will be prompted to select your dataset.
- Browse and select a CSV file (`.csv`) from your computer.

4. **Enter Report Title**: 
- The script will prompt you to enter a title for the report.
- Type a title and press Enter.

5. **Generate Report**: 
- The script will load and analyze the dataset.
- It will generate a profiling report saved in the same folder as the `profiling.py` script.
- Look for a file named `[your title]_profile_report.html`.
