import random
import pandas as pd

# Create lists of categorical values
ages = [random.randint(18, 65) for _ in range(500)]
sexes = ['male', 'female']
children = [random.randint(0, 5) for _ in range(500)]
smoker = ['yes', 'no']
regions = ['northeast', 'northwest', 'southeast', 'southwest']

# Generate dataset
data = []
for _ in range(500):
    entry = [
        random.choice(ages),
        random.choice(sexes),
        random.choice(children),
        random.choice(smoker),
        random.choice(regions)
    ]
    data.append(entry)

# Create a DataFrame
df = pd.DataFrame(data, columns=['age', 'sex', 'children', 'smoker', 'region'])

# Export to CSV
df.to_csv('insurance.csv', index=False)

# age,sex,children,smoker,region