import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hia",
    version="0.0.1",
    author="Daniel Gómez Pan,  takercito",
    author_email="pana_1990@hotmail.com",
    description="hia makes machine learning more accurate and easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="hhttps://github.com/hispan-ia/hia",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)