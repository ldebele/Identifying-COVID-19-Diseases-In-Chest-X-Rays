import json
from locust import HttpUser, task, constant


class LoadTest(HttpUser):
    wait_time = constant(0)
    host = "http://localhost:8080"


    @task
    def predict(self):
        img_path = './data/non_COVID.png'
        payload = {'file': (img_path, open(img_path, 'rb'))}

        # send a POST request to image prediction endpoint
        self.client.post("/predict", files=payload)

        # sent a GET request to home page
        # headers = {"Content-Type": "application/"}
        # response = self.client.get("/home", headers=headers)

       




