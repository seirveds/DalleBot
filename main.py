from api_call import call_dalle_api
from prompt_model import PromptModel
from utils import images_to_grid, commentscraper_csv_to_corpus


CORPUS_FILENAME = "corpus.txt"

def main():
    # Preproces raw data to usable corpus
    commentscraper_csv_to_corpus(data_dir="raw_data", corpus_path=CORPUS_FILENAME)

    # Initialize model and fit on corpus
    model = PromptModel()
    model.fit_model(CORPUS_FILENAME)

    # Generate single prompt
    prompt = model.generate_prompt(n=1)[0]
    print(prompt)

    # Call dalle api with generated prompt, turn response into 3 by 3 grid with images
    response = call_dalle_api(prompt)
    image_grid = images_to_grid(response)

    # image_grid.show()

    image_grid.save(f"{prompt}.png")


if __name__ == "__main__":
    for _ in range(10):
        main()
