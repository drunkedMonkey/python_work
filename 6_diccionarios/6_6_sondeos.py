favourite_languajes={
    'Ivan': 'Python',
    'Sami': 'C',
    'Blanca':'Java'
}

favourite_languajes_sondeo={
    'Ivan': 'Python',
    'Sami': 'C',
    'Blanca':'Java',
    'Luis':'Python',
    'Sandra':'C#'
}

for name, languaje in favourite_languajes_sondeo.items():
    if name in favourite_languajes.keys():
        print(name + " gracias por responder.")
    else:
        print(name + " por favor responde la encuesta.")

