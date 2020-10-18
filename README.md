# Py-Cep

[![PyPI version](https://img.shields.io/pypi/v/Py-Cep?style=for-the-badge)](https://pypi.org/project/Py-Cep/)
[![Python](https://img.shields.io/pypi/pyversions/Py-Cep?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/github/license/thomaznathanael/Py-Cep?style=for-the-badge)](https://github.com/thomaznathanael/Py-Cep/blob/main/LICENSE)

[![Alerts](https://img.shields.io/lgtm/alerts/github/thomaznathanael/Py-Cep?style=for-the-badge&logo=lgtm)](https://lgtm.com/projects/g/thomaznathanael/Py-Cep/alerts/)
[![Quality](https://img.shields.io/lgtm/grade/python/github/thomaznathanael/Py-Cep?style=for-the-badge&logo=lgtm)](https://lgtm.com/projects/g/thomaznathanael/Py-Cep/context:python)

Obtem informações de CEPs do Brasil

## Pré requisitos

  * Instalação de qualquer versão do Python (http://www.python.org/download)
  
## Instalação das dependências

```bash
$ pip install -r requirements.txt
```

## Utilização

```bash
>>> from pycep import PyCep
>>> cep1 = PyCep('59104210')
>>> cep1.dadosCep
{'cep': '59104-210', 'logradouro': 'Rua Alvorada', 'complemento': '', 'bairro': 'Igapó', 'localidade': 'Natal', 'uf': 'RN', 'ibge': '2408102', 'gia': '', 'ddd': '84', 'siafi': '1761'}
>>> cep1.dadosCep['localidade']
'Natal'
>>> cep1.dadosCep['uf']
'RN'
>>> cep1.dadosCep.keys()
dict_keys(['cep', 'logradouro', 'complemento', 'bairro', 'localidade', 'uf', 'ibge', 'gia', 'ddd', 'siafi'])
>>> cep1.dadosCep.values()
dict_values(['59104-210', 'Rua Alvorada', '', 'Igapó', 'Natal', 'RN', '2408102', '', '84', '1761'])
>>>
```

## Licença
-------
[Licença MIT](LICENSE)
