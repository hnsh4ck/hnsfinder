# Hidden Links Finder

** hnsfinder ** is a Python tool designed to find hidden links on websites by scanning the HTML for links that are hidden using `display:none` style attributes. The tool is inspired by the functionality of Subzy and is easy to use via the command line.

## Features
- Scans a website for hidden links
- Command-line interface for easy usage
- Clear and informative output

## Requirements
- Python 3.6 or higher
- `requests` library
- `beautifulsoup4` library

## Installation

1. **Clone the Repository**

   git clone https://github.com/hnsh4ck/hnsfinder.git
   cd hnsfinder
   
## Install Dependencies

Before running the script, you'll need to install the required Python libraries:

- pip install -r requirements.txt

Alternatively, you can install the libraries manually:

- pip install requests beautifulsoup4

## Usage

To use the tool, simply run the Python script from the command line with the URL of the website you want to scan: 

- python hnsfinder.py https://example.com

Example Output:

[INFO] Scanning https://example.com for hidden links...

[SUCCESS] Hidden links found:
  - https://example.com/hidden-page-1
  - https://example.com/hidden-page-2

If no hidden links are found, you'll see:

[INFO] No hidden links found.


## License

This project is licensed under the MIT License. See the LICENSE file for details.
Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.
Contact

For any questions or suggestions, feel free to reach out:

    Email: hnsh4ck@gmail.com
    GitHub: hnsh4ck
