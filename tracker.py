import csv
import requests
import json

def getOrder(ordernr, plz):
    r = requests.get("https://data.smartagent.io/v1/jdsports/track-my-order?orderNumber="+ordernr+"&facia=jdsportsat&postcode="+plz)
    j = json.loads(r.text)
    message = j["message"]["text"]
    date = j["date"]
    payment = j["payment"]["type"]
    amount = j["totals"]["total"]["amount"] + " " + j["totals"]["total"]["currency"]
    tracking = j["delivery"]["trackingURL"]
    img = j["vendors"][0]["items"][0]["img"]
    name = j["vendors"][0]["items"][0]["name"]
    print(ordernr + " | " + date + " - " + name + " - " + payment + " " + amount + " >>> " + message)

while True:
    print(">>>scrape?")
    input()
    with open("orders.csv", 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader, None)
        for row in csv_reader:
            ordernr = row[0].replace("#","")
            plz = row[1]
            getOrder(ordernr, plz)
