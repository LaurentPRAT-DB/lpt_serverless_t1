# Project Context & Memory Management

## Project Overview
- **Project Name**: lpt_serverless_t1
- **Purpose**: Databricks serverless Spark application for data processing
- **Workspace**: https://e2-demo-field-eng.cloud.databricks.com
- **Profile**: DEMO FIELD

## Current Architecture
- **Compute**: Databricks Serverless Spark
- **Spark Version**: 15.4.x-scala2.12
- **Node Type**: i3.xlarge
- **Scaling**: 1-4 workers with autoscaling
- **Language**: Python 3.11+

## Key Files
- `src/lpt_serverless_t1/call_serverless.py` - Main serverless session creation
- `src/lpt_serverless_t1/main.py` - Core data processing functions
- `resources/lpt_serverless_t1.job.yml` - Job configuration
- `databricks.yml` - Bundle configuration

## Data Sources
- `lpt.dbdemos_retail_c360.churn_users` - Customer churn analysis data
- `samples.nyctaxi.trips` - NYC taxi trip data

## Development Setup
- Uses `uv` for dependency management
- Databricks Connect for local development
- Asset bundles for deployment

## Current Status
- Basic serverless Spark session working
- Simple SQL queries to test connectivity
- No ML models currently implemented

## TODO / Future Enhancements
- Add machine learning models
- Implement data processing pipelines
- Add monitoring and logging
- Optimize for serverless performance

## Notes for AI Assistant
- This is a Databricks serverless project
- Focus on serverless-optimized patterns
- Consider cost optimization for serverless compute
- Maintain compatibility with Databricks Connect
