import pandas as pd
import json

file_path = 'oi.xlsx'
sheet_name = 'Balance Sheet Movement'

df = pd.read_excel(file_path, sheet_name=sheet_name)

df.fillna('', inplace=True)

def format_data(df):
    data_list = [] 
    for i, row in df.iterrows():
        formatted_row = {"Related Party": row['Related Party']}  
        
        for col in df.columns[1:]: 
            value = str(row[col])  # Convert value to string
            
            array_as_string = f"[{value}, '']"
            
            formatted_row[col] = f'#{array_as_string}#'
            print(i)
            
        
        data_list.append(formatted_row)
    
    return data_list

formatted_data = format_data(df)

output_file = 'output.json'
with open(output_file, 'w') as f:
    json.dump(formatted_data, f, indent=4)
    
print(f"Data successfully written to {output_file}")
