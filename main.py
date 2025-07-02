import csv
import os

def split_csv(input_file, output_file1, output_file2, split_criteria):
    """
    Parse a CSV file and split it into two separate files based on given criteria
    
    Parameters:
    input_file (str): Path to input CSV file
    output_file1 (str): Path to first output CSV file
    output_file2 (str): Path to second output CSV file
    split_criteria (function): Function that determines which output file a row goes to
    """
    
    # Lists to store rows for each output file
    data_for_file1 = []
    data_for_file2 = []
    
    # Read the input CSV file
    with open(input_file, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        # Get headers
        headers = next(csv_reader)
        
        # Process each row
        for row in csv_reader:
            if split_criteria(row):
                data_for_file1.append(row)
            else:
                data_for_file2.append(row)
    
    # Write to first output file
    with open(output_file1, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers)
        csv_writer.writerows(data_for_file1)
    
    # Write to second output file
    with open(output_file2, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers)
        csv_writer.writerows(data_for_file2)

def example_split_criteria(row):
    """
    Example criteria: Split based on whether a value in the first column is greater than 50
    Modify this function according to your needs
    """
    return float(row[0]) > 50

def get_input_file_path():
    """
    Prompt user for file name and construct full path
    """
    base_path = "path/to/your/directory"  # Set your default base path here
    
    while True:
        print("\nEnter the file name or partial path:")
        user_input = input("> ").strip()
        
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
        
        split_csv(input_csv, output_csv1, output_csv2, example_split_criteria)
        print("\nCSV files have been successfully split!")
        print(f"Created: {output_csv1}")
        print(f"Created: {output_csv2}")
        
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")