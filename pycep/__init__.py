#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
from sys import exit

__version__ = '1.0.5'

class PyCep:
    def __init__(self, cep):
        response = requests.get('http://www.viacep.com.br/ws/%s/json' % cep)
        if response.status_code == 200:
            self.__dadosCep = response.json()

    @property
    def dadosCep(self):
        return self.__dadosCep
