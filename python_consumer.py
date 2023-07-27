import pandas as pd
import os
import time


def get_parquet_files(directory):
    parquet_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                parquet_files.append(os.path.join(root, file))

    return parquet_files


def concat_parquet_files(file_list):
    df_list = []

    for file in file_list:
        df = pd.read_csv(file)
        df_list.append(df)

    return pd.concat(df_list, ignore_index=True)


def start_consumer(directory):
    while True:
        parquet_list = get_parquet_files(directory)
        try:
            df = concat_parquet_files(parquet_list)
            print(df.max())
        except:
            print("No file in " + directory)


if __name__ == '__main__':
    streaming_output = "C:/Users/enzol/spark_streaming/streaming_output"
    start_consumer(streaming_output)
