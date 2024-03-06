import yaml

# Load the YAML file
with open('input,yml', 'r') as file:
    input_data = yaml.safe_load(file)

# Extract data
temperature = input_data['temperature']
x = input_data['settings']['x']
y = input_data['settings']['y']

# calculation
result = temperature * (sum(x) + sum(y))

print("The result is:", result)
