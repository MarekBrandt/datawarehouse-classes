import datetime
import random as rand

from faker import Faker
from faker.providers import DynamicProvider

from advertisement import Advertisement
from advertisers import Advertiser
from customers import Customer
from product_amount import ProductAmount
from products import Product
from questionnaire import Questionnaire
from salon import Salon
from service import Service
from service_visit import ServiceVisit
from visit import Visit

fake = Faker()
Faker.seed(0)
t0 = 2015
t1 = 2017

questionnaire_data = []
advertisements_data = []
services_data = []
services_data2 = []
products_data = []
customers_data = []
salons_data = []
visit_data = []
advertisers_data = []
services = ["manicure klasyczny", "pedicure klasyczny", "regulacja brwi",
            "henna brwi", "henna rzes", "strzyzenie meskie",
            "przycinanie brody", "przycinanie wasa",
            "manicure hybrydowy", "pedicure hybrydowy", "strzyzenie damskie",
            "brwi permanentne", "usta permanentne", "pielegnacja brody",
            "pielegnacja wasa"]

PRODUCTS_COUNT = 30

CUSTOMERS_COUNT = 1000

SALONS_COUNT = 10

ADVERTISERS_COUNT = 50

VISIT_COUNT1 = 1000
VISIT_COUNT2 = 500
thematics = ["samochodowa", "kulinarna", "odziezowa", "obuwnicza", "meblowa", "sprzetowa", "weselna",
             "salony pieknosci"]

specializations = ["ulotki", "billboardy", "reklamy internetowe"]

ad_specializations = ["ulotka", "billboard", "reklama internetowa"]

thematics_provider = DynamicProvider(
    provider_name="thematic",
    elements=thematics
)

specializations_provider = DynamicProvider(
    provider_name="specialization",
    elements=specializations
)
service_provider = DynamicProvider(
    provider_name="service",
    elements=services
)
ad_specializations_provider = DynamicProvider(
    provider_name="ad_specialization",
    elements=ad_specializations
)

fake.add_provider(service_provider)
fake.add_provider(thematics_provider)
fake.add_provider(specializations_provider)
fake.add_provider(ad_specializations_provider)


def generate_services(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, len(services)):
            serv = Service(i + 1, services[i], rand.randint(2000, 10000) / 100)
            services_data.append(serv)
            file.write(serv.bulk_format() + '\n')


def update_service_prices(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, len(services_data)):
            serv = services_data[i]
            new_serv = Service(serv.id, serv.name, serv.price * 1.2)
            services_data2.append(new_serv)
            file.write(new_serv.bulk_format() + '\n')


def generate_products(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, PRODUCTS_COUNT + 1):
            prod = Product(i, "Product" + str(i), "Brand" + str(rand.randint(1, 8)), "Type" + str(rand.randint(1, 6)),
                           rand.randint(2000, 20000) / 100)
            products_data.append(prod)
            file.write(prod.bulk_format() + '\n')


def generate_customers(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, CUSTOMERS_COUNT + 1):
            cust = Customer(i, fake.first_name(), fake.last_name(), rand.randint(1950, 2010))
            customers_data.append(cust)
            file.write(cust.bulk_format() + '\n')


def generate_advertisers(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, ADVERTISERS_COUNT + 1):
            advertiser = Advertiser(i, "Company" + str(i) + "@gmail.com", "Company" + str(i), fake.msisdn()[3:],
                                    fake.specialization(), fake.thematic())
            advertisers_data.append(advertiser)
            file.write(advertiser.bulk_format() + '\n')


def generate_advertisement(file_name, number):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, number + 1):
            price = rand.randint(50000, 1000000) / 100
            num1 = rand.randint(0, len(services_data) * 2) * 0.75
            if num1 >= len(services_data):
                num1 = ""
            num1 = str(num1)
            num2 = rand.randint(1, len(salons_data) - 1)
            num3 = rand.randint(1, len(advertisers_data) - 1)
            ad = Advertisement(i, num1, str(num2), str(num3), fake.ad_specialization(), price)
            advertisements_data.append(ad)
            file.write(ad.bulk_format() + '\n')


def generate_salon(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, SALONS_COUNT + 1):
            salon = Salon(i, fake.city(), fake.street_name(), rand.randint(1, 100), fake.msisdn()[4:])
            salons_data.append(salon)
            file.write(salon.bulk_format() + '\n')


