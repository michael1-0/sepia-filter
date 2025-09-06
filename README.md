# Simple Sepia Filter Script

A simple command line program using Pillow that converts images to have the sepia filter.

## Installation

Create a python virtual environment:

```
python3 -m venv venv
```

Activate the virtual environment:

```
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\Activate.ps1
```

Install the requirements:

```
pip install -r requirements.txt
```

## Usage

Default intensity:

```
python3 sepia.py <input-file> <output-file>
```

Adjusting intensity (0.0 to 1.0):

```
python3 sepia.py -i 0.5 <input-file> <output-file>
```
