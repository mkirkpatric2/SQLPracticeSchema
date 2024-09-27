CREATE TYPE subscriptionTier AS ENUM ('free', 'paid', 'power');

CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	username VARCHAR(25) NOT NULL UNIQUE,
	subscriptionTier subscriptionTier,
	fName VARCHAR(25),
	lName VARCHAR(25),
	streetAddress VARCHAR(50),
	city VARCHAR(25),
	country VARCHAR(25),
	active90 BOOL NOT NULL
);

CREATE TABLE services (
    serviceID SERIAL PRIMARY KEY,
    serviceName VARCHAR(50) UNIQUE,
    tierMinimum subscriptionTier,
    paidTierProductDiscount INT,
    powerTierProductDiscount INT
);

CREATE TABLE serviceOfferings (
    offeringID SERIAL PRIMARY KEY,
    offeringTitle VARCHAR(25),
    offeredBy VARCHAR(50) UNIQUE REFERENCES services(serviceName)
);

CREATE TABLE subscriptions (
	subID SERIAL PRIMARY KEY,
	customerID INT NOT NULL references customers(id),
	offeringID INT NOT NULL references serviceOfferings(offeringID)
);

CREATE TABLE products (
	productID SERIAL PRIMARY KEY,
	productName VARCHAR(50) NOT NULL UNIQUE,
    productDescription VARCHAR(200),
    basePrice FLOAT NOT NULL,
    serviceConnection INT REFERENCES services(serviceID)
);

CREATE TABLE purchases (
	userID INT NOT NULL references customers(id),
	productID INT NOT NULL references products(productID)
);

