"""
Available Data
serviceName
lowDiscount
powerTierProductDiscount

"""
import random

lowDiscount = []
highDiscount = []

for x in range(20):
    lowDiscount.append(random.randint(1, 10))
    highDiscount.append(lowDiscount[x] + random.randint(3, 7))

serviceName = [
    "Web Hosting",
    "Cloud Storage",
    "Email Marketing",
    "SEO Optimization",
    "Social Media Management",
    "Online Payment Processing",
    "Graphic Design",
    "Content Creation",
    "Virtual Assistant Services",
    "IT Support",
    "Data Backup Solutions",
    "Website Development",
    "Digital Marketing",
    "App Development",
    "Consulting Services"
]

