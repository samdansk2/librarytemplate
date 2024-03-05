import yaml

# path to YAML file
yaml_file_path = "src\librarytemplate\data\input,yml"

# Read the YAML file
with open(yaml_file_path, "r") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# Access and work with the YAML data
temperature = yaml_data["temperature"]
settings = yaml_data["settings"]
data = yaml_data["data"]

# Print some example data to verify it's loaded correctly
print("Temperature:", temperature)
print("Settings X:", settings["x"])
print("Settings Y:", settings["y"])
