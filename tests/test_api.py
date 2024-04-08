import pytest

from api.api_temperature_control import ApiTemperatureControl


# Fixture to initialize the API driver
@pytest.fixture(scope="module")
def api_driver():
    api_driver = ApiTemperatureControl()
    return api_driver


# Test function with parameterization
@pytest.mark.parametrize("pass_criteria", [30])
def test_sequence(api_driver, pass_criteria):
    similar_intents = 0
    similar_entities = 0
    utterances = ["Set temperature to 25 degrees", "Increase temperature"]
    actual_intents = ["SetTemperature", "IncreaseTemperature"]
    actual_entities = ["temperature=25", "action=increase"]

    # Printing table header
    print("Utterance\tActual intent\tActual entity\tAPI intent\tAPI entity\tIntent Similarity\tEntity Similarity")

    # Iterating through each utterance
    for i in range(len(utterances)):
        utterance = utterances[i]
        expected_intent = actual_intents[i]
        expected_entity = actual_entities[i]

        # Calling API
        api_intent, api_entity = api_driver.call_api()

        # Calculating similarity
        intent_similarity = api_driver.calculating_similarity(expected_intent, api_intent)
        entity_similarity = api_driver.calculating_similarity(expected_entity, api_entity)

        # Updating similar intents and entities count
        if intent_similarity == "Similar":
            similar_intents += 1
        if entity_similarity == "Similar":
            similar_entities += 1

        # Printing results log
        print(
            f"{utterance}\t{expected_intent}\t{expected_entity}\t{api_intent}\t{api_entity}\t{intent_similarity}\t{entity_similarity}")

    # Calculating similarity percentages
    intent_similarity_percentage = api_driver.similarity_percentage(similar_intents, len(utterances))
    entity_similarity_percentage = api_driver.similarity_percentage(similar_entities, len(utterances))

    # Checking pass criteria
    assert intent_similarity_percentage >= pass_criteria and entity_similarity_percentage >= pass_criteria
