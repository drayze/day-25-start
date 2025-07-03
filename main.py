import pandas as pd
import os

def split_csv(input_file, output_file1, output_file2):
    """
    Parse a CSV file and split it into two separate files using pandas
    
    Parameters:
    input_file (str): Path to input CSV file
    output_file1 (str): Path to first output CSV file
    output_file2 (str): Path to second output CSV file
    """
    
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)
    
    # Calculate the middle index
    mid_point = len(df) // 2
    
    # Split the DataFrame into two parts
    df1 = df[:mid_point]
    df2 = df[mid_point:]
    
    # Write to output files
    df1.to_csv(output_file1, index=False)
    df2.to_csv(output_file2, index=False)
    
    return len(df1), len(df2)  # Return the number of rows in each file


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

# Main execution
if __name__ == "__main__":
    try:
        # Get input file path from user
        input_csv = get_input_file_path()
        
        # Generate output file names based on input file
        base_name = os.path.splitext(os.path.basename(input_csv))[0]
        output_csv1 = f"{base_name}_output1.csv"
        output_csv2 = f"{base_name}_output2.csv"
        
        split_csv(input_csv, output_csv1, output_csv2)
        print("\nCSV files have been successfully split!")
        print(f"Created: {output_csv1}")
        print(f"Created: {output_csv2}")
        
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")