from locust import HttpUser, task, between, LoadTestShape
import random


existing_ids = (
    "000bbb62-760a-449e-a657-f660c8ac560f",
    "000caeb4-50df-40e4-82b4-04037dc51316",
    "000a9f35-b42e-456d-920d-9c9a34510dce",
    "000032ef-1b42-4bce-b481-d683be261e95",
    "801677dd-a7f2-4b52-95cd-ff5e3cd16f73",
    "80188724-9cb8-4fe1-ad0b-a962f4b8de8a",
    "8022f2a2-cced-4474-ae6a-435733496c6a",
    "80336c4d-aeea-465a-9fc4-9c51e4d3237c",
)

not_existing_ids = (
    "000bbb62-760a-449e-a657-f660c8ac560d",
    "000caeb4-50df-40e4-82b4-04037dc51313",
    "000a9f35-b42e-456d-920d-9c9a34510dca",
    "000032ef-1b42-4bce-b481-d683be261e91",
    "801677dd-a7f2-4b52-95cd-ff5e3cd16f70",
    "80188724-9cb8-4fe1-ad0b-a962f4b8de8b",
    "8022f2a2-cced-4474-ae6a-435733496c6b",
    "80336c4d-aeea-465a-9fc4-9c51e4d3237b",
    "670db653-971d-49f6-b883-70613cea393b",
    "e13e42df-69ad-4162-a099-ca115e03cc4b",
)

locations = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]


class AuctionTestUser(HttpUser):
    wait_time = between(0.1, 1)

    @task
    def get_all_auctions(self):
        self.client.get("/api/auctions")

    @task
    def create_auction(self):
        data = {
            "number_of_slots": random.randint(1, 100),
            "entrance_ticket_price": random.randint(10, 500),
            "location": random.choice(locations),
            "date": "2024-12-10T12:00:00"
        }
        self.client.post("/api/auctions", json=data)

    @task
    def get_auction_by_id(self):
        self.client.get(f"/api/auctions/{random.choice(existing_ids)}")

    # @task
    # def update_auction(self):
    #     auction_id = random.choice(not_existing_ids)
    #     data = {
    #         "number_of_slots": random.randint(1, 100),
    #         "entrance_ticket_price": random.randint(10, 500),
    #         "location": "Updated Location",
    #         "date": "2024-12-11T12:00:00"
    #     }
    #     self.client.put(f"/api/auctions/{auction_id}", json=data)

    # @task
    # def delete_auction(self):
    #     auction_id = random.choice(not_existing_ids)
    #     self.client.delete(f"/api/auctions/{auction_id}")
