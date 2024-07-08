from setuptools import setup, find_packages
import logging

REPO_URL = 'https://github.com/BenHababo/python_packages'

def parse_requirements(filename):
    try: 
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        logging.warning(f'requirements file {filename} not found')
        return []


pakace_name = 'test-package'
setup(
    name=pakace_name,
    version='0.1',
    packages=find_packages(where=pakace_name),
    install_requires=[
        # List your package dependencies here
    ],
    entry_points={
        'console_scripts': [
            # If you have command-line scripts, list them here
            # 'script_name = module_name:function_name'
        ],
    },
    author='Ben Hababo',
    author_email='benha@monday.com',
    description='A brief description of your package',
    long_description=open(f'{pakace_name}/README.md').read(),
    long_description_content_type='text/markdown',
    url=REPO_URL,
    python_requires='>=3.6',
    requires=parse_requirements(f'{pakace_name}/requirements.txt'),
    
)