from pathlib import Path
import customerSeg.utils

# Should be root of 'customer-segmenter' repository
root = Path(__file__).parents[2]

data_dir = root / 'data'
raw_dir = data_dir / 'raw'
interim_dir = data_dir / 'interim'
merged_dir = interim_dir / 'merged'
transformed_dir = data_dir / 'transformed'

azure_connection_string = customerSeg.utils.get_env_var('AZURE_CONNECTION_STRING')
container_name = "test"