import pandas as pd
from sdv.datasets.demo import download_demo
from sdv.lite import SingleTablePreset

class SyntheticDataGenerator:
    # Output file = Your custom output file's path
    def __init__(self, dataset_name, modality='single_table', num_rows=1000, output_file="sdv_sample_dataset.csv"):
        self.dataset_name = dataset_name
        self.modality = modality
        self.num_rows = num_rows
        self.output_file = output_file

    def generate_synthetic_data(self):
        real_data, metadata = self._load_data()

        # Generate synthetic data
        synthetic_data = self._generate_synth_data(metadata, real_data)

        # Save synthetic data to a CSV file
        self._save_to_csv(synthetic_data)

        print(f"Synthetic data saved to {self.output_file}")

    def _load_data(self):
        if self.dataset_name == 'custom':
            real_data = pd.read_csv("sdv_sample_dataset.csv")
            metadata = None
        else:
            # Download demo data
            real_data, metadata = download_demo(modality=self.modality, dataset_name=self.dataset_name)

        return real_data, metadata

    def _generate_synth_data(self, metadata, real_data):
        # Create the synthesizer
        synthesizer = SingleTablePreset(metadata, name='FAST_ML')

        # Fit the synthesizer to real data
        synthesizer.fit(data=real_data)

        # Generate synthetic data
        synthetic_data = synthesizer.sample(num_rows=self.num_rows)

        return synthetic_data

    def _save_to_csv(self, synthetic_data):
        synthetic_data_df = pd.DataFrame(synthetic_data)
        synthetic_data_df.to_csv(self.output_file, index=False)

if __name__ == "__main__":
    generator = SyntheticDataGenerator(dataset_name='fake_hotel_guests')
    generator.generate_synthetic_data()