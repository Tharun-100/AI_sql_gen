import os
from flask import Flask, request, jsonify
from openai import OpenAI
from google.cloud import bigquery
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Get the environment variables
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
google_application_credentials = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
bigquery_project_id = os.getenv('BIGQUERY_PROJECT_ID')
schema_file_path = os.getenv('SCHEMA_FILE_PATH')

# Set up clients
openai_client = OpenAI()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_application_credentials
bigquery_client = bigquery.Client(project=bigquery_project_id)

with open(schema_file_path, 'r') as f:
    schema = json.load(f)

def dataframe_from_query(sql_query):
    query_job = bigquery_client.query(sql_query)
    df = query_job.result().to_dataframe()
    return df

def generate_sql(natural_language_query, schema, error):
    prompt = f"""
    Database Schema:
    {schema}\n
    User Query:
    {natural_language_query}\n
    Any Error:
    {error}\n
    SQL Query:
    """
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant that translates natural language into SQL queries based on the {prompt}. Do not output anything other than the SQL query, no text nothing.You should recognize names or any other strings of clients and brand even though some part of string is missing or mis aligned, for example: actual string: House of RARE RABBIT user: rare rabbit, rare rabit, house of rare.Use LIKE operators or any other functions to complete this task without any errors."},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content[7:][:-3]

def recheck_sql(user_message, schema, error=None, retries=0, max_retries=5):
    try:
        sql_query = generate_sql(user_message, schema, error)
        df = dataframe_from_query(sql_query)
        return sql_query
    except Exception as e:
        error = str(e)
        retries += 1
        if retries < max_retries:
            return recheck_sql(user_message, schema, error, retries, max_retries)
        else:
            raise Exception(f"Failed after {max_retries} attempts. Last error: {error}")

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    user_message = data.get('query')
    if not user_message:
        return jsonify({"error": "No query provided"}), 400
    try:
        final_sql_query = recheck_sql(user_message, schema, retries=0, max_retries=5)
        df = dataframe_from_query(final_sql_query)
        return jsonify({"result": df.to_dict(orient='records')})
    except Exception as e:
        return jsonify({"error": f"Error processing query: {e}"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
