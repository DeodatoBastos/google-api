from sheets import create_spreadsheet,  write_columns_names, export_pandas_df_to_sheets, write_mean
from dotenv import load_dotenv
import os

if __name__ == "__main__":

    load_dotenv()
    file_path = "data/data.csv"

    if os.getenv("ID") is None:
        spreadsheet_id = create_spreadsheet()
        write_columns_names(spreadsheet_id, file_path)
        export_pandas_df_to_sheets(spreadsheet_id, file_path)

        with open(".env", "a") as file:
            file.write(f"ID={spreadsheet_id}")

    else:
        spreadsheet_id = os.getenv("ID")
        write_columns_names(spreadsheet_id, file_path)
        export_pandas_df_to_sheets(spreadsheet_id, file_path)
        write_mean(spreadsheet_id, 0.123)
