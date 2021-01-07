from pathlib import Path
import requests
from io import StringIO
from pandas.io.common import is_url, is_file_like, is_fsspec_url 
from pandas.io.parsers import get_filepath_or_buffer
from customerSeg.config import raw_dir, interim_dir

# TODO
# write methods for extracting from azure blob storage, aws s3, google cloud
# current s3 uri check is hacky/basic

class Extract:

    """
    Extract data from storage.
    """

    def __init__(self, source, target):
        """
        Accepted source formats: url, file-like (str or pathlib.Path), s3.
        """
        # StringIO is expected type for imported pandas-based parser functions
        self.source = StringIO(str(source))  
        self.target = target
        self._set_extract_method()

    def _check_source_format(self, src):
        src = self.source
        if is_url(src):
            fmt = 'url'
        elif is_file_like(src):
            fmt = 'filelike'
        elif is_fsspec_url(src):
            fmt = 's3'
        else:
            fmt = 'invalid'
        return fmt
    
    def _set_extract_method(self):
        input_type = self._check_source_format(self.source)
        
        if input_type == 'url':
            self._extract = self._extract_from_url
        elif input_type == 'filelike':
            self._extract = self._extract_from_filelike
        elif input_type == 's3':
            self._extract = self._extract_from_s3
        else:
            self._extract = None
        
        return None
        
    def _extract_from_url(self):
        """
        Basic filename extraction. May fail if URL does not end with normal file extension. See examples.
        GOOD : " ...com/data/file.csv ";  "...org/data/spreadsheet.xlsx"
        BAD  : " ...com/data/file.csv?keyword=something "; "...com/data/file.csv?anything_after_csv"
        """
        url = self.source
        # Set up destination savepath
        savepath = self.target / Path(url).name
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
        except requests.ConnectionError:
            print(f'Connection to {url} failed.')
            # Exit early
            return None
        with open(savepath, 'wb') as sp:
            sp.writelines(response.iter_content(1024))
    
    def _extract_from_filelike(self):
        sourcepath = self.source
        savepath = self.target / Path(sourcepath).name
        try:
            with open(sourcepath, 'rb') as src:
                obj = src.read()
                with open(savepath, 'wb') as sp:
                    sp.write(obj)
        except Exception as e:
            print(e)
            return None

    def _extract_from_s3(self):
        pass

    def extract(self):
        self._extract()


if __name__ == '__main__':
    # Path to example customer library
    url_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx'
    # save file to a pre-designated 'raw' data directory, as defined in customerSeg.config
    extraction_path = raw_dir / 'Online_Retail.csv'

    E = Extract(source=url_path, target=extraction_path)
    E.extract()