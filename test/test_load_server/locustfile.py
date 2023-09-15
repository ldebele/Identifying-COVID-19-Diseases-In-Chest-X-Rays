import random, io
from PIL import Image
from locust import HttpUser, task, constant


class LoadTest(HttpUser):
    wait_time = constant(0)
    host = "http://localhost:8000"

    @task
    def home(self):
        # sent a GET request to home page endpoints
        headers = {"Content-Type": "application/"}
        self.client.get("/home", headers=headers)


    @task
    def predict(self):
        width = 224
        height = 224 

        img = Image.new('1', (width, height))
        pixels = img.load()
        for x in range(width):
            for y in range(height):
                pixel_value = random.choice([0,1])
                pixels[x, y] = pixel_value


        # Convert the image to bytes and create a BytesIO stream
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format="PNG")
        img_byte_array.seek(0)

        payload = {"file": ("test_img.png", img_byte_array)}


        # send a POST request to image prediction endpoint
        self.client.post("/predict", files=payload)
      

       




