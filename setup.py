from setuptools import setup, find_packages

setup(
    name="gofile",
    version="0.0.1",
    py_modules=["gofile"],
    description="A Python wrapper for the GoFile API",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Codec04",
    license="MIT",
    packages=find_packages(),
    url="https://github.com/Codec04/gofile/",
    project_urls={
        "Bugs": "https://github.com/Codec04/gofile/issues/",
        "Documentation": "https://github.com/Codec04/gofile/wiki/",
        "Source code": "https://github.com/Codec04/gofile/"
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=["requests~=2.25.1"]
)
