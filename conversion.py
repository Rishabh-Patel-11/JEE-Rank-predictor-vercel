import json

# File paths
input_file = "data/2025-01-22_morning.txt"
output_file = "data/2025-01-22_morning.json"

# Read the file and process the data
data_list = []
with open(input_file, "r") as file:
    for line in file:
        parts = line.split()
        if len(parts) == 2:
            marks, percentile = parts
            data_list.append({"marks": int(marks), "percentile": float(percentile)})

# Convert to JSON format
json_output = json.dumps(data_list, indent=4)

# Save to a new file
with open(output_file, "w") as file:
    file.write(json_output)

print(f"Converted data has been saved to {output_file}")
