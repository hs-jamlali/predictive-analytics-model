import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'])
    df.set_index('date', inplace=True)
    return df

if __name__ == "__main__":
    data = preprocess_data('data/sample_data.csv')
    data.to_csv('data/preprocessed_data.csv')
    print("Data preprocessed and saved to data/preprocessed_data.csv")