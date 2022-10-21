import io
import logging
from api_call import call_dalle_api
from prompt_model import PromptModel
from twitter_api import TwitterAPI
from utils import commentscraper_csv_to_corpus, clean_prompt, images_to_grid


class DalleBot:

    def __init__(self, corpus_path):
        self.corpus_path = corpus_path
        self.model = self.fit_prompt_model()

        self.twitter_api = TwitterAPI()

    def process_raw_data(self, data_dir):
        """ Only used locally, no data processing in production. """
        commentscraper_csv_to_corpus(
            data_dir=data_dir, corpus_path=self.corpus_path
        )

    def fit_prompt_model(self):
        """ Use corpus to fit promt model. """
        model = PromptModel()
        model.fit(self.corpus_path)
        return model

    def generate_prompt(self):
        """ Use fitted model to generate single prompt. """
        prompt = self.model.generate_prompt(n=1)[0]
        # Remove tokens not allowed in filenames, as we use the prompt
        # as the filename of the generated image
        prompt = clean_prompt(prompt)
        return prompt

    def make_tweet(self, prompt=None):
        """ Generates promt from promp model, calls DalleMini api, and posts returned images as tweet. """
        # Random prompt if nothing passed, otherwise we use
        # passed prompt
        if prompt is None:
            prompt = self.generate_prompt()

        # Calls api and returns image as bytes
        image_bytes = self.generate_image(prompt)

        # Use twitter api to post image
        self.twitter_api.post_tweet(
            status=f"{prompt} #dalle #dalle2 #dallemini #bot",
            filename=f"{prompt}.png",
            file=image_bytes
        )

        logging.info("Succesfully posted tweet")

    @staticmethod
    def generate_image(prompt=None):
        """
        Calls dalle api with passed prompt. Returns image as bytes
        to prevent saving and loading file to disk.
        """
        dalle_api_response = call_dalle_api(prompt)
        image_grid = images_to_grid(dalle_api_response)

        # Turn image into bytes to prevent having to save and load image from local disk (cant do this in serverless environment)
        image_io = io.BytesIO()
        image_grid.save(image_io, format="png")
        # Get bytes from io object
        image_bytes = image_io.getvalue()

        return image_bytes
