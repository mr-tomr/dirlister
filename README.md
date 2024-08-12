# dirlister

`dirlister` is a Python script for enumerating web directories and files on a target URL. It recursively lists all accessible directories and files from a specified starting URL.

## Features

- Enumerates both directories and files.
- Recursively explores subdirectories.
- Avoids infinite loops by tracking visited URLs.
- Simple and easy-to-use command-line interface.

## Installation

### Requirements

The script requires Python 3 and the following Python libraries:

- `requests`
- `beautifulsoup4`

You can install these dependencies using the following command:

```bash
pip install -r requirements.txt
```

Usage:

```bash
python3 dirlister.py <URL>
```
