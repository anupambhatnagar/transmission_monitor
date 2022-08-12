from setuptools import find_packages, setup

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
    classifiers=[ ],
    include_package_data=True,
    package_data={"": []},
)
