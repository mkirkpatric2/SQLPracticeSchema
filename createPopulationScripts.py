from Data import customerData as cd
from Data import serviceData as sd
from Data import productData as pd
import random


def populateCustomers():
    f = open("./popScripts/populateCustomers.sql", 'w')
    f.write("INSERT INTO customers (username, subscriptionTier"
            ", fName, lName, streetAddress, city, country, active90)"
            "\nVALUES\n")
    for x in range(40):
        f.write(f"('{cd.usernames[x]}', '{cd.subscriptionTier[x]}',"
                f"'{cd.firstNames[x]}', '{cd.lastNames[x]}', "
                f"'{cd.streetAddresses[x]}', '{cd.cities[x]}',"
                f"'United States', {cd.bools[x]}),\n")
    f.write(f"('{cd.usernames[40]}', '{cd.subscriptionTier[40]}',"
            f"'{cd.firstNames[40]}', '{cd.lastNames[40]}', "
            f"'{cd.streetAddresses[40]}', '{cd.cities[40]}',"
            f"'United States', {cd.bools[40]});\n")
    f.close()


def populateServices():
    f = open("./popScripts/populateServices.sql", 'w')
    f.write("INSERT INTO services (serviceName, tierMinimum"
            ", paidTierProductDiscount, powerTierProductDiscount)"
            "\nVALUES\n")
    for x in range(14):
        f.write(f"('{sd.serviceName[x]}', '{cd.subscriptionTier[x]}',"
                f"{sd.lowDiscount[x]}, {sd.highDiscount[x]}),\n")
    f.write(f"('{sd.serviceName[14]}', '{cd.subscriptionTier[14]}',"
            f"{sd.lowDiscount[14]}, {sd.highDiscount[14]});\n")
    f.close()


def populateServiceOfferings():
    f = open("./popScripts/populateServiceOfferings.sql", 'w')
    f.write("INSERT INTO serviceOfferings (offeringTitle, offeredBy)"
            "\nVALUES\n")
    for x in range(14):
        for y in range(5):
            f.write(f"('{sd.offeringName[y]}', '{sd.serviceName[x]}'),\n")

    f.write(f"('{sd.offeringName[0]}', '{sd.serviceName[14]}');\n")
    f.close()


def populateSubscriptions():
    f = open("./popScripts/populateSubscriptions.sql", 'w')
    # 41 cust 71 offerings
    f.write("INSERT INTO subscriptions (customerID, offeringID)"
            "\nVALUES\n")

    for x in range(115):
        f.write(f"({random.randint(1, 41)}, {random.randint(1, 71)}),\n")

    f.write(f"({random.randint(1, 41)}, {random.randint(1, 71)});")

    f.close()


def populateProducts():
    f = open("./popScripts/populateProducts.sql", 'w')
    f.write("INSERT INTO products (productName, basePrice,"
            "serviceConnection)"
            "\nVALUES\n")

    for x in range(24):
        f.write(f"('{pd.products[x]}', {pd.prices[x]}, {random.randint(1, 15)}),\n")

    f.write(f"('{pd.products[24]}', {pd.prices[24]}, {random.randint(1, 15)});\n")
    f.close()


def populatePurchases():
    f = open("./popScripts/populatePurchases.sql", 'w')
    f.write("INSERT INTO purchases (userID, productID)"
            "\nVALUES\n")

    for x in range(250):
        f.write(f"({random.randint(1, 39)}, {random.randint(1, 25)}),\n")

    f.write(f"({random.randint(1, 41)}, {random.randint(1, 25)});\n")
    f.close()


def createPopulationScripts():
    populateCustomers()
    populateServices()
    populateServiceOfferings()
    populateSubscriptions()
    populateProducts()
    populatePurchases()
    print("Done!")


createPopulationScripts()
