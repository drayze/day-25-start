base_path = "C:/Users/YourName/Documents"  # Windows example
# or
base_path = "/home/username/documents"  # Linux/Mac example
import os

#######

def get_input_file_path():
    base_path = os.getcwd()  # Use current working directory
    # ... rest of the function
#########

def get_input_file_path():
    base_path = os.getcwd()
    
    # Prompt user for file name and construct full path
    print("\nEnter the file name or partial path (must be a .csv file):")
    while True:
        user_input = input("> ").strip()

        # Check if the input ends with .csv
        if not user_input.endswith('.csv'):
            print("File must have .csv extension")
            continue
            
        # Construct full path    
        full_path = os.path.join(base_path, user_input)
        
        # Check if file exists
        if os.path.isfile(full_path):
            return full_path
        else:
            print(f"File not found: {full_path}")
            retry = input("Would you like to try again? (y/n): ").lower()
            if retry != 'y':
                raise FileNotFoundError("Valid input file not provided")
            
##############



