YData Profiling Script - Instructions

Instructions for using the YData Profiling Script (profiling.py) to generate a summary report of a CSV dataset. Follow these steps to install the necessary components and run the script on both Windows and macOS.


1. Install Python
Download and install Python from https://www.python.org/downloads/.
Follow the installation instructions, and ensure that the option to "Add Python to PATH" is checked during installation.
Verify Python Installation:
Open your terminal (Command Prompt on Windows, Terminal on macOS).
Type the following command and hit Enter:
python3 --version
If installed correctly, this should display the version number of Python installed (e.g., Python 3.10.2).
2. Install Required Libraries
In your terminal, install the necessary Python libraries (Pandas and YData Profiling) by following these commands:

Install Pandas (Python Data Analysis Library)

In the terminal, type:
pip install pandas
If you see an error, try:
pip3 install pandas
Install YData Profiling

In the terminal, type:
pip install ydata-profiling
If you encounter issues, try:
pip3 install ydata-profiling
3. Run the Profiling Script
Download the profiling.py script to your computer.
Run the Script:
Open the terminal and type python (leave a space after python).
Drag and drop the profiling.py script into the terminal window.
On macOS, this might look like:
python /Users/YourUsername/Downloads/profiling.py
Press Enter.
Select Dataset File:
After a few moments, you should see a prompt to select your dataset. Browse and select a CSV file (.csv) from your computer.
Enter Report Title:
The script will prompt you to enter a title for the report. Type a title and press Enter.
Generate Report:
The script will load and analyze the dataset. It will generate a profiling report saved in the same folder as the profiling.py script. Look for a file named [your title]_profile_report.html.
