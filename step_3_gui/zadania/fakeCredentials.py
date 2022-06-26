from faker import Faker

faker = Faker()

username = faker.first_name() + "".join(faker.random_letters(length=5))
password = faker.password(length=10)
email = faker.ascii_email()

print(username)
print(password)
print(email)