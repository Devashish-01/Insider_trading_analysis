# Insider Trading Data Analysis

This is a web application built using [Streamlit](https://streamlit.io/) that processes multiple CSV files related to insider trading data, specifically focusing on transactions involving promoters and promoter groups. The app analyzes the data, displays the top companies involved in buying/selling, and allows users to download the processed data.

## Features

- **Multiple File Upload**: Users can upload multiple CSV files at once, and the app will integrate the data for analysis.
- **Data Processing**: The app processes the CSV files, filters relevant data (e.g., Equity Shares, Market Sale/Purchase), and calculates the quantity traded based on buying and selling transactions.
- **Top 15 Companies Visualization**: Users can view the top 15 companies involved in buying/selling through a bar chart.
- **Download Processed Data**: Users can download the processed data as a CSV file.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Streamlit
- Pandas
- Matplotlib

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**

   ```bash
   streamlit run insider_trading.py
   ```

4. **Access the app:**

   Open your browser and go to `http://localhost:8501/`.

## CSV File Requirements

The uploaded CSV files must contain the following columns:

- `COMPANY \n`
- `CATEGORY OF PERSON \n`
- `TYPE OF SECURITY (PRIOR) \n`
- `MODE OF ACQUISITION \n`
- `VALUE OF SECURITY (ACQUIRED/DISPLOSED) \n`
- `ACQUISITION/DISPOSAL TRANSACTION TYPE \n`

## Usage

1. **Upload CSV Files**: Use the file uploader to select multiple CSV files.
2. **View Integrated Data**: The app will display the integrated data from all the uploaded files.
3. **Top 15 Companies Analysis**: Click the button to view a bar chart of the top 15 companies involved in buying and selling transactions.
4. **Download Processed Data**: Click the download button to get the processed data as a CSV file.

## File Structure

```
├── insider_trading.py    # Main Streamlit app file
├── requirements.txt      # List of required Python packages
├── README.md             # Project documentation
└── .gitignore            # Git ignore file
```

### Example CSV Data

| COMPANY                              | CATEGORY OF PERSON    | TYPE OF SECURITY (PRIOR)    | MODE OF ACQUISITION    | VALUE OF SECURITY (ACQUIRED/DISPLOSED)    | ACQUISITION/DISPOSAL TRANSACTION TYPE     |
|-----------------------------------------|-----------------------|-----------------------------|------------------------|-------------------------------------------|------------------------------------------|
| XYZ Ltd                                 | Promoters             | Equity Shares               | Market Purchase        | 1000                                      | Buy                                      |
| ABC Ltd                                 | Promoter Group        | Equity Shares               | Market Sale            | 500                                       | Sell                                     |
| XYZ Ltd                                 | Promoters             | Equity Shares               | Market Purchase        | 2000                                      | Buy                                      |

## License

This project is licensed under the MIT License.

## Acknowledgements

- Thanks to [Streamlit](https://streamlit.io/) for providing a simple and powerful framework for building web apps.

### Explanation:
- **Features**: Summarizes the app's main functionalities.
- **CSV File Requirements**: Lists the necessary columns for the CSV files.
- **Installation**: Provides step-by-step instructions for setting up and running the app.
- **Usage**: Explains how to interact with the app.
- **File Structure**: Shows the structure of the project files.
- **Example CSV Data**: Provides an example of the data expected in the CSV files.
- **License**: Mentions the license type.
