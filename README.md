# AI Analytics

In this project we will generate a sql query and retrieve the data from bigquery by passing natural language query using gpt-4o model.

## Table of Contents
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setting up the environment](#setting-up-the-environment)
  - [Installing dependencies](#installing-dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed [Python 3.x](https://www.python.org/downloads/).

### Setting up the environment

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Tharun-100/AI_sql_gen.git
    cd AI_sql_gen
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment**:

    - **On Windows**:
        ```bash
        .\env\Scripts\activate
        ```

    - **On macOS and Linux**:
        ```bash
        source env/bin/activate
        ```

### Installing dependencies

1. **Upgrade pip**:
    ```bash
    pip install --upgrade pip
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

instructions for usage in the command prompt, move to the project directory
```bash
    python app.py
 ```
create a new file to post the query for getting the SQL query and DATA
```python
# python script to call the local host 
import requests

url1 = 'http://localhost:8000/query'
url2 = 'http://localhost:8000/sql'
query_data = {
    'query': "give me top 10 products based on website revenue" 
}

response1 = requests.post(url1, json=query_data)
response = requests.post(url2, json=query_data)
print("User Query:",query_data["query"])
print("SQL QUERY:",response.json())  
print("DATA",response1.json())  
