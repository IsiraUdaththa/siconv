# # Sinhala to Singlish Transliterator

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)


A Python library for transliterating Sinhala script to Singlish (Romanized Sinhala) and vice versa. This project aims to provide a fast and reliable solution for converting between these two scripts.

## Features

- **Bidirectional Support**: Convert from Sinhala to Singlish and Singlish to Sinhala.
- **Easy to Use**: Simple API for integrating into your projects.
- **Customizable**: Extend and modify transliteration rules as needed.

## Installation

Install the package from PyPI:

```sh
pip install siconv
```

## Usage Example:

```python
from siconv import sinhala_to_singlish

sinhala_text = "ආයුබෝවන්, Sri Lanka"
converted_singlish = sinhala_to_singlish(sinhala_text)
print("Sinhala to Singlish:", converted_singlish) # Output: ayubowan, Sri Lanka

sinhala_text = "ආයුබෝවන්, Sri Lanka"
converted_singlish = sinhala_to_singlish(sinhala_text, exclusive=True)
print("Sinhala to Singlish:", converted_singlish) # Output: ayubowan
```

```python
from siconv import singlish_to_sinhala

singlish_text = "ayubowan"
converted_sinhala = singlish_to_sinhala(singlish_text)
print("Singlish to Sinhala:", converted_sinhala) # Output: ආයුබෝවන්

singlish_text = "mk bn"
converted_sinhala = singlish_to_sinhala(sinhala_text, slangs=True)
print("Sinhala to Singlish:", converted_sinhala) # Output: මොකද කරන්නේ බන්
```

## Project Directory

```
siconv/
│
├── siconv/
│   ├── __init__.py
│   ├── to_singlish.py
│   ├── to_sinhala.py
│
├── tests/
│   ├── __init__.py
│   ├── test_to_singlish.py
│   ├── test_to_sinhala.py
│
├── data/
│   ├── transliteration_rules.json
│
├── .gitignore
├── LICENSE
├── README.md
├── setup.py
```
