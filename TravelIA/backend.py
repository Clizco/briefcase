import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=None):
    if required_words is None:
        required_words = []
    message_certainty = 0
    has_required_words = True


    for word in user_message:
        if word in recognised_words:
            message_certainty += 1


    percentage = float(message_certainty) / float(len(recognised_words))


    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break


    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}


    def response(bot_response, list_of_words, single_response=False, required_words=None):
        if required_words is None:
            required_words = []
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Respuestas cortas -------------------------------------------------------------------------------------------------------
    response('Hola!', ['hola', 'ola', 'hi'], single_response=True)
    response('Hasta luego!', ['adios', 'bye'], single_response=True)
    response('Estoy bien y tu?', ['como', 'estas'], required_words=['estas'])
    response('No hay de que!', ['gracias', 'muchas'], single_response=True)
    response('Te lo agradezco', ['que', 'crack', 'eres'], required_words=['crack', 'eres'])

    # Respuestas largas
    response(long.R_EATING, ['que', 'tu', 'comes'], required_words=['que', 'comes'])
    response(long.R_QUIENSOY, ['quien', 'eres', 'tu'], required_words=['quien', 'eres'])
    response(long.R_UPDATE, ['como', 'actualizar', 'actualizo', 'mi' 'telefono', 'Samsung'], required_words=['telefono'])
    response(long.R_FABRICA, ['como', 'restablezco', 'de', 'fabrica', 'mi', 'celular', 'Samsung'], required_words=['restablezco', 'fabrica'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)


    return long.unknown() if highest_prob_list[best_match] < 1 else best_match



def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response



while True:
    print('Zap: ' + get_response(input('Tu: ')))