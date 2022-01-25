# How To Use the Migration Tool

1. Pre-Setup: Installing the necessary software to run the program
    - Download Python, if not already installed
        1. Go to https://www.python.org/downloads/macos/
        2. Download the latest release of Python for macOS (should be 3.10.2, but any version of Python3 works)
    - Download the necessary Python libraries to run the program, if not already installed
        1. Now that Python3 is installed, open a window in _Terminal_.
        2. Type in "pip3 install numpy", and you should see a bunch of text popping up illustrating the library's installation. Once complete, type in "pip3 install pandas", and you should see the same installation process, but for another library.
        3. Once both of these are installed, you are now ready to run the program.

2. Setup: Designate a folder to contain the program along with the data files before proceeding.

3. Click on the green **Code** button on this page, and then click _Download Zip_.
    - In the downloaded zip folder you should see a file called `dancesupplies.py`. This is the program to combine the CSV files.
      
4. Take the program and move it to the folder with both the data and the rewards spreadsheets. 
    - In order for the program to work properly, both the data and rewards files need to be _.csv_ files. In order to do this, enter the spreadsheet you would like to make a CSV copy of:
        - Click "File"
        - Click "Save As"
        - Open the _File Format_ drop-down menu and choose "CSV UTF-8 (Comma-Delimited) (.csv)"
        - Then save to the designated folder.

5. In order for the program to run on the files you want, you will need to open the program and change the filenames. The place to read in the data csv file and rewards csv file is in the beginning of the program, and it looks like this:
```
# Read in the CSV File with the rewards numbers and points
    rewards = pd.read_csv("rewards.csv")

    # Read in the CSV File with the customer information
    data = pd.read_csv("testdata.csv")

``` 
  Change the filenames from "rewards.csv" and "testdata.csv" to the desired filenames (keep the quotes around the names)

6. Once the file is updated to read your desired files, open the terminal window again.
    - Navigate to the designated folder that you created in the setup
    - Once you are in the designated folder, enter "python3 dancesupplies.py"
    - If all goes well, you should see a _.csv_ file pop up in the folder called "migration.csv" and "flagged_numbers.csv"

7. You're done!