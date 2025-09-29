import pandas as pd

xlsx_files = ['data/human_label/n206-s42-xlsx/MI_labelled_n206_s42.xlsx',
              'data/human_label/n206-s42-xlsx/MB_labelled_n206_s42.xlsx',
              'data/human_label/n206-s42-xlsx/EPV_labelled_n206_s42.xlsx',
              'data/human_label/n206-s42-xlsx/JLA_labelled_n206_s42.xlsx']

for xlsx_file in xlsx_files:
    print(f"Processing {xlsx_file}...")
    json_file = xlsx_file.replace('.xlsx', '.json')

    df = pd.read_excel(xlsx_file, engine='openpyxl', sheet_name='Data')

    #change input type from str to list
    df['inputs'] = df['inputs'].apply(lambda x: eval(x) if isinstance(x, str) else x)
    #label to lowercase and substitute spaces by underscores
    df['label'] = df['label'].str.lower().str.replace(' ', '_')
    df = df[['inputs', 'label']]


    print(f"columns: {df.columns} \n rows: {len(df)}")
    print(f"Diff Labels: {df['label'].unique()} - {len(df['label'].unique())} unique labels")



    print(f"Saving to {json_file}...")
    df.to_json(json_file, orient='records', force_ascii=False, indent=2)


