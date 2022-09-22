from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/104.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
url = "https://www.amazon.in/Crucial-PC4-25600-SODIMM-260-Pin-Memory/" \
      "dp/B07Q8TNXKP/ref=sr_1_3?crid=2K6C5YFT8V926&keywords=" \
      "ram&qid=1661256964&sprefix=ram%2B%2Caps%2C257&sr=8-3&th=1"


responses = requests.get(url=url, headers=headers)

amazon_web = responses.text
soup = BeautifulSoup(amazon_web, "lxml")

heading = soup.find(name="div", id="apex_desktop", class_="celwidget", )

price = heading.getText()

new_price = price.strip()
x = new_price.split()
dot = x[1].split("₹")
price_int = dot[1]
price_ints = price_int.replace(",", "")
y = price_ints.split(".")

current_price = int(y[0])

if current_price < 4000:
    print("price drop")

    my_email = "nikhilpn360@gmail.com"
    password = "your password for smtplib"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr="from mail",
                            to_addrs="clinent",
                            msg=f"Subject: Crucial Ram Price Dropped\n\nThere is a Price Drop of {current_price} "
                                f"on amazon Buy Now{url}"
                            )

else:
    print("Not drop")
