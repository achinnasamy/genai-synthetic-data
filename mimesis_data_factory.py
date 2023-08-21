import mimesis
import pandas as pd

class MimesisDataFactory:

    def __init__(self, size):
        self.myperson = mimesis.Person()
        self.addr_prov = mimesis.Address()
        self.size = size

    def generate_synthetic_data(self):
        data = []
        for _ in range(self.size):
            firstname = self.myperson.first_name()
            lastname = self.myperson.last_name()
            address = self.addr_prov.address()
            email = self.myperson.email()
            phone = self.myperson.telephone()
            age = self.myperson.age()
            data.append((firstname, lastname, address, email, phone, age))
        return data

    def test_synthetic_data(self, data):
        df = pd.DataFrame(data, columns=['First Name', 'Last Name', 'Address', 'Email', 'Phone', 'Age'])
        return df

data_generator = MimesisDataFactory(200)
fake_user_data_list = data_generator.generate_synthetic_data()
fake_user_data = data_generator.test_synthetic_data(fake_user_data_list)
fake_user_data.to_csv("mimesis_user_data.csv")