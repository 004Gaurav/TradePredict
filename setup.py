from setuptools import setup, find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the given file.
    """
    with open(file_path) as file:
        requirements = file.readlines()
    
    # Remove any leading/trailing whitespace characters
    requirements = [req.replace('\n',"") for req in requirements]
    
    # Remove version numbers (e.g., 'numpy==1.21.0' becomes 'numpy')
    requirements = [req.split('==')[0] for req in requirements if req and not req.startswith('#')]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="TradePredict",
    version="1.0.0",
    author="Gaurav Kumar",
    author_email="gauravkumar19994@gmail.com",
    description="A machine learning-based stock price prediction tool using historical market data.",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),    
    
    entry_points={
        "console_scripts": [
            "tradepredict=app:main",  # Change 'app' and 'main' to your actual filename and function
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='==3.11.*',
)
