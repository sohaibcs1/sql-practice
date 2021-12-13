from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="get_ipinfo",
    version="0.1.1",
    author='Muhammad Sohaib',
    author_email="sohaib.cs1@gmail.com",
    description='Get Country, Region, City, GPS ,ZIP and ISP',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['ip', 'address', 'location'],
    classifiers=[
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6", 
    py_modules=['get_ipinfo'],
    package_dir={"": "src"}
    #install_requires=['urllib','requests']
    
)
