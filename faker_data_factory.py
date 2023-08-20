import uuid

from faker import Faker
from pyspark.sql import SparkSession


class Session:
    def session_create(self):
        spark = SparkSession.builder.appName("FakerDataFactory").getOrCreate()
        return spark

class FakerDataFactory():

    def __init__(self, quants):
        super().__init__()
        self.quants = quants



    def generate_synthetic_data(self):

        fake = Faker()
        name = []
        address = []
        zipcode = []
        email = []
        phone = []
        gender = []
        occupation = []
        company = []
        dob = []
        website = []
        username = []
        text = []
        country = []
        city = []
        state = []
        uuid_val = []
        ssn =[]
        credit_card = []

        for _ in range(self.quants):
            name.append(fake.name())
            address.append(fake.address())
            zipcode.append(fake.zipcode())
            email.append(fake.email())
            phone.append(fake.phone_number())
            gender.append(fake.random_element(elements=('Male', 'Female')))
            occupation.append(fake.job())
            company.append(fake.company())
            dob.append(fake.date_of_birth())
            website.append(fake.url())
            username.append(fake.user_name())
            text.append(fake.text())
            country.append(fake.country())
            city.append(fake.city())
            state.append(fake.state())
            uuid_val.append(fake.uuid4())
            ssn.append(fake.ssn())
            credit_card.append(fake.credit_card_number())

        return (
            name, address, zipcode, email, phone, gender, occupation,
            company, dob, website, username, text, country, city, state, uuid_val, ssn, credit_card
        )

    def do_logic(self):

        pass

    def fill_job_name(self):

        pass

    def test_synthetic_data(self):
        spark = Session.session_create(self)
        (
            n, a, z, e, p, g, occ, comp, dob, web, u, t, country, city, state,uuid_val, ssn, credit_card
        ) = FakerDataFactory.generate_synthetic_data(self)
        # print(spark)

        df = spark.createDataFrame(
            list(zip(n, a, z, e, p, g, occ, comp, dob, web, u, t, country, city, state,uuid_val, ssn, credit_card)),
            ['Name', 'Address', 'Zipcode', 'Email', 'Phone', 'Gender', 'Occupation',
             'Company', 'Date of Birth', 'Website', 'Username', 'Text', 'Country', 'City', 'State','uuid_val', 'ssn', 'credit_card']
        )
        df.show()

faker_job = FakerDataFactory(quants=10)
faker_job.test_synthetic_data()

        # df1 = df.dropDuplicates()
        # if df.count() == df1.count():
        #     print('nooo')
        # else:
        #     print('yes')