def generate_visit(file_name, number, mode):
    if mode == 'a':
        start = VISIT_COUNT1 + 1
        end = VISIT_COUNT1 + VISIT_COUNT2
    else:
        start = 1
        end = VISIT_COUNT1
    with open(file_name, mode, encoding='utf-8') as file:
        for i in range(start, end):
            num1 = rand.randint(1, len(salons_data) - 1)
            num2 = rand.randint(1, len(customers_data) - 1)
            min_date = datetime.date(t0, 1, 1)
            max_date = datetime.date(t1, 1, 1)
            reservation_date = fake.date_between_dates(min_date, max_date)
            max_visit_date = reservation_date + datetime.timedelta(days=30)
            visit_date = fake.date_between_dates(reservation_date, max_visit_date)
            cancel_date = ''
            if rand.randint(1, 10) == 1:
                cancel_date = fake.date_between_dates(reservation_date, visit_date)
            visit = Visit(i, num1, num2, str(reservation_date), str(visit_date), str(cancel_date),
                          str(rand.randint(5000, 30000) / 100))
            visit_data.append(visit)
            file.write(visit.bulk_format() + '\n')


def generate_service_visit(file_name, mode):
    if (mode == 'a'):
        start = VISIT_COUNT1 + 1
        end = VISIT_COUNT1 + VISIT_COUNT2 + 1
    else:
        start = 1
        end = VISIT_COUNT1 + 1

    with open(file_name, mode, encoding='utf-8') as file:
        for i in range(start, end):
            how_many = rand.randint(0, 10)
            if how_many < 6:
                how_many = 1
            elif how_many < 10:
                how_many = 2
            else:
                how_many = 3
            service_list = []
            for j in range(0, how_many):
                service_id = rand.randint(0, len(services_data) - 1) + 1
                while service_id in service_list:
                    service_id = rand.randint(0, len(services_data) - 1) + 1
                service_list.append(service_id)
                ser_vis = ServiceVisit(i, service_id)
                file.write(ser_vis.bulk_format() + '\n')


def generate_product_amount(file_name, number, mode):
    if mode == 'a':
        start = VISIT_COUNT1 + 1
        end = VISIT_COUNT1 + VISIT_COUNT2
    else:
        start = 1
        end = VISIT_COUNT1
    with open(file_name, mode, encoding='utf-8') as file:
        for i in range(1, number+1):
            prod_amo = ProductAmount(rand.randint(start, end), rand.randint(1, len(products_data)),rand.randint(1, 4))
            file.write(prod_amo.bulk_format() + '\n')


def generate_questionnaire(file_name, number, mode):
    if mode == 'w':
        visits = visit_data[0:number]
    else:
        visits = visit_data[VISIT_COUNT1+1:VISIT_COUNT1+VISIT_COUNT2-1]
    with open(file_name, mode, encoding='utf-8') as file:
        used = []
        for i in range(0, number):

            not_found = True
            while not_found:
                visit = rand.choice(visits)
                if visit not in used:
                    used.append(visit)
                    not_found = False

            visit_id = visit.id

            ad_id = ""

            if rand.randint(1, 10) < 3:
                ad_is_cause = 'nie'
            else:
                ad_is_cause = 'tak'

            if rand.randint(1, 10) < 3:
                ad_seen = 'nie'
            else:
                ad_seen = 'tak'
                valid_ads = []
                for ad in advertisements_data:
                    if str(ad.salon_id) == str(visit.salon_id):
                        valid_ads.append(ad)
                ad_id = str(rand.choice(valid_ads).id)

            points = rand.randint(1, 10)

            column = Questionnaire(ad_id, ad_is_cause, ad_seen, points, visit_id)
            questionnaire_data.append(column)
            file.write(column.csv_format() + '\n')

def generate(time0, time1):
    t0 = time0
    t1 = time1
    if (t0 == 2015):
        generate_services("Dane/uslugi.bulk")
        generate_products("Dane/produkty.bulk")
        generate_customers("Dane/klienci.bulk")
        generate_salon("Dane/salony.bulk")
        generate_advertisers("Dane/reklamodawcy.bulk")
        generate_advertisement("Dane/reklamy.bulk", 1000)
        generate_visit("Dane/wizyty.bulk", VISIT_COUNT1, 'w')
        generate_service_visit("Dane/uslugi_wizyty.bulk", 'w')
        generate_product_amount("Dane/produkty_ilosc.bulk", 800,'w')
        generate_questionnaire("Dane/ankiety.csv", 200, "w")
    else:
        update_service_prices("Dane/uslugi.bulk")
        generate_visit("Dane/wizyty.bulk", VISIT_COUNT2, 'a')
        generate_service_visit("Dane/uslugi_wizyty.bulk", 'a')
        generate_product_amount("Dane/produkty_ilosc.bulk", 500, 'a')
        generate_questionnaire("Dane/ankiety.csv", 100, "a")


    # generate_portal("Dane/portale.bulk", 10)

    # generate_questionnaire("Dane/ankiety.csv", 10)


if __name__ == '__main__':
    generate(t0, t1)
    generate(2017, 2020)
