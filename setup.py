from setuptools import find_packages, setup

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="gofile",
    version="0.1.2",
    description="A simple Python wrapper for the GoFile API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Coosta6915",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "Documentation": "https://github.com/Coosta6915/gofile/wiki/",
        "GitHub": "https://github.com/Coosta6915/gofile/"
    },
    packages=find_packages(),
    install_requires=["requests~=2.25.1"],
    python_requires='>=3',
)
