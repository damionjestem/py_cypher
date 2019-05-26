dictionary = {
  "a": "y",
  "e": "i",
  "i": "o",
  "o": "a",
  "y": "e",
}


def cypher(user_input):
    result = str()
    for i in range(len(user_input)):
        if user_input[i] in dictionary:
            result = result + dictionary[user_input[i]]
        else:
            result = result + user_input[i]

    return result


dictionary_reversed = {
    "y": "a",
    "i": "e",
    "o": "i",
    "a": "o",
    "e": "y",
}


def decypher(user_input):
    result = str()
    for i in range(len(user_input)):
        if user_input[i] in dictionary_reversed:
            result = result + dictionary_reversed[user_input[i]]
        else:
            result = result + user_input[i]

    return result
