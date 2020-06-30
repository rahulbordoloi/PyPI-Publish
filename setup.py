from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='R07',
    version='0.0.1',
    description='Packages of R-07!',
    url="https://github.com/rahulbordoloi/PyPI-Publish",
    author="Rahul Bordoloi",
    author_email="rahulbordoloi24@gmail.com",

    py_modules=['R07'],
    package_dir={'': 'src'},

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],

    long_description = long_description,
    long_description_content_type = 'text/markdown',

    install_requires = [
        "blessings ~= 1.7",
    ],

    extras_require = {
        "dev" : [
            "pytest>=3.7",
        ],
    },
) 