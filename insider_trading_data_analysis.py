import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Function to process the CSV and return a sorted DataFrame
def process_csv(dataframe):
    name = {}

    # Fill NaN values with empty strings to avoid errors during string operations
    dataframe = dataframe.fillna('')

    for i, row in dataframe.iterrows():
        # Clean and extract necessary fields by converting to string and stripping
        company_name = str(row['COMPANY \n']).strip()
        category = str(row['CATEGORY OF PERSON \n']).strip()
        security_type = str(row['TYPE OF SECURITY (PRIOR) \n']).strip()
        acquisition_type = str(row['MODE OF ACQUISITION \n']).strip()
        number = row['VALUE OF SECURITY (ACQUIRED/DISPLOSED) \n']
        buy_sell = str(row['ACQUISITION/DISPOSAL TRANSACTION TYPE \n']).strip()

        # Ensure 'number' is numeric
        try:
            number = float(number)
        except ValueError:
            continue  # Skip rows with non-numeric 'number' values

        # Filter the rows based on conditions
        if category in ['Promoters', 'Promoter Group']:
            if security_type == 'Equity Shares' and acquisition_type in ['Market Sale', 'Market Purchase']:
                # Update the quantity based on buy/sell
                if company_name in name:
                    name[company_name] += int(number) if buy_sell == 'Buy' else -int(number)
                else:
                    name[company_name] = int(number) if buy_sell == 'Buy' else -int(number)

    # Convert the dictionary to a DataFrame
    result_df = pd.DataFrame(name.items(), columns=['Company Name', 'Quantity Traded'])

    # Sort the DataFrame in descending order of 'Quantity Traded'
    result_df = result_df.sort_values(by='Quantity Traded', ascending=False)

    return result_df

# Function to integrate multiple CSV files
def integrate_files(files):
    dataframes = []
    for file in files:
        df = pd.read_csv(file)
        dataframes.append(df)
    integrated_df = pd.concat(dataframes, ignore_index=True)
    return integrated_df

# Streamlit app title
st.title("Insider Trading Data Analysis")

# Multiple file uploader widget for CSV files
uploaded_files = st.file_uploader("Upload CSV Files here ", type="csv", accept_multiple_files=True)

# If files are uploaded, process them
if uploaded_files:
    # Integrate the uploaded CSV files into a single DataFrame
    integrated_df = integrate_files(uploaded_files)

    st.write("Integrated Data from Multiple Files:")
    st.dataframe(integrated_df)

    # Process the integrated CSV and get the result DataFrame
    processed_df = process_csv(integrated_df)

    # Display options to view different analyses
    if st.button("Show Top 15 Companies Involved in Buying/Selling"):
        st.subheader("Top 15 Companies Involved in Buying/Selling")
        st.dataframe(processed_df)
        if not processed_df.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            processed_df.head(15).plot(kind='bar', x='Company Name', y='Quantity Traded', ax=ax, color='skyblue')
            plt.title('Top 15 Companies by Promoter Group Transactions')
            plt.xlabel('Company Name')
            plt.ylabel('Quantity Traded')
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig)
        else:
            st.write("No data available for plotting.")

    # Download the processed CSV file
    csv = processed_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Full Processed CSV",
        data=csv,
        file_name="processed_promoter_data.csv",
        mime='text/csv'
    )
