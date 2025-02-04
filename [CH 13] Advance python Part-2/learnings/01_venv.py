# here is the explanation of virtual environment what i learnt 

"""
A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages.

Usage:

1. Create a virtual environment:
    
    python -m venv myenv
    
   This command creates a directory named `myenv` that contains the virtual environment. 
   Inside this directory, you will find a copy of the Python interpreter and the standard library, 
   along with various supporting files.

2. Activate the virtual environment:
    - On Windows:
        
        myenv\Scripts\activate
        
      This command activates the virtual environment. After activation, your command prompt will change to indicate that you are now working inside the virtual environment.
    

3. Install packages using pip:
    
    pip install package_name
    
   This command installs a package named `package_name` in the virtual environment. You can install multiple packages by listing them separated by spaces. For example:
    
    pip install package1 package2
    

4. Deactivate the virtual environment when done:
    
    deactivate

   This command deactivates the virtual environment and returns you to the system's default Python interpreter.

5. To delete the virtual environment, simply remove the directory:

    rm -rf myenv

   This command deletes the `myenv` directory and all its contents, effectively removing the virtual environment.

Note: Always ensure that the virtual environment is activated before running scripts or installing packages to ensure that the correct environment is being used.
"""