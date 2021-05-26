import glob2
import pandas as pd

path = r"C://Users//Filip//OneDrive - Redslim//Desktop//AZ//"

def merge_files(files):
    print("Merging files:")
    df = pd.DataFrame()
    for file in files:
        print(file)
        df_current = pd.read_csv(file, header=None)
        df = pd.concat([df,df_current])
    print('\nComplete')
    
    return df

if __name__ == '__main__':
    files = glob2.glob(path+'*MEASURE*.csv.bz2')
    df = merge_files(files)
    
df.to_csv(path+'merged_MEASURE.csv', header=None,index=None,line_terminator = '\r')