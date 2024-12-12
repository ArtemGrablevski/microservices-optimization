import uuid
from datetime import datetime, timedelta
import random


def generate_sql_script(file_name, num_rows=10000):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("INSERT INTO auctions (auction_id, number_of_slots, entrance_ticket_price, location, date) VALUES\n")

        locations = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
        start_date = datetime(2023, 1, 1)

        for i in range(num_rows):
            auction_id = str(uuid.uuid4())
            number_of_slots = random.randint(1, 100)
            entrance_ticket_price = random.randint(10, 500)
            location = random.choice(locations)
            date = start_date + timedelta(days=random.randint(0, 365))

            f.write(
                f"('{auction_id}', {number_of_slots}, {entrance_ticket_price}, '{location}', '{date.strftime('%Y-%m-%d %H:%M:%S')}')"
            )
            
            if i < num_rows - 1:
                f.write(",\n")
            else:
                f.write(";\n")


generate_sql_script("insert_auctions.sql", num_rows=800_000)
