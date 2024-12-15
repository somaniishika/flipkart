from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str = "requirements.txt") -> List[str]:
    """
    This function reads the requirements.txt file and returns a list of dependencies.
    """
    requirement_list = []
    try:
        with open(file_path, "r") as file:
            requirement_list = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Ensure the file exists.")

    # Filter out empty lines or comments
    requirement_list = [
        req for req in requirement_list if req and not req.startswith("#")
    ]
    return requirement_list

setup(
    name="flipkart",
    version="0.0.1",
    author="Ishika",
    author_email="ishika05somani@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
