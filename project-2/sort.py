import pandas as pd
from collections import OrderedDict 

wb_file = 'Hedge Fund Strategies Brokenup.xlsx'
rb_file = 'output.xlsx'

print('Reading "{}"...'.format(wb_file))

sheets = pd.read_excel(wb_file, sheet_name=None)

output_sheets = OrderedDict()

print("Processing sheets...")

for sheetname, df in sheets.items():

    print("--> Processing {}...".format(sheetname))

    old_rows = df.iloc[:, 0]
    old_rows.dropna(inplace=True)
    new_cols = []
    for i in old_rows:
        if i not in new_cols:
            new_cols.append(i)

    index = df.iloc[:, 4]
    index.dropna(inplace=True)
    index = list(index)
    new_index = []
    for i in index:
        if i not in new_index:
            new_index.append(i)
    
    df_out = pd.DataFrame(columns=new_cols, index=new_index)

    df.drop(df.columns[[3, 4]], axis=1, inplace=True)
    df.dropna(inplace=True)

    for index, row in df.iterrows():
        if row[1] in df_out.index:
            df_out.at[row[1], row[0]] = row[2]
        else:
            print("Input date is not in output date list!")
    
    df_out.rename(index=lambda s: s.strftime('%Y-%m-%d'), inplace=True)

    output_sheets[sheetname] = df_out

print('Writing "{}"...'.format(rb_file))

with pd.ExcelWriter(rb_file, engine='xlsxwriter') as writer:
    for sheetname, df in output_sheets.items():
        print("--> Writing sheet {}...".format(sheetname))
        df.to_excel(writer, sheetname)
    writer.save()

print("Done!")
