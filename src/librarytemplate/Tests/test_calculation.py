import unittest
import yaml

yaml_file_path= "src\\librarytemplate\\data\\input,yml"

# Load the YAML file
with open(yaml_file_path, 'r') as file:
    input_data = yaml.safe_load(file)

def calculate_result(input_data):
    temperature = input_data['temperature']
    x = input_data['settings']['x']
    y = input_data['settings']['y']
    result = temperature * (sum(x) + sum(y))
    return result

class TestCalculation(unittest.TestCase):
    def test_normal_case(self):
        input_data = {
            'temperature': 10,
            'settings': {
                'x': [1, 2, 3],
                'y': [4, 5, 6]
            }
        }
        expected_result = 10 * (sum([1, 2, 3]) + sum([4, 5, 6]))
        self.assertEqual(calculate_result(input_data), expected_result)

    def test_negative_values(self):
        input_data = {
            'temperature': -5,
            'settings': {
                'x': [-1, -2, -3],
                'y': [-4, -5, -6]
            }
        }
        expected_result = -5 * (sum([-1, -2, -3]) + sum([-4, -5, -6]))
        self.assertEqual(calculate_result(input_data), expected_result)

    def test_zero_temperature(self):
        input_data = {
            'temperature': 0,
            'settings': {
                'x': [1, 2, 3],
                'y': [4, 5, 6]
            }
        }
        expected_result = 0
        self.assertEqual(calculate_result(input_data), expected_result)

    def test_empty_lists(self):
        input_data = {
            'temperature': 10,
            'settings': {
                'x': [],
                'y': []
            }
        }
        expected_result = 0  # Since both x and y are empty, their sum is zero
        self.assertEqual(calculate_result(input_data), expected_result)

if __name__ == '__main__':
    unittest.main()
