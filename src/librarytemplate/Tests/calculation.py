import yaml

yaml_file_path = "src\librarytemplate\data\input.yml"

# Load the YAML file
with open(yaml_file_path, 'r') as file:
    input_data = yaml.safe_load(file)

# Extract data
temperature = input_data['temperature']
x = input_data['settings']['x']
y = input_data['settings']['y']

# Perform calculation
result = temperature * (sum(x) + sum(y))

print("Result of the calculation:", result)
