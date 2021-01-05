from pathlib import Path
import customerSeg.utils

# Should be '~/path/to/customer-segmenter' repository
root = Path(__file__).parents[2]

### Directories
data_dir = root / 'data'
raw_dir = data_dir / 'raw'
interim_dir = data_dir / 'interim'

merged_dir = interim_dir / 'merged'
merged_data_path = merged_dir / 'merge.csv'

transformed_dir = data_dir / 'transformed'
customer_table_path = transformed_dir / 'customer_table.csv'

azure_connection_string = customerSeg.utils.get_env_var('AZURE_CONNECTION_STRING')
container_name = "test"