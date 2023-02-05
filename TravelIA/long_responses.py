import random

R_EATING = "No como nada porque soy un robot XD!"
R_QUIENSOY = "Soy el asistente virtual de Electrox. Preguntame lo que tu quieras....."
R_PRODUCTOS = "En esta pagina encontraras nuestro catalogo de productos: www.zlasosl.com"
R_UPDATE = "Para actualizar el software de tu teléfono Samsung, ve a Ajustes > Actualización de software > Descargar e instalar."
R_FABRICA = "Para restablecer los ajustes de fábrica del teléfono Samsung, ve a Ajustes > Gestión general > Restablecer > Restablecer datos de fábrica."



def unknown():
    response = ["¿Podrías por favor reformular eso? ",
                "...",
                "Suena bien.",
                "Que significa eso?"][
        random.randrange(4)]
    return response