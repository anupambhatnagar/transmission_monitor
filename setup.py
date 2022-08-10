from setuptools import find_packages, setup
from package import Package

setup(
    name="transmission-monitor",
    version="0.0.1",
    description="A commmand line tool to monitor network traffic for Zoom and Workplace Chat",
    url="",
    author="Anupam Bhatnagar",
    author_email="anupambhatnagar@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "tk"
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    include_package_data=True,
    package_data={"": ["configs/*.json", "configs/*.config"]},
)
