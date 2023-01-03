# Continuous Deployment with Snowpark Python Notebooks
An example of leveraging Jupyter Notebooks to perform continuous deployment of Snowpark Python code.

## Setting up your environment to use this repository.
First, you will need an installation of Python 3.8.

### Python Environment Configuration
You can configure a virtual environment to install the dependencies for this repository using the code below:

If you're on macOS or Linux, you can do this with the following commands:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If you're on Windows, you can do this with the following commands using PowerShell:
```
python -m venv venv
venv\Scripts\activate.ps1
pip install -r requirements.txt
```

### Environment Variable Configuration
You will need to set the following environment variables to use this repository:
- `SNOWFLAKE_ACCOUNT` - The name of your Snowflake account.
- `SNOWFLAKE_USER` - The username of the user you want to use to connect to Snowflake.
- `SNOWFLAKE_PASSWORD` - The password of the user you want to use to connect to Snowflake.
- `SNOWFLAKE_DATABASE` - The name of the database you want to use to connect to Snowflake.
- `SNOWFLAKE_SCHEMA` - The name of the schema you want to use to connect to Snowflake.
