"""
Export transformed data into warehouse
"""

from pathlib import Path
from azure.storage.blob import BlobServiceClient, BlobClient
import customerSeg.config

class Load:
    
    def __init__(self, source, target, method, **kwargs):
        self.source = source
        self.target = target
        self.method = method
        
        self.connect_str = kwargs.get('connect_str', None)
        self.container_name = kwargs.get('container_name', None)

        self.set_load_method()  

    def _load_to_azure(self):
        blob_service_client = BlobServiceClient.from_connection_string(self.connect_str)
        blob_client = blob_service_client.get_blob_client(container=self.container_name, blob=self.target)

        with open(self.source, "rb") as data:
            blob_client.upload_blob(data)

    def set_load_method(self):
        if self.method == 'blob':
            self._load = self._load_to_azure

    def load(self):
        print(f'Uploading via {self.method} method . . .')
        self._load()
        print('Uploaded')




if __name__ == '__main__':

    src = customerSeg.config.transformed_dir / '' # filename goes here
    tgt = 'test_output'
    mthd = 'blob'


    conn_str = customerSeg.config.azure_connection_string
    cont_name = customerSeg.config.container_name

    L = Load(source=src,
            target=tgt,
            method=mthd, 
            connect_str=conn_str,
            container_name=cont_name)

    L.load()