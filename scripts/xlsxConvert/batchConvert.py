from pathlib import Path
import re
import subprocess
from multiprocessing.dummy import Pool
from argparse import ArgumentParser
import pandas as pd
from customerSeg.config import raw_dir, interim_dir, merged_dir


class BatchConverter:

    def __init__(self, xlsx_dir, csv_dir, outputcsv, script_path):
        self.xlsx_dir = xlsx_dir
        self.csv_dir = csv_dir
        self.outputcsv = outputcsv
        self.script_path = script_path
        self.commands = []
    
    def run(self, n_threads=2):
        """
        Converts all .xlsx files in <xlsx_dir> to .csv files, saved to <csv_dir>
        """
        print(f'Searching for files in {self.xlsx_dir}')
        self._generate_subprocess_list()
        print(f'Converting {len(self.commands)} files...')
        self._multithread_calls(n_threads)
        print('Converted')
        return None
    
    def _generate_subprocess_list(self):
        for filepath in self.xlsx_dir.glob('*.xlsx'):
            filename = re.search(r'(.+[\\|\/])(.+)(\.(csv|xlsx|xls))', str(filepath)).group(2) # Extract File Name on group 2 "(.+)"
            call = ["python", str(self.script_path), str(filepath), str(self.csv_dir/filename)+'.csv']
            self.commands.append(call)
        return None

    def _multithread_calls(self, n_threads):
        pool = Pool(2)
        # on Windows: use functools.partial(subprocess.call, shell=True) in place of subprocess.call 
        for i, return_code in enumerate(pool.imap(subprocess.call, self.commands)):
            if return_code != 0:
                print(f"Command # {i} failed with return code {return_code}.")
        return None

    def merge_csvs(self, output_filepath):
        """
        Use after converting xlsx to csv with self.run(). Merges all .csvs in <csv_dir> into one.
        """
        listofdataframes = []
        for filepath in self.csv_dir.glob('*.csv'):
            df = pd.read_csv(filepath)
            if df.shape[1] == 8: # make sure 8 columns
                listofdataframes.append(df)
            else:
                print(f'{filepath}  has {df.shape[1]} columns - skipping')

        bigdataframe = pd.concat(listofdataframes).reset_index(drop=True)
        bigdataframe.to_csv(self.outputcsv,index=False)
        return None

if __name__ == '__main__':
    converter_script_path = Path(__file__).parent / 'xlsx2csv.py'
    xlsx_directory= raw_dir
    csv_directory = interim_dir
    output_filepath = merged_dir / 'merge.csv'

    BC = BatchConverter(xlsx_directory, csv_directory, output_filepath, converter_script_path)
    BC.run()
    BC.merge_csvs(output_filepath)