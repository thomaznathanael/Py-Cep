# PyCep

[![Python](https://img.shields.io/pypi/pyversions/Eel?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/github/license/thomaznathanael/PyCep?style=for-the-badge)](https://github.com/thomaznathanael/PyCep/blob/main/LICENSE)

[![Alerts](https://img.shields.io/lgtm/alerts/github/thomaznathanael/PyCep?style=for-the-badge&logo=lgtm)](https://lgtm.com/projects/g/thomaznathanael/PyCep/alerts/)
[![Quality](https://img.shields.io/lgtm/grade/python/github/thomaznathanael/PyCep?style=for-the-badge&logo=lgtm)](https://lgtm.com/projects/g/thomaznathanael/PyCep/context:python)

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
>>> data
{'cep': '59104-210', 'logradouro': 'Rua Alvorada', 'complemento': '', 'bairro': 'Igapó', 'localidade': 'Natal', 'uf': 'RN', 'ibge': '2408102', 'gia': '', 'ddd': '84', 'siafi': '1761'}
>>> data['localidade']
'Natal'
>>> data['uf']
'RN'
>>> data.keys()
dict_keys(['cep', 'logradouro', 'complemento', 'bairro', 'localidade', 'uf', 'ibge', 'gia', 'ddd', 'siafi'])
>>> data.values()
dict_values(['59104-210', 'Rua Alvorada', '', 'Igapó', 'Natal', 'RN', '2408102', '', '84', '1761'])
>>>
```

## Licença
-------
[Licença MIT](LICENSE)
