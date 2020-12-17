from customerSeg.config import raw_dir
from pathlib import Path
import requests

# TODO
# write from_azure, from_s3 methods

class Extract:



    def from_url(self, url, sub_dir=''):
        response = requests.get(url)
        filepath = raw_dir / sub_dir / Path(url).name
        with open(filepath, 'wb') as f:
            f.write(response.content)
    
    def from_azure(self):
        pass