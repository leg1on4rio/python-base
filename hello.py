#!/usr/bin/env python3

"""Hello World multi language.

Dependendo da lingua configurada no ambiente, o script exibe a mensagem de 
forma apropriada.

Como usar:

Tenha a env LANG devidamente configurada ex: 

    export LANG=pt_BR.UTF-8

Execução:

    ./hello.py
    ou
    python3 hello.py
"""
__version__ = "0.0.1"
__author__ = "leg1on4rio"
__license__ = "enlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_ES":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"
elif current_language == "de_DE":
    msg = "Hallo, Welt!"

print(msg)
