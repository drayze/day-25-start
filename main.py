import csv

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

# Example usage:
def example_split_criteria(row):
    """
    Example criteria: Split based on whether a value in the first column is greater than 50
    Modify this function according to your needs
    """
    return float(row[0]) > 50

# Main execution
if __name__ == "__main__":
    try:
        # Replace these with your actual file paths
        input_csv = "input.csv"
        output_csv1 = "output1.csv"
        output_csv2 = "output2.csv"
        
        split_csv(input_csv, output_csv1, output_csv2, example_split_criteria)
        print("CSV files have been successfully split!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")