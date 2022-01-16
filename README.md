# gofile

A simple Python wrapper for the Gofile API.

## Info

**The Gofile API and the Python wrapper are currently in their beta versions and will evolve over time. Check regularly to see if changes have been made.**

Current version works with the `2021-06-22` API.

## Installation

### [gofile PyPI page](https://pypi.org/project/gofile/)

To install run

    python3 -m pip install gofile

or just

    pip install gofile

## Usage

See [documentation](https://github.com/Coosta6915/gofile/wiki/) for detailed usage examples.

```py
import gofile

server = gofile.getServer()

print(server)

gofile.uploadFile("/home/user/documents/images.zip")
```
