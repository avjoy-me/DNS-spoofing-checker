# DNS-spoofing-checker
This repository contains a Python script to check for DNS spoofing by querying multiple DNS servers in Taiwan. The script verifies whether the DNS servers return the correct IP address for a specified domain. The results are displayed in the terminal and saved to a text file for further analysis.

## Features

- **Parallel Processing**: Utilizes threading to query DNS servers in parallel, reducing the overall runtime.
- **DNS Querying**: Checks if DNS servers return the correct IP address for the given domain.
- **Error Handling**: Handles various DNS resolution errors, including timeouts and non-answers.
- **Output**: Results are displayed in the terminal and saved to a text file (`dns_spoofing_results.txt`).

## Prerequisites

- Python 3.x
- `dnspython` library
- `pandas` library

You can install the required libraries using pip:
```sh
pip install dnspython pandas
