# librarytemplate
A lightweight python library for all the fresh innovative python developers who are racing towards their career . 

## Summary
Transforming code into a reusable Python library empowers developers to streamline workflows and solve business problems efficiently. This article and accompanying repository outline a proven process and offer guidelines to seamlessly convert code into a Python library.

### key focus areas :
- **Efficient Code Writing**: Prioritize writing code that is not only effective in solving business problems but also reusable across different projects and scenarios.
- **Comprehensive Testing**: Implement robust testing practices to ensure the reliability and stability of the codebase, facilitating easy integration into larger projects.
- **Package Development**: Explore strategies for packaging the code into a Python library, enabling seamless distribution and use by fellow team members or the broader open-source community.
- **Documentation and Guidelines**: Provide clear documentation and guidelines to assist developers in understanding and utilizing the library effectively, promoting adoption and collaboration.

## development process :

| Step |  Description | Commands/Detailed Description | Reference |
|---|---|---|---|
| 1 | Create a github repository  | Follow the naming conventions  | [https://www.freecodecamp.org/news/build-your-first-python-package/](https://www.freecodecamp.org/news/build-your-first-python-package/) |
| 2 | Development via branches   | divide all the process into branches  | better understanding for the end users |
| 3 | create a folder structure | Initial branch to follow directory structure| https://github.com/samdansk2/librarytemplate/tree/2_read_yml |
| 4 | create a read_yml | read the yaml file using input| https://github.com/samdansk2/librarytemplate/tree/2_read_yml |
| 5 | sample_calculation | Do the calculation using given .csv file| https://github.com/samdansk2/librarytemplate/tree/sample_calculation |
| 6 | writing tests | create the test for the above calculation ( test file naming : _test*.py) | https://github.com/samdansk2/librarytemplate/tree/4_write_test |
| 7 | Add .toml file and setup.py to build wheels | pip install bumpver <br> bumpver update --patch  <br> pip install build <br> python -m build | https://realpython.com/pypi-publish-python-package/ |
| 8 | Create account on pypi and upload using twine package | These commands will push the .whl and .tar.gz file into the pypi repository <br> conda install twine <br> twine upload dist/*  | https://realpython.com/pypi-publish-python-package/ |

# Usage

The recommended practices for developing python libraries are given below:

<img src="docs/package_development.svg" width=auto, height=auto/>


[https://realpython.com/pypi-publish-python-package/](https://realpython.com/pypi-publish-python-package/)
