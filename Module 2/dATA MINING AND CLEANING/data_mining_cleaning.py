import pandas as pd
class DataMining:
    def scrap_data(url):
        pass

    def consume_api(url):
        pass

    def load_csv(filepath):
        df = pd.read_csv(filepath)
        return df

class DataCleaning(DataMining):
    def check_missing_values(filepath):
        pass

    def imputation_missing_mean():
        pass

    def imputation_missing_mode():
        pass

    def imputation_missing_median():
        pass
    
    def imputation_missing_zeros():
        pass
    
    def check_duplicates(dataframe):
        pass

    def check_outliers(df):
        pass

    def clean(clean_data):
        return clean_data