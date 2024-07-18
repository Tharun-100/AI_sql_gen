# AI Analytics(Natural Language to SQL Query Translator)

In this project, we will generate an SQL query and retrieve data from BigQuery by passing natural language queries using the GPT-40 model.

## Table of Contents
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setting up the environment](#setting-up-the-environment)
  - [Installing dependencies](#installing-dependencies)
  - [Setting up environment variables](#setting-up-environment-variables)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed [Python 3.x](https://www.python.org/downloads/).
- You have a Google Cloud account with BigQuery enabled.
- You have an OpenAI API key.

### Setting up the environment

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
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

### Setting up environment variables

Create a `.env` file in the root directory of your project and add the following environment variables:

```plaintext
OPENAI_API_KEY=your_openai_api_key
GOOGLE_APPLICATION_CREDENTIALS=path_to_your_google_credentials_json
BIGQUERY_PROJECT_ID=your_bigquery_project_id
SCHEMA_FILE_PATH=path_to_your_schema_file.json

## Usage
Run the Flask application:
``` 
bash
python app.py
```
The application will be available at http://0.0.0.0:8000.
/query

    Method: POST
    Description: Translate natural language query to SQL, execute it, and return the results.
    Request body:
{
  "query": "Your natural language query"
}
### Response
{
  "result": [ ... ]  // Query results as a list of records
}
/sql

    Method: POST
    Description: Translate natural language query to SQL and return the SQL query.
    Request body:
{
  "query": "Your natural language query"
}
Response:

{
  "result": "Translated SQL query"
}

