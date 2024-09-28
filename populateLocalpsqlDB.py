from sqlalchemy import create_engine, text
engine = create_engine('postgresql+psycopg2://localhost:5432/postgres')

with engine.connect() as con:
    with open("./createTables.sql") as file:
        query = text(file.read())
        con.execute(query)

    with open("./popScripts/populateCustomers.sql") as file:
        query = text(file.read())
        con.execute(query)

    with open("./popScripts/populateServices.sql") as file:
        query = text(file.read())
        con.execute(query)

    with open("./popScripts/populateServiceOfferings.sql") as file:
        query = text(file.read())
        con.execute(query)

    with open("./popScripts/populateSubscriptions.sql") as file:
        query = text(file.read())
        con.execute(query)

    with open("./popScripts/populateProducts.sql") as file:
        query = text(file.read())
        con.execute(query)

    with open("./popScripts/populatePurchases.sql") as file:
        query = text(file.read())
        con.execute(query)

    con.commit()
    con.close()
