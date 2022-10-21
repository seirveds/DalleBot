if __name__ == "__main__":
    import logging
    from dallebot import DalleBot

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    bot = DalleBot("corpus.txt")
    bot.make_tweet()
