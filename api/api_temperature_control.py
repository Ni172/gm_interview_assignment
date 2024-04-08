import random


class ApiTemperatureControl:
    # Database of utterances, intents, and entities
    DB_UTTERANCES = ["Set temperature to 25 degrees", "Increase temperature"]
    DB_INTENTS = ["SetTemperature", "IncreaseTemperature"]
    DB_ENTITIES = ["temperature=25", "action=increase"]

    def call_api(self):
        """
        Simulates API response with random intents and entities.
        """
        intents = self.DB_INTENTS
        entities = self.DB_ENTITIES

        api_intent = random.choice(intents)
        api_entity = random.choice(entities)
        return api_intent, api_entity

    def calculating_similarity(self, expect: str, actual: str):
        """
        Calculates the similarity between expected and actual intents.
        """
        return "Similar" if expect == actual else "Non-similar"

    def similarity_percentage(self, count_similar: int, total_utterances: int):
        """
        Calculates the percentage of similarity.
        """
        return (count_similar / total_utterances) * 100
