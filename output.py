import csv

def search_and_modify(csv_file, search_column, search_value, modify_column, new_value):
    # Read the CSV file and store data in a list of dictionaries
    data = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Search for the specific data and modify it
    for entry in data:
        if entry[search_column] == search_value:
            entry[modify_column] = new_value

    # Write the modified data back to the CSV file
    with open(csv_file, 'w', newline='') as file:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Example usage:
csv_file_path = 'example.csv'
search_column_name = 'Name'
search_value_to_find = 'John Doe'
modify_column_name = 'Age'
new_value_to_set = '30'

search_and_modify(csv_file_path, search_column_name, search_value_to_find, modify_column_name, new_value_to_set)