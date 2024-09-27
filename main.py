from Data import customerData as cd
from Data import serviceData as sd


def populateCustomers():
    f = open("./populateCustomers.sql", 'w')
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
    f = open("./populateServices.sql", 'w')
    f.write("INSERT INTO services (serviceName, tierMinimum"
            ", paidTierProductDiscount, powerTierProductDiscount)"
            "\nVALUES\n")
    for x in range(14):
        f.write(f"('{sd.serviceName[x]}', '{cd.subscriptionTier[x]}',"
                 f"{sd.lowDiscount[x]}, {sd.highDiscount[x]}),\n")
    f.write(f"('{sd.serviceName[x]}', '{cd.subscriptionTier[x]}',"
            f"{sd.lowDiscount[x]}, {sd.highDiscount[x]});\n")
    f.close()

def main():
    populateCustomers()
    populateServices()
    print("Done!")








if __name__ == '__main__':
    main()
