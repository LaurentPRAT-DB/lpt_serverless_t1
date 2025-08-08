# uv init
# uv venv
# uv sync
# uv add pip   -> to enable the Dependencies check from Databricks extension.

"""Module for creating and using a Databricks serverless Spark session."""

from databricks.connect import DatabricksSession
from databricks.sdk.core import Config

config = Config(profile="DEMO FIELD")

spark = DatabricksSession.builder.remote(serverless=True).getOrCreate()

spark.sql("SELECT * FROM lpt.dbdemos_retail_c360.churn_users limit 5").show()

# Close the Spark session
spark.stop()
