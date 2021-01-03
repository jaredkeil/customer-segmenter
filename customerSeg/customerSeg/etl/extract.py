from customerSeg.config import raw_dir
from pathlib import Path
import requests
from io import StringIO
from pandas.io.common import is_url, is_file_like, is_fsspec_url 
from pandas.io.parsers import get_filepath_or_buffer

# TODO
# write methods for extracting from azure blob storage, aws s3, google cloud

class Extract:

    """
    Extract data from storage.
    """

    def __init__(self, source, target):
        """
        Accepted source formats: url, file-like (str or pathlib.Path), s3.
        """
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
            self.extract = self._extract_from_url
        elif input_type == 'filelike':
            self.extract = self._extract_from_filelike
        elif input_type == 's3':
            self.extract = self._extract_from_s3
        else:
            self.extract = None
        
        return None
        
    def _extract_from_url(self):
        """Read from url"""
        # Basic filename extraction. May fail if URL does not end with normal file extension
        # GOOD  " ...com/data/file.csv "
        # BAD   " ...com/data/file.csv?keyword=something " 
        url = self.source
        filepath = self.target / Path(url).name
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
        except requests.ConnectionError:
            print(f'Connection to {url} failed.')
            return None
        with open(filepath, 'wb') as f:
            f.writelines(response.iter_content(1024))
    
    def _extract_from_filelike(self):
        sourcepath = self.source
        filepath = self.target / Path(sourcepath).name
        try:
            with open(sourcepath, 'rb') as src:
                obj = src.read()
                with open(filepath, 'wb') as f:
                    f.write(obj)
        except Exception as e:
            print(e)
            return None

    def _extract_from_s3(self):
        pass

    def run(self):
        self.extract()
