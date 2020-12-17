from pathlib import Path

# Should be root of 'customer-segmenter' repository
root = Path(__file__).parents[2]

data_dir = root / 'data'
raw_dir = data_dir / 'raw'
interim_dir = data_dir / 'interim'
merged_dir = interim_dir / 'merged'