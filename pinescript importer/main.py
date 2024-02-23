import csv
from datetime import datetime, timedelta

def txt_to_csv(input_file, output_file, start_date):
    # Validate the format of the start date
    try:
        datetime.strptime(start_date, '%Y%m%d')
    except ValueError:
        print("Invalid date format. Please enter the date in the format 'YYYYMMDD'.")
        return

    # Convert start_date to a datetime object
    start_datetime = datetime.strptime(start_date, '%Y%m%d')

    # Open the input text file for reading
    with open(input_file, 'r') as txt_file:
        # Read lines from the input file
        lines = txt_file.readlines()

        # Open a CSV file for writing
        with open(output_file, 'w', newline='') as csv_file:
            # Create a CSV writer object
            writer = csv.writer(csv_file)

            # Write each line as a row in the CSV file
            for i, line in enumerate(lines):
                # Split each line by whitespace
                data = line.strip().split()

                # Calculate the date for the current row
                current_date = (start_datetime + timedelta(days=i)).strftime('%Y%m%d')

                # Insert the current date at the beginning of the row
                row = [current_date] + data + data + data + data

                # Write the row to the CSV file
                writer.writerow(row)

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.csv"
    
    # Get starting date from user input
    start_date = input("Enter the starting date (YYYYMMDD): ")

    txt_to_csv(input_file, output_file, start_date)
    print(f"CSV file '{output_file}' has been created from '{input_file}'.")
