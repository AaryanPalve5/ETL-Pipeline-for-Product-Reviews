# ETL Pipeline for Product Reviews

This project involves extracting, transforming, and loading (ETL) product review data from multiple sources into a database to provide actionable insights.

## Project Structure

- `data/` - Contains the input data files (CSV, JSON, and Text file).
- `scripts/` - Contains the Python scripts for extraction, transformation, loading, and the main pipeline.
- `requirements.txt` - Lists the required Python dependencies.
- `README.md` - Documentation for setting up and running the pipeline.

## Data Sources

- **Source A (CSV)**: Structured review data from an internal database.
- **Source B (JSON)**: Mocked data simulating a REST API response.
- **Source C (Text)**: Unstructured product reviews in raw text format.


---

### **How to Run the Project:**

1. **Install the required dependencies**:
   Ensure you have all the necessary libraries by running `pip install -r requirements.txt`.

2. **Place your data files**:
   Place the `source_a_data.csv`, `source_b_data.json`, and `source_c_data.txt` files in the `data/` directory.

3. **Run the ETL pipeline**:
   Navigate to the `scripts/` directory and run the ETL pipeline:
   ```bash
   python etl_pipeline.py
