import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ensae2019",
    version="1.0",
    author="Albane Gerondeau, Caroline Moreau, Corentin Odic, Pauline Roubeix, Michael Soumm",
    author_email="michael.soumm@ensae.fr",
    description="Small package to show data with cartopy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MSoumm/ensae2019-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)