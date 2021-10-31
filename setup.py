from setuptools import setup, find_packages


def requirements("requirements.txt": str) -> list:
    with open(file, encoding="utf-8") as r:
        return [i.strip() for i in r]

setup(
    name="gofile",
    version="0.1.2",
    py_modules=["gofile"],
    description="A simple Python wrapper for the GoFile API",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Coosta6915",
    license="MIT",
    packages=find_packages(),
    project_urls={
        "Documentation": "https://github.com/Coosta6915/gofile/wiki/",
        "GitHub": "https://github.com/Coosta6915/gofile/"
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=requirements,
    python_requires=">=3.6"
)
