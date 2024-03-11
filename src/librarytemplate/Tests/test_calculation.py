import unittest
import yaml

class TestCalculation(unittest.TestCase):
    def test_calculation(self):
        yaml_file_path= "src\librarytemplate\data\input,yml"

        # Load the YAML file
        with open(yaml_file_path, 'r') as file:
            input_data = yaml.safe_load(file)

        # Extract data
        temperature = input_data['temperature']
        x = input_data['settings']['x']
        y = input_data['settings']['y']

        result = temperature * (sum(x) + sum(y))

        expected_result = temperature * (sum(input_data['settings']['x']) + sum(input_data['settings']['y']))

        # Assert the calculated result matches the expected result
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
