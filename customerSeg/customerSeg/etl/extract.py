from customerSeg.config import raw_dir
from pathlib import Path
import requests
from pandas.io.common import is_url, is_file_like, 
from pandas.io.parsers import 

# TODO
# write methods for extracting from azure blob storage, aws s3, google cloud

class Extract:

    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.fmt = self.check_source_format()

    def check_source_format(self):
        return 'url'

    def from_url(self, sub_dir=''):
        url = self.source
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
        except requests.ConnectionError:
            print(f'Connection to {url} failed.')
            return None

        # Basic filename extraction. May fail if URL does not end in extension
        # GOOD  " ...com/data/file.csv "
        # BAD   " ...com/data/file.csv?keyword=something " 
        filepath = raw_dir / sub_dir / Path(url).name
        with open(filepath, 'wb') as f:
            f.writelines(response.iter_content(1024))
    


