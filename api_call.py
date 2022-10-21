from base64 import b64decode
import logging
import requests
import time


def call_dalle_api(query, max_retries=100):
    """ Calls dalle api with passed query."""
    # Because api could be overloaded, we use a for loop to make the request
    # If we get a status code 200 response we break the loop, otherwise we wait 2 seconds
    # and try again
    for _ in range(max_retries):
        logging.info("Making request...")
        response = requests.post("https://bf.dallemini.ai/generate", json={"prompt": query})
        if response.status_code == 200:
            # Turn raw response into dictionary
            response = response.json()
            # Print succes
            logging.info(f"Api succesfully returned content for query: '{query}'")
            break
        else:
            logging.info(f"Request returned status code {response.status_code}, trying again in 2 seconds")
            time.sleep(2)
    
    # Nine base64 decoded images in a list
    return [b64decode(img) for img in response["images"]]
