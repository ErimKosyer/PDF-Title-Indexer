# PDF-Title-Indexer

## Installation

Install dependencies

```
pip3 install -r requirements.txt
```

## Usage

Invoke script as seen below

```
python PDFIndexer.py <PDF FILE NAME>
```

This will output the indexed file into the directory that the script is found in.

## How it works

The script works by matching the font style of the title/subtitles that are to be indexed. The constant by which the program uses to search for headings can be changed to 'fontname' or 'size' if desired (refer to [pdfplumber docs](https://github.com/jsvine/pdfplumber)).


## Customisation

The script can be customised to change the column names in the resulting CSV file. 

This project is ongoing.

