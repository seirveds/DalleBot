import markovify


class PromptModel:
    def __init__(self):
        self.model = None

    def fit(self, corpus_path, state_size=3):
        """ """
        corpus = self.load_data(corpus_path)

        self.model = markovify.NewlineText(corpus, state_size=state_size)
        self.model = self.model.compile()

    def generate_prompt(self, n=1):
        """ Generate n random prompts. """
        # Need a high number for tries to prevent returning Nones
        return [self.model.make_sentence(tries=999) for _ in range(n)]

    @staticmethod
    def load_data(corpus_path):
        """ Loads .txt file with every sentence on a separate line to string. """
        with open(corpus_path, "r", encoding="utf8") as f:
            corpus = f.read()

        return corpus
