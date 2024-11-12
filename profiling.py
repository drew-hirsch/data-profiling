import os
import subprocess
import sys

# Function to install a package if it's not already installed
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check and install required packages
try:
    import pandas as pd
except ImportError:
    print("Pandas not found. Installing...")
    install_package("pandas")
    import pandas as pd

try:
    from ydata_profiling import ProfileReport
except ImportError:
    print("ydata-profiling not found. Installing...")
    install_package("ydata-profiling")
    from ydata_profiling import ProfileReport

# Tkinter is usually included with Python installations, but it's good to confirm
try:
    from tkinter import Tk, filedialog
except ImportError:
    print("Tkinter not found. Please install Tkinter manually, as it's usually included with your Python installation.")
    sys.exit(1)  # Exit if Tkinter is missing, as it requires manual installation on some systems

# Function to select the file using tkinter file dialog
def select_file():
    Tk().withdraw()  # Initialize Tkinter and hide the root window
    print("Please select your dataset file.")
    
    # Open file dialog and prompt user to select a file
    file_path = filedialog.askopenfilename(
        title="Select Dataset",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    
    if not file_path:
        print("No file selected. Exiting program.")
        return None
    else:
        print(f"Selected file: {file_path}")
        return file_path

# Function to get report title from user
def get_report_title():
    report_title = input("Enter a title for your YData profiling report: ")
    return report_title

# Function to generate profiling report
def generate_report(dataset_path, report_title):
    try:
        # Load the dataset
        data = pd.read_csv(dataset_path)
        print("Dataset loaded successfully.")
        
        # Generate the profiling report
        profile = ProfileReport(data, title=report_title, explorative=True)
        
        # Save the report in the same directory as the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        report_file = os.path.join(script_dir, report_title.replace(" ", "_").lower() + "_profile_report.html")
        profile.to_file(report_file)
        
        print(f"Report generated successfully! Check the file: {report_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please make sure the dataset is in CSV format and contains valid data.")

if __name__ == "__main__":
    dataset_path = select_file()
    if dataset_path:
        report_title = get_report_title()
        generate_report(dataset_path, report_title)
