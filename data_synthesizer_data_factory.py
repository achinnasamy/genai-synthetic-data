
import pandas as pd
from DataSynthesizer.DataDescriber import DataDescriber
from DataSynthesizer.DataGenerator import DataGenerator
from DataSynthesizer.ModelInspector import ModelInspector
from DataSynthesizer.lib.utils import read_json_file, display_bayesian_network
from multiprocessing import freeze_support

input_data = "train.csv"

mode = 'bayesian_network_mode'
description_file = "{mode}_description.json"
synthetic_data = "synthoutput.csv"

# An attribute is categorical if its number of unique values is less than this threshold
threshold_value = 10

# Specify categorical attributes
categorical_attributes = {'Survived': True, 'Pclass': True, 'Sex': True, 'SibSp': True, 'Parch': True, 'Embarked': True}

# Specify candidate keys
candidate_keys = {'Id': True, 'Name': True}

# Tune noise level. Increase epsilon value to reduce the injected noises. Set epsilon=0 to turn off differential privacy
epsilon = 0.0

# The maximum number of parents in Bayesian network
degree_of_bayesian_network = 3

# Number of tuples generated in the synthetic dataset.
num_tuples_to_generate = 10

if __name__ == '__main__':
    freeze_support()

    describer = DataDescriber(category_threshold=threshold_value)
    describer.describe_dataset_in_correlated_attribute_mode(dataset_file=input_data,
                                                            epsilon=epsilon,
                                                            k=degree_of_bayesian_network,
                                                            attribute_to_is_categorical=categorical_attributes,
                                                            attribute_to_is_candidate_key=candidate_keys)
    describer.save_dataset_description_to_file(description_file)

    generator = DataGenerator()
    generator.generate_dataset_in_correlated_attribute_mode(num_tuples_to_generate, description_file)
    generator.save_synthetic_data(synthetic_data)