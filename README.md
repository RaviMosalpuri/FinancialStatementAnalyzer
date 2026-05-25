# Financial Statement Analyzer

## Project Overview
The Financial Statement Analyzer is a Python-based tool designed to automate the collection and analysis of company financial statements. It provides structured access to income statements, balance sheets, and cash flow statements, enabling ratio analysis and comparative benchmarking.  

This project aligns with the CFA curriculum by reinforcing fundamental concepts in financial reporting and analysis, while also serving as a practical foundation for quantitative finance applications.

## Project Goals
- Automate the retrieval of financial statements using public APIs.
- Provide clean, structured datasets for further analysis.
- Lay the groundwork for ratio analysis, visualization, and reporting.
- Demonstrate CFA-relevant applications such as equity analysis and financial statement interpretation.
- Build a modular, extensible codebase suitable for future enhancements (e.g., portfolio analysis, risk modeling).

## Setup Instructions

### Prerequisites
- Python 3.9 or higher

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/financial-statement-analyzer.git
   cd financial-statement-analyzer
    ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Project Structure
    financial-statement-analyzer/
    ├── data/          # Raw and processed financial data
    ├── notebooks/     # Jupyter notebooks for demos and analysis
    ├── src/           # Python scripts (data collection, analysis)
    ├── docs/          # Documentation and references
    ├── README.md      # Project overview and instructions
    └── requirements.txt

## Usage
Run the data collection script to fetch financial statements for a given company ticker:
  ```bash
  python src/data_collection.py

  Example (Apple Inc.):
  python src/data_collection.py AAPL
  ```

The financial statements will be saved in the data/ directory as CSV files.
