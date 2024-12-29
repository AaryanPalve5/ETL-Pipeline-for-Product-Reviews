## ETL Pipeline for Product Reviews

This project extracts, transforms, and loads (ETL) product review data from diverse sources into a database, providing actionable insights for customer sentiment analysis and product performance assessment.

## Project Structure

* **`data/`**: Contains input data files (CSV, JSON, Text).
* **`scripts/`**: Houses Python scripts for data extraction, transformation, loading, and the main pipeline execution.
* **`requirements.txt`**: Lists essential Python dependencies.
* **`README.md`**: Provides setup and running instructions (this document).

## Data Sources

* **Source A (CSV)**: Structured review data from an internal database (e.g., ratings, customer IDs, product IDs).
* **Source B (JSON)**: Mocked data mimicking a REST API response, structured similarly to Source A.
* **Source C (Text)**: Unstructured product reviews in raw text format, with each review on a separate line.

## Dependencies

This project utilizes the following Python libraries:

* **`textblob`**: For sentiment analysis of review text. Install it using `pip install textblob`.

## Setting Up the Project

1. **Install Dependencies**
   Run the following command in your terminal to install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare Data Files**
   Ensure you have the following data files in the `data/` directory:

   - `source_a_data.csv`: CSV file containing structured review data with at least 1000 rows.
   - `source_b_data.json`: JSON file mimicking a REST API response with at least 500 entries.
   - `source_c_data.txt`: Text file with at least 700 lines, each containing a product review in the specified format (`review_id|product_id|customer_id|rating|review_date|review_text`).

3. **Configure Database Connection (Optional)**
   If you wish to store the processed data in a database (e.g., SQLite, PostgreSQL), you'll need to modify the `scripts/load.py` script to reflect your preferred database connection details. This typically involves specifying connection parameters like host, database name, and credentials.

## Running the Pipeline

1. **Navigate to `scripts/` Directory**
   Use your terminal to navigate to the `scripts/` directory within your project.

2. **Execute the `etl_pipeline.py` Script**
   Run the following command to initiate the ETL pipeline:

   ```bash
   python etl_pipeline.py
   ```

## Expected Output

The ETL process performs the following tasks:

1. **Extracts Data**
   - Reads data from all three data sources.
   - Simulates API calls using the provided JSON file for Source B.

2. **Transforms Data**
   - Normalizes data into a consistent schema with columns like `review_id`, `product_id`, `customer_id`, `rating`, `review_date`, `review_text`, and newly added `sentiment` based on sentiment analysis.
   - Parses and cleans unstructured data from Source C.
   - Removes invalid rows (e.g., missing rating, malformed review date).
   - Eliminates duplicate records.

3. **Loads Data (Optional)**
   - Stores the cleaned and transformed data into the database specified in `scripts/load.py` (if configured).
   - Provides SQL queries within the `scripts/load.py` script to retrieve:
     - Average product ratings.
     - Top 3 most positively reviewed products.
     - Top 3 most negatively reviewed products.

## Additional Notes

- This solution assumes you have a basic understanding of Python programming and terminal commands.
- For more complex data processing scenarios, consider exploring data warehousing solutions like Apache Spark.
- Feel free to customize the provided code and data structures to suit your specific data formats and analysis needs.

By following these instructions and executing the `etl_pipeline.py` script, you'll gain valuable insights into customer sentiment and product performance through this ETL pipeline.
