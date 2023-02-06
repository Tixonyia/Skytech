from django_seed import Seed
seeder = Seed.seeder(locale='sv_SE')
print(seeder.faker.name())