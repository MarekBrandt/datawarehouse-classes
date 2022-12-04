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


def generate_services(files):
    for i in range(0, len(services)):
        serv = Service(i + 1, services[i], rand.randint(2000, 10000) / 100)
        services_data.append(serv)
    for file_name in files:
        with open(file_name, 'w', encoding='utf-8') as file:
            for serv in services_data:
                file.write(serv.bulk_format() + '\n')


def update_advertisers(files):
    for file_name in files:
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in range(0, len(advertisers_data)):
                adv = advertisers_data[i]
                new_adv = None
                random_numb = rand.randint(1,10)
                if random_numb < 2:
                    new_adv = Advertiser(adv.id, adv.email, adv.name, adv.nip, fake.specialization(), fake.thematic())
                elif random_numb < 4:
                    new_adv = Advertiser(adv.id, adv.email, adv.name, adv.nip, adv.specialization, fake.thematic())
                elif random_numb < 6:
                    new_adv = Advertiser(adv.id, adv.email, adv.name, adv.nip, fake.specialization(), adv.thematic)
                else:
                    new_adv = Advertiser(adv.id, adv.email, adv.name, adv.nip, adv.specialization, adv.thematic)
                services_data2.append(new_adv)
                file.write(new_adv.bulk_format() + '\n')


def generate_products(files):
    for i in range(1, PRODUCTS_COUNT + 1):
        prod = Product(i, "Product" + str(i), "Brand" + str(rand.randint(1, 8)), "Type" + str(rand.randint(1, 6)),
                       rand.randint(2000, 20000) / 100)
        products_data.append(prod)
    for file_name in files:
        with open(file_name, 'w', encoding='utf-8') as file:
           for prod in products_data:
                file.write(prod.bulk_format() + '\n')


def generate_customers(files, number, mode):
    customer_temp = []
    if (mode == 'w'):
        start = 1
        end = number + 1
    else:
        start = len(customers_data) + 1
        end = start + number + 1
    for i in range(start, end):
        cust = Customer(i, fake.first_name(), fake.last_name(), rand.randint(1950, 2010))
        customers_data.append(cust)
        customer_temp.append(cust)
    for file_name in files:
        with open(file_name, mode, encoding='utf-8') as file:
            for cust in customer_temp:
                file.write(cust.bulk_format() + '\n')


def generate_advertisers(files):
    for i in range(1, ADVERTISERS_COUNT + 1):
        advertiser = Advertiser(i, "Company" + str(i) + "@gmail.com", "Company" + str(i), fake.msisdn()[3:],
                                fake.specialization(), fake.thematic())
        advertisers_data.append(advertiser)
    for file_name in files:
        with open(file_name, 'w', encoding='utf-8') as file:
            for advertiser in advertisers_data:
                file.write(advertiser.bulk_format() + '\n')


def generate_advertisement(files, number):
    for i in range(1, number + 1):
        price = rand.randint(50000, 1000000) / 100
        num1 = rand.randint(1, len(services_data))
        if rand.randint(1, 10) < 3:
            num1 = ""
        num2 = rand.randint(1, len(salons_data))
        num3 = rand.randint(1, len(advertisers_data))
        ad = Advertisement(i, str(num1), str(num2), str(num3), fake.ad_specialization(), price)
        advertisements_data.append(ad)
    for file_name in files:
        with open(file_name, 'w', encoding='utf-8') as file:
            for ad in advertisements_data:
                file.write(ad.bulk_format() + '\n')


def generate_salon(files):
    for i in range(1, SALONS_COUNT + 1):
        salon = Salon(i, fake.city(), fake.street_name(), rand.randint(1, 100), fake.msisdn()[4:])
        salons_data.append(salon)
    for file_name in files:
        with open(file_name, 'w', encoding='utf-8') as file:
            for salon in salons_data:
                file.write(salon.bulk_format() + '\n')


def generate_visit(files, mode):
    visit_temp = []
    if mode == 'a':
        start = VISIT_COUNT1 + 1
        end = VISIT_COUNT1 + VISIT_COUNT2
    else:
        start = 1
        end = len(customers_data) + 1

    for i in range(start, end):
        num1 = rand.randint(1, len(salons_data))
        num2 = i
        how_many = rand.randint(0, 10)
        if how_many < 6:
            how_many = 1
        elif how_many < 10:
            how_many = 2
        else:
            how_many = 3
        for j in range(0, how_many):
            min_date = datetime.date(t0, 1, 1)
            max_date = datetime.date(t1, 12, 1)
            reservation_date = fake.date_between_dates(min_date, max_date)
            max_visit_date = reservation_date + datetime.timedelta(days=30)
            visit_date = fake.date_between_dates(reservation_date, max_visit_date)
            cancel_date = ''
            if rand.randint(1, 10) == 1:
                cancel_date = fake.date_between_dates(reservation_date, visit_date)
            visit = Visit(len(visit_data) + 1, num1, num2, str(reservation_date), str(visit_date), str(cancel_date),
                          str(rand.randint(5000, 30000) / 100))
            visit_data.append(visit)
            visit_temp.append(visit)
    for file_name in files:
        with open(file_name, mode, encoding='utf-8') as file:
            for visit in visit_temp:
                    file.write(visit.bulk_format() + '\n')


def generate_service_visit(files, mode):
    ser_vis_temp = []
    if mode == 'a':
        start = VISIT_COUNT1 + 1
        end = VISIT_COUNT1 + VISIT_COUNT2 + 1
    else:
        start = 1
        end = VISIT_COUNT1 + 1

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
            ser_vis_temp.append(ser_vis)
    for file_name in files:
        with open(file_name, mode, encoding='utf-8') as file:
            for ser_vis in ser_vis_temp:
                    file.write(ser_vis.bulk_format() + '\n')


def generate_product_amount(files, number, mode):
    prod_amo_temp = []
    if mode == 'a':
        start = VISIT_COUNT1 + 1
        end = len(visit_data) + 1
    else:
        start = 1
        end = VISIT_COUNT1

    used = []
    for i in range(1, number + 1):
        not_found = True
        while not_found:
            visit_id = rand.randint(start, end)
            product_id = rand.randint(1, len(products_data))
            if (visit_id, product_id) not in used:
                used.append((visit_id, product_id))
                not_found = False
        prod_amo = ProductAmount(visit_id, product_id, rand.randint(1, 4))
        prod_amo_temp.append(prod_amo)
    for file_name in files:
        with open(file_name, mode, encoding='utf-8') as file:
            for prod_amo in prod_amo_temp:
                file.write(prod_amo.bulk_format() + '\n')


def generate_questionnaire(files, number, mode):
    questionnaire_temp = []
    if mode == 'w':
        visits = visit_data
    else:
        visits = visit_data[VISIT_COUNT1 + 1:VISIT_COUNT2 - 1]

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
            if not len(valid_ads):
                ad_id = ''
            else:
                ad_id = str(rand.choice(valid_ads).id)

        points = rand.randint(1, 10)

        column = Questionnaire(ad_id, ad_is_cause, ad_seen, points, visit_id)
        questionnaire_data.append(column)
        questionnaire_temp.append(column)
    for file_name in files:
        with open(file_name, mode, encoding='utf-8') as file:
            for column in questionnaire_temp:
                file.write(column.csv_format() + '\n')


def generate(time0, time1):
    global t0
    global t1
    t0 = time0
    t1 = time1
    if t0 == 2015:
        generate_services(["Dane/uslugi.bulk", "Dane/uslugi2.bulk"])
        generate_products(["Dane/produkty.bulk", "Dane/produkty2.bulk"])
        generate_customers({"Dane/klienci.bulk", "Dane/klienci2.bulk"}, 800, "w")
        generate_salon(["Dane/salony.bulk", "Dane/salony2.bulk"])
        generate_advertisers(["Dane/reklamodawcy.bulk", "Dane/reklamodawcy2.bulk"])
        generate_advertisement(["Dane/reklamy.bulk", "Dane/reklamy2.bulk"], 1000)
        generate_visit(["Dane/wizyty.bulk", "Dane/wizyty2.bulk"], 'w')
        global VISIT_COUNT1
        VISIT_COUNT1 = len(visit_data)
        generate_service_visit(["Dane/uslugi_wizyty.bulk", "Dane/uslugi_wizyty2.bulk"], 'w')
        generate_product_amount(["Dane/produkty_ilosc.bulk", "Dane/produkty_ilosc2.bulk"], 800, 'w')
        generate_questionnaire(["Dane/ankiety.csv", "Dane/ankiety2.csv"], 200, "w")
    else:
        generate_customers(["Dane/klienci2.bulk"], 500, "a")
        update_advertisers(["Dane/reklamodawcy2.bulk"])
        generate_visit(["Dane/wizyty2.bulk"], 'a')
        global VISIT_COUNT2
        VISIT_COUNT2 = len(visit_data)
        generate_service_visit(["Dane/uslugi_wizyty2.bulk"], 'a')
        generate_product_amount(["Dane/produkty_ilosc2.bulk"], 500, 'a')
        generate_questionnaire(["Dane/ankiety2.csv"], 100, "a")


if __name__ == '__main__':
    generate(t0, t1)
    generate(2017, 2020)
