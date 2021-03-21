# <p align="center"> REG.RU CloudAPI

![PyPI](https://img.shields.io/pypi/v/regru_cloudapi?style=plastic)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/regru_cloudapi)
![PyPI - License](https://img.shields.io/pypi/l/regru_cloudapi)


<p align="center"> Неофициальная библиотека для работы с API услуги <a href="https://reg.ru">Reg.ru</a> Облачные VPS.
<p align="center">Документация по API Reg.ru Облачные VPS - <a href="https://developers.cloudvps.reg.ru">developers.cloudvps.reg.ru</a>
    
* [Приступая к работе](#getting_started)
    * [Установка при помощи PyPi](#pypi)
    * [Установка вручную](#manually)
    * [Зависимости](#dependencies)
* [Быстрый старт](#quick_start)
* [Документация](DOCUMENTATION.md)
* [Лицензия](LICENSE)


## Приступая к работе <a name="getting_started"></a>

### Установка при помощи PyPi: <a name="pypi"></a>

```shell
pip3 install regru_cloudapi
```

### Установка вручную: <a name="manually"></a>

```shell
git clone https://github.com/plvskiy/regru_cloudapi.git
cd regru_cloudapi
python setup.py install
```

### Зависимости: <a name="dependencies"></a>

```
setuptools
requests
```

## Быстрый старт <a name="quick_start"></a>

Сперва импортируем модуль 

```python
from regru_cloudapi import CloudAPI
```

Далее авторизуемся:

```python
api = CloudAPI('token')
```

> Токен можно получить в Личном Кабинете -> Услуга Облачные сервера -> 
Настройки -> Токен для API
> 
> Подробно - https://developers.cloudvps.reg.ru/getting-started/authentication.html.

Следующим шагом используем нужные нам функции. Например, запросим список тарифов:

```python
api.get_tariffs()
```

На выходе мы получим список тарифов в JSON. Пример:

```json
{
  "prices": [
    {
      "plan": "cloud-1-1018",
      "price": "0.32",
      "price_month": 215,
      "type": "reglet",
      "unit": "hour"
    }
  ]
}
```

Полный код:

```python
from regru_cloudapi import CloudAPI

api = CloudAPI('token')

api.get_tariffs()
```

## Документация - [DOCUMENTATION.md](DOCUMENTATION.md)

## Лицензия - [LICENSE](LICENSE)