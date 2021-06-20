# Документация 

* [Перед началом](#before_the_start)
* [Проверить статус задания](#get_info_action)
* [Методы без токена](#without_token)
  * [Получить список тарифов](#get_tariffs)
  * [Цены на ресурсы](#get_prices)
* [Текущий баланс и детализация расходов](#get_balance_data)
* [Просмотр списка образов](#images)
* [SSH-ключи](#ssh_keys)
  * [Просмотр списка SSH-ключей](#get_ssh_keys)
  * [Добавление SSH-ключа](#add_ssh_key)
  * [Переименование SSH-ключа](#rename_ssh_key)
  * [Удаление SSH-ключа](#delete_ssh_key)
* [Изменение PTR](#ptr)
* [Виртуальные серверы](#vps)
  * [Просмотр списка серверов и просмотр информации о сервере](#get_reglets)
  * [Создание сервера](#create_reglet)
    * [Создание сервера из снэпшота](#create_reglet_snapshot)
  * [Действия с VPS](#actions)
    * [Перезагрузка сервера](#reboot)
    * [Переименование сервера](#rename_reglet)
    * [Смена тарифа](#resize)
    * [Смена тарифа лицензии ISPmanager](#isp_license)
    * [Сброс root-пароля](#password_reset)
    * [Переустановка системы](#rebuild)
      * [Переустановка сервера из снэпшота](#rebuild_snapshot)
    * [Клонирование сервера](#clone)
    * [Создание снэпшота](#snapshot)
    * [Включение и выключение сервера](#start_stop)
    * [Включение и выключение бекапирования](#enable_disable_backups)
    * [Восстановление из бекапа](#restore)
    * [Удаление сервера](#delete_reglet)
    * [Список удаленных серверов](#get_removed_reglets)
    * [Восстановление удаленного сервера](#restore_removed)
    * [Получить VNC-ссылку](#vnc)
* [Снэпшоты](#snapshots)
  * [Просмотр списка снэпшотов](#get_snapshots)
  * [Создание снэпшота](#snapshot)
  * [Создание сервера из снэпшота](#create_reglet_snapshot)
  * [Переустановка сервера из снэпшота](#rebuild_snapshot)
  * [Удаление снэпшота](#delete_snapshot)
* [Дополнительные IP-адреса](#additional_ip)
  * [Просмотр списка дополнительных IP](#get_additional_ips)
  * [Добавление нового IP-адреса](#add_additional_ips)
  * [Удаление дополнительного IP](#delete_additional_ips)
* [Приватные сети](#private_networks)
  * [Просмотр списка приватных сетей](#get_vpcs)
  * [Получение одной приватной сети](#get_vpcs_info)
  * [Добавление приватной сети](#add_vpcs)
  * [Переименовать приватную сеть](#rename_vpcs)
  * [Удаление приватной сети](#delete_vpcs)
  * [Список ресурсов подключенных к приватной сети](#get_vpcs_members)
  * [Присоединить к приватной сети](#join_vpcs_member)
  * [Отсоединить от приватной сети](#disconnect_vpcs_member)
  
## Перед началом <a name="before_the_start"></a>

> Подробно - https://developers.cloudvps.reg.ru/getting-started/authentication.html

> Токен можно получить в Личном Кабинете -> Услуга Облачные сервера -> 
Настройки -> Токен для API  
> 
Импортируем и авторизуемся:
```python
from regru_cloudapi import CloudAPI
api = CloudAPI(token='token')
```

Далее в Документации будет использоваться переменная api, чтобы обозначить использование в ней токена.

## Проверить статус задания <a name="get_info_action"></a>

> Описание метода - https://developers.cloudvps.reg.ru/getting-started/taskqueue.html

**Аргументы:**
* `action_id` - Идентификатор запроса

**Функция:**
```python
api.get_info_action(action_id=119123)
```

В качестве `action_id` нужно использовать ID задания.  
ID можно найти в ответе практически каждой функции:
```json
{
    "action": {
        "completed_at": "2018-07-12 01:31:44",
        "created_at": "2019-03-04 18:11:01",
        "id": 119123,
        "region_slug": "msk1",
        "resource_id": 6867,
        "resource_type": "reglet",
        "started_at": "2018-07-12 01:31:44",
        "status": "in-progress",
        "type": "reboot"
    }
}
```

## Методы без токена <a name="without_token"></a>

В API Reg.ru есть методы для которых не нужен токен, о них ниже.

* [Получить список тарифов](#get_tariffs)
* [Цены на ресурсы](#get_prices)

---

### Получить список тарифов <a name="get_tariffs"></a>

> Описание метода - https://developers.cloudvps.reg.ru/sizes/index.html

**Функция:**

```python
CloudAPI().get_tariffs()
```

Выше видим, что для CloudAPI не используется токен, так как метод в API не принимает токен:
```shell
curl \
-X GET \
-H "Authorization: Bearer $TOKEN" \
-H "Content-Type: application/json" \
'https://api.cloudvps.reg.ru/v1/sizes'
```

**Ответ:**
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

---

### Цены на ресурсы <a name="get_prices"></a>

> Описание метода - https://developers.cloudvps.reg.ru/billing/prices.html

Собственно еще одна функция, которая не принимает токен.

**Функция:**
```python
CloudAPI().get_prices()
```

**Ответ:**
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

## Текущий баланс и детализация расходов <a name="get_balance_data"></a>

> Описание метода - https://developers.cloudvps.reg.ru/billing/balance.html

**Функция:**
```python
api.get_balance_data()
```

**Ответ:**
```json
{
  "balance_data": {
    "balance": 2154.55,
    "bonus_balance": 41736.72,
    "days_left": 424,
    "detalization": [
      {
        "linked": [
          {
            "plan": "cloud-3",
            "price": "0.26190",
            "price_month": "176.00",
            "resource_id": 123,
            "type": "backup"
          }
        ],
        "name": "Filipino Bird",
        "plan": "cloud-3",
        "price": "1.30952",
        "price_month": "880.00",
        "resource_id": 321,
        "state": "active",
        "type": "reglet"
      }
    ],
    "hourly_cost": 4.31128,
    "hours_left": 10180,
    "monthly_cost": 2896.83,
    "state": "active"
  }
}
```

## Просмотр списка образов <a name="images"></a>

> Описание метода - https://developers.cloudvps.reg.ru/images/list.html

**Аргументы:**
* `param_type` - Тип получаемой информации

**Типы:**
* `distribution` - Шаблоны операционных систем
* `application` - Шаблоны приложений
* `snapshot` - Снэпшоты
* `backup` - Бэкапы

**Функция:**
```python
api.images(param_type='distribution')
```

**Ответ:**
```json
{
    "images": [
        {
            "created_at": "2017-10-31 10:55:48",
            "distribution": "ubuntu-16.04",
            "id": 3459,
            "min_disk_size": "10",
            "name": "Ubuntu 16.04 LTS",
            "private": 0,
            "region_slug":"msk1",
            "size_gigabytes": "2.4",
            "slug": "ubuntu-16-04-amd64",
            "type": "distribution"
        },
        {
            "created_at": "2017-10-31 10:55:48",
            "distribution": "centos-7",
            "id": 3461,
            "min_disk_size": "10",
            "name": "CentOS 7",
            "private": 0,
            "region_slug":"msk1",
            "size_gigabytes": "2.4",
            "slug": "centos-7-amd64",
            "type": "distribution"
        }
    ]
}
```

## SSH-ключи <a name="ssh_keys"></a>

* [Просмотр списка SSH-ключей](#get_ssh_keys)
* [Добавление SSH-ключа](#add_ssh_key)
* [Переименование SSH-ключа](#rename_ssh_key)
* [Удаление SSH-ключа](#delete_ssh_key)

---

### Просмотр списка SSH-ключей <a name="get_ssh_keys"></a>

> Описание метода - https://developers.cloudvps.reg.ru/ssh-keys/list.html

**Функция:**
```python
api.get_ssh_keys()
```

**Ответ:**
```json
{
    "ssh_keys": [
        {
            "fingerprint": "50:8c:26:58:b0:3c:96:24:14:e7:39:cb:2e:d8:5e:cd",
            "id": 597,
            "name": "Deployment key",
            "public_key": "ssh-rsa AAAAB3(...)dQ7Ay9 root@DESKTOP-F24V59S"
        }
    ]
}
```

---

### Добавление SSH-ключа <a name="add_ssh_key"></a>

> Описание метода - https://developers.cloudvps.reg.ru/ssh-keys/add.html

**Аргументы:**
* `name` - Имя ключа
* `pkey (public_key)` - Содержание (тело) ключа

**Функция:**
```python
api.add_ssh_key(name='Deployment key', 
                pkey='ssh-rsa AAAAB3(...)dQ7Ay9 root@DESKTOP-F24V59S')
```

**Ответ:**
```json
{
    "ssh_key": {
        "fingerprint": "50:8c:26:58:b0:3c:96:24:14:e7:39:cb:2e:d8:5e:cd",
        "id": 607,
        "name": "Deployment key",
        "public_key": "ssh-rsa AAAAB3(...)dQ7Ay9 root@DESKTOP-F24V59S"
    }
}
```

---

### Переименование SSH-ключа <a name="rename_ssh_key"></a>

> Описание метода - https://developers.cloudvps.reg.ru/ssh-keys/rename.html

**Аргументы:**
* `name` - Новое имя ключа
* `key_id` - Идентификатор ключа

**Функция:**
```python
api.rename_ssh_key(name='PRIMARY KEY', 
                   key_id='50:8c:26:58:b0:3c:96:24:14:e7:39:cb:2e:d8:5e:cd')
```

**Ответ:**
```json
{
    "ssh_key": {
        "fingerprint": "50:8c:26:58:b0:3c:96:24:14:e7:39:cb:2e:d8:5e:cd",
        "id": 597,
        "name": "PRIMARY KEY",
        "public_key": "ssh-rsa AAAAB3(...)dQ7Ay9 root@DESKTOP-F24V59S"
    }
}
```

---

### Удаление SSH-ключа <a name="delete_ssh_key"></a>

> Описание метода - https://developers.cloudvps.reg.ru/ssh-keys/delete.html

**Аргументы:**
* `key_id` - Идентификатор ключа

**Функция:**
```python
api.delete_ssh_key(key_id='50:8c:26:58:b0:3c:96:24:14:e7:39:cb:2e:d8:5e:cd')
```

**В случае успеха будет возвращено булево значение:**
```python
True
```

## Изменение PTR <a name="ptr"></a>

> Описание метода - https://developers.cloudvps.reg.ru/ptr/index.html

**Аргументы:**
* `domain` - Домен, который нужно прописать в качестве PTR
* `ip` - IP-адрес, для которого нужно указать PTR

**Функция:**
```python
api.ptr(domain='mail.mydomain.ru', 
        ip='193.124.204.254')
```

**Ответ:**
```json
{
    "ip": {
        "ptr": "mail.mydomain.ru"
    }
}
```

## Виртуальные серверы <a name="vps"></a>

* [Просмотр списка серверов и просмотр информации о сервере](#get_reglets)
* [Создание сервера](#create_reglet)
  * [Создание сервера из снэпшота](#create_reglet_snapshot)
* [Действия с VPS](#actions)
  * [Перезагрузка сервера](#reboot)
  * [Переименование сервера](#rename_reglet)
  * [Смена тарифа](#resize)
  * [Смена тарифа лицензии ISPmanager](#isp_license)
  * [Сброс root-пароля](#password_reset)
  * [Переустановка системы](#rebuild)
    * [Переустановка сервера из снэпшота](#rebuild_snapshot)
  * [Клонирование сервера](#clone)
  * [Создание снэпшота](#snapshot)
  * [Включение и выключение сервера](#start_stop)
  * [Включение и выключение бекапирования](#enable_disable_backups)
  * [Восстановление из бекапа](#restore_from_backup)
  * [Удаление сервера](#delete_reglet)
  * [Список удаленных серверов](#get_removed_reglets)
  * [Восстановление удаленного сервера](#restore_removed)
  * [Получить VNC-ссылку](#vnc)
  
---

### Просмотр списка серверов и просмотр информации о сервере<a name="get_reglets"></a>

**Описание методов:**
> Просмотр списка серверов - https://developers.cloudvps.reg.ru/reglets/list.html

> Просмотр информации о сервере - https://developers.cloudvps.reg.ru/reglets/info.html

**Аргументы:**
* `reglet_id` (**_Опциональный_**) - Уникальный идентификатор сервера

**Функция для просмотра списка серверов**:
```python
api.get_reglets()
```

**Ответ:**
```json
{
    "links": {
        "actions": []
    },
    "reglets": [
        {
            "archived_at": null,
            "created_at": "2018-07-12 02:40:27",
            "disk": 10,
            "hostname": "193-124-206-121.cloudvps.regruhosting.ru",
            "id": 6891,
            "image": {
                "created_at": "2017-10-31 10:55:48",
                "distribution": "ubuntu-16.04",
                "id": 3459,
                "min_disk_size": "10",
                "name": "Ubuntu 16.04 LTS",
                "private": 0,
                "region_slug":"msk1",
                "size_gigabytes": "2.4",
                "slug": "ubuntu-16-04-amd64",
                "type": "distribution"
            },
            "image_id": 3459,
            "ip": "193.124.206.121",
            "ipv6": "2a00:f40:2:4:2::1",
            "link_token":null,
            "locked": 0,
            "memory": 512,
            "name": "VNC",
            "ptr":"193-124-206-121.cloudvps.regruhosting.ru",
            "region_slug": "msk1",
            "service_id": 31386957,
            "size": {
                "archived":0,
                "disk": 10,
                "id": 5,
                "memory": 512,
                "name": "Cloud-1",
                "price":"0.00000",
                "price_month":"0.00000",
                "slug": "cloud-1",
                "vcpus": 1,
                "weight": 10
            },
            "size_slug": "cloud-1",
            "status": "active",
            "sub_status": null,
            "vcpus": 1
        }
    ]
}
```

**Функция для просмотра информации о сервере**:
```python
api.get_reglets(reglet_id=6891)
```

**Ответ:**
```json
{
    "reglet": {
        "archived_at": null,
        "created_at": "2018-07-12 02:40:27",
        "disk": 10,
        "disk_usage": 6.7,
        "hostname": "193-124-206-121.cloudvps.regruhosting.ru",
        "id": 6891,
        "image": {
            "created_at": "2017-10-31 10:55:48",
            "distribution": "ubuntu-16.04",
            "id": 3459,
            "min_disk_size": "10",
            "name": "Ubuntu 16.04 LTS",
            "private": 0,
            "region_slug":"msk1",
            "size_gigabytes": "2.4",
            "slug": "ubuntu-16-04-amd64",
            "type": "distribution"
        },
        "image_id": 3459,
        "ip": "193.124.206.121",
        "ipv6": "2a00:f40:2:4:2::1",
        "locked": 0,
        "memory": 512,
        "name": "VNC",
        "ptr":"193-124-206-121.cloudvps.regruhosting.ru",
        "region_slug": "msk1",
        "service_id": 31386957,
        "size": {
            "archived":0,
            "disk": 10,
            "id": 5,
            "memory": 512,
            "name": "Cloud-1",
            "price":"0.00000",
            "price_month":"0.00000",
            "slug": "cloud-1",
            "vcpus": 1,
            "weight": 10
        },
        "size_slug": "cloud-1",
        "status": "active",
        "sub_status": null,
        "vcpus": 1
    }
}
```

---

### Создание сервера <a name="create_reglet"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/add.html

**Аргументы:**
* `size` (**_Обязательный_**) - Уникальный идентификатор тарифа, т.е. `slug` 
  (см. [Тарифы](https://developers.cloudvps.reg.ru/sizes/index.html#sizes))
* `image` (**_Обязательный_**) - Уникальный идентификатор образа, т.е. `slug` 
  (см. [Образы](https://developers.cloudvps.reg.ru/images/index.html#images))
* `name` (**_Опциональный_**) - Имя сервера, может быть автоматически сгенерировано
* `isp_license_size` (**_Опциональный_**) - тариф ISPManager для заказа
* `ssh_keys` (**_Опциональный_**) - Массив с идентификаторами загруженных SSH-ключей
* `backups` (**_Опциональный_**) - Включить бэкапирование `true`
  (см. [Бэкапирование сервера](https://developers.cloudvps.reg.ru/reglets/switch_backups.html#reglets-backups))

**Функция:**
```python
api.create_reglet(size='cloud-1', image='docker-18.03ce', name='Sandbox', 
                  ssh_keys=["50:8c:26:58:b0:3c:96:24:14:e7:39:cb:2e:d8:5e:cd"], 
                  backups='true')
```

**Ответ:**
```json
{
    "links": {
        "actions": [
            {
                "completed_at": "2018-07-12 02:33:09",
                "id": 119153,
                "region_slug": "msk1",
                "resource_id": 6889,
                "resource_type": "reglet",
                "started_at": "2018-07-12 02:33:09",
                "status": "in-progress",
                "type": "create"
            }
        ]
    },
    "reglet": {
        "archived_at": null,
        "created_at": "2018-07-12 02:33:09",
        "disk": 10,
        "hostname": "193-124-206-117.cloudvps.regruhosting.ru",
        "id": 6889,
        "image": {
            "created_at": "2018-04-18 12:51:18",
            "distribution": "ubuntu-16.04",
            "id": 4597,
            "min_disk_size": 5,
            "name": "Docker 18.03.0-ce",
            "private": 0,
            "size_gigabytes": "1.7",
            "slug": "docker-18.03ce",
            "type": "application"
        },
        "image_id": 4597,
        "ip": "193.124.206.117",
        "ipv6": "2a00:f940:2:4:2::1",
        "locked": 1,
        "memory": 512,
        "name": "Sandbox",
        "old_id": null,
        "region_slug": "msk1",
        "resource_id": 6889,
        "service_id": 31386957,
        "backups_enabled": "1",
        "size": {
            "disk": 10,
            "id": 5,
            "memory": 512,
            "name": "Cloud-1",
            "slug": "cloud-1",
            "vcpus": 1,
            "weight": 10
        },
        "size_slug": "cloud-1",
        "status": "new",
        "sub_status": null,
        "type": "reglet",
        "vcpus": 1
    }
}
```

---

#### Создание сервера из снэпшота <a name="create_reglet_snapshot"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/add.html#create-from-snapshot

Создать сервер из снэпшота можно при помощи той же функции - `api.create_reglet()`. 
Единственное различие - в параметре `image` необходимо передать уникальный идентификатор снэпшота.

**Функция:**
```python
api.create_reglet(size='cloud-1', image='6655', name='Sandbox', 
                  ssh_keys=["50:8c:26:58:b0:3c:96:24:14:e7:39:cb:2e:d8:5e:cd"])
```

---

### Действия с VPS <a name="actions"></a>

* [Перезагрузка сервера](#reboot)
* [Переименование сервера](#rename_reglet)
* [Смена тарифа](#resize)
* [Смена тарифа лицензии ISPmanager](#isp_license)
* [Сброс root-пароля](#password_reset)
* [Переустановка системы](#rebuild)
  * [Переустановка сервера из снэпшота](#rebuild_snapshot)
* [Клонирование сервера](#clone)
* [Создание снэпшота](#snapshot)
* [Включение и выключение сервера](#start_stop)
* [Включение и выключение бекапирования](#enable_disable_backups)
* [Восстановление из бекапа](#restore)
* [Удаление сервера](#delete_reglet)
* [Список удаленных серверов](#get_removed_reglets)
* [Восстановление удаленного сервера](#restore_removed)
* [Получить VNC-ссылку](#vnc)

**Обязательные аргументы:**
* `reglet_id` - Идентификатор сервера
* `action` - Тип действия

**Дополнительные аргументы**, зависящие от типа действия:

* `size` (**_Обязательный_** для `resize`) - Читаемое имя тарифа (slug) 
  (см. [Тарифы](https://developers.cloudvps.reg.ru/sizes/index.html#sizes))
* `image` (**_Обязательный_** для `rebuild`) - Уникальный идентификатор образа, т.е. slug 
  (см. [Образы](https://developers.cloudvps.reg.ru/images/index.html#images))
* `offline` - (**_Опциональный_** для `clone`):
  * 1 - Делать консистентный клон диска с остановкой сервера,
  * 0 - Без остановки
* `name`:
  * **_Опциональный_** для `clone` - Имя клона
  * **_Обязательный_** для `snapshot` - Имя снэпшота, не обязано быть уникальным
* `isp_license_size` (**_Обязательный_** для `resize_isp_license`) - тариф ISPmanager

**Типы действий:**
* `reboot` - Перезагрузка сервера
* `password_reset` - Сброс root-пароля
* `start` - Включение сервера
* `stop` - Выключение сервера
* `enable_backups` - Включение бекапирования
* `disable_backups` - Выключение бекапирования
* `resize` - Смена тарифа
* `rebuild` - Переустановка системы
* `restore` - Восстановление из бекапа
* `clone` - Клонирование сервера
* `snapshot` - Создание снэпшота
* `resize_isp_license` - Смена тарифа лицензии ISPmanager

**Функция:**
```python
api.actions(reglet_id, action)
```

---

#### Перезагрузка сервера <a name="reboot"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/reboot.html

**Аргументы:**
* `reglet_id` - Идентификатор сервера
* `action` (`reboot`) - Тип действия

**Функция:**
```python
api.actions(reglet_id=6867, action='reboot')
```

**Ответ:**
```json
{
    "action": {
        "completed_at": "2018-07-12 01:31:44",
        "id": 119123,
        "region_slug": "msk1",
        "resource_id": 6867,
        "resource_type": "reglet",
        "started_at": "2018-07-12 01:31:44",
        "status": "in-progress",
        "type": "reboot"
    }
}
```

---

#### Переименование сервера <a name="rename_reglet"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/rename.html

**Аргументы:**
* `reglet_id` - Идентификатор сервера
* `name` - Новое имя сервера

**Функция:**
```python
api.rename_reglet(reglet_id=6867, name='VNC')
```

**Ответ:**
```json
{
    "reglet": {
        "archived_at": null,
        "created_at": "2018-07-12 02:40:27",
        "disk": 10,
        "hostname": "193-124-206-121.cloudvps.regruhosting.ru",
        "id": 6891,
        "image": {
            "created_at": "2017-10-31 10:55:48",
            "distribution": "ubuntu-16.04",
            "id": 3459,
            "min_disk_size": "10",
            "name": "Ubuntu 16.04 LTS",
            "private": 0,
            "size_gigabytes": "2.4",
            "slug": "ubuntu-16-04-amd64",
            "type": "distribution"
        },
        "image_id": 3459,
        "ip": "193.124.206.121",
        "ipv6": "2a00:f40:2:4:2::1",
        "locked": 0,
        "memory": 512,
        "name": "VNC",
        "old_id": null,
        "region_slug": "msk1",
        "resource_id": 6891,
        "service_id": 31386957,
        "size": {
            "disk": 10,
            "id": 5,
            "memory": 512,
            "name": "Cloud-1",
            "slug": "cloud-1",
            "vcpus": 1,
            "weight": 10
        },
        "size_slug": "cloud-1",
        "status": "active",
        "sub_status": "",
        "type": "reglet",
        "vcpus": 1
    }
}
```

---

#### Смена тарифа <a name="resize"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/resize.html

**Аргументы:**
* `reglet_id` - Идентификатор сервера
* `action` (`resize`) - Тип действия
* `size` - Читаемое имя тарифа (`slug`) - см. [Тарифы](https://developers.cloudvps.reg.ru/sizes/index.html#sizes)

**Функция:**
```python
api.actions(reglet_id=6867, action='resize', size='cloud-4')
```

**Ответ:**
```json
{
    "action": {
        "completed_at": "2018-07-12 01:43:17",
        "id": 119127,
        "region_slug": "msk1",
        "resource_id": 6867,
        "resource_type": "reglet",
        "started_at": "2018-07-12 01:43:16",
        "status": "in-progress",
        "type": "resize"
    }
}
```

---

#### Смена тарифа лицензии ISPmanager <a name="isp_license"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/isp_license.html

**Аргументы:**
* `reglet_id` - Идентификатор сервера
* `action` (`resize_isp_license`) - Тип действия
* `isp_license_size` - тариф ISPmanager

**Функция:**
```python
api.actions(reglet_id=6891, action='resize', isp_license_size='isp_pro6')
```

**Ответ:**
```json
{
    "action": {
        "completed_at": "2018-07-18 00:15:20",
        "id": 121237,
        "region_slug": "msk1",
        "resource_id": 6891,
        "resource_type": "reglet",
        "started_at": "2018-07-18 00:15:19",
        "status": "in-progress",
        "type": "isp_license_size"
    }
}
```

---

#### Сброс root-пароля <a name="password_reset"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/resize.html

**Аргументы:**
* `reglet_id` - Идентификатор сервера
* `action` (`password_reset`) - Тип действия

**Функция:**
```python
api.actions(reglet_id=6891, action='password_reset')
```

**Ответ:**
```json
{
    "action": {
        "completed_at": "2018-07-18 00:07:29",
        "id": 121235,
        "region_slug": "msk1",
        "resource_id": 6891,
        "resource_type": "reglet",
        "started_at": "2018-07-18 00:07:28",
        "status": "in-progress",
        "type": "password_reset"
    }
}
```

---

#### Переустановка системы <a name="rebuild"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/rebuild.html

**Аргументы:**
* `reglet_id` - Идентификатор сервера
* `action` (`rebuild`) - Тип действия
* `image` - Уникальный идентификатор образа, т.е. `slug` 
  (см. [Образы](https://developers.cloudvps.reg.ru/images/index.html#images))

**Функция:**
```python
api.actions(reglet_id=6891, action='rebuild', 
            image='docker-18.03ce')
```

**Ответ:**
```json
{
    "action": {
        "completed_at": "2018-07-18 00:15:20",
        "id": 121237,
        "region_slug": "msk1",
        "resource_id": 6891,
        "resource_type": "reglet",
        "started_at": "2018-07-18 00:15:19",
        "status": "in-progress",
        "type": "rebuild"
    }
}
```

##### Переустановка сервера из снэпшота <a name="rebuild_snapshot"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/rebuild.html#rebuild-from-snapshot

Переустановить сервер из снэпшота можно так же, как это описано в [Переустановка системы](#rebuild). 
Единственное различие - в параметре `image` необходимо передать уникальный идентификатор снэпшота.

**Аргументы:**
* `reglet_id` - Идентификатор сервера
* `action` (`rebuild`) - Тип действия
* `image` - Уникальный идентификатор снэпшота
  
**Функция:**
```python
api.actions(reglet_id=6867, action='rebuild', image=6893)
```

---

#### Клонирование сервера <a name="clone"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/clone.html

**Аргументы:**
* `reglet_id` (_**Обязательный**_) - Идентификатор сервера
* `action` (`clone`) (_**Обязательный**_) - Тип действия
* `offline` (**_Опциональный_**):
  * 1 - Делать консистентный клон диска с остановкой сервера,
  * 0 - Без остановки
* `name` (**_Опциональный_**) - Имя клона

**Функция:**
```python
api.actions(reglet_id=6891, action='clone', offline=1, 
            name='May the 4')
```

**Ответ:**
```json
{
    "action": {
        "completed_at": "2020-04-14 14:06:59",
        "id": 120589,
        "region_slug": "msk1",
        "resource_id": 7047,
        "resource_type": "clone",
        "started_at": "2020-04-14 14:06:59",
        "status": "in-progress",
        "type": "create"
    },
    "reglet_id": "6891"
}
```

---

#### Создание снэпшота <a name="snapshot"></a>

> Описание метода - https://developers.cloudvps.reg.ru/snapshots/add.html

**Аргументы:**
* `reglet_id` (_**Обязательный**_) - Идентификатор сервера
* `action` (`snapshot`) (_**Обязательный**_) - Тип действия
* `offline` (**_Опциональный_**):
  * 1 - Делать консистентный клон диска с остановкой сервера,
  * 0 - Без остановки
* `name` (**_Опциональный_**) - Имя клона

**Функция:**
```python
api.actions(reglet_id=6891, action='snapshot', offline=1, 
            name="snapshot 6891")
```

**Ответ:**
```json
{
    "action": {
        "completed_at": "2018-07-16 14:06:59",
        "id": 120589,
        "region_slug": "msk1",
        "resource_id": 7047,
        "resource_type": "snapshot",
        "started_at": "2018-07-16 14:06:59",
        "status": "in-progress",
        "type": "create"
    },
    "reglet_id": "6891"
}
```

---

#### Включение и выключение сервера <a name="start_stop"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/power_on_off.html

**Аргументы:**
* `reglet_id` - Идентификатор сервера
* `action` - Тип действия:
  * `start` - Запуск сервера
  * `stop` - Остановка сервера

**Функция:**
```python
api.actions(reglet_id=6891, action='start')
```

**Ответ:**
```json
{
    "action": {
        "completed_at": "2018-07-12 01:31:44",
        "id": 119123,
        "region_slug": "msk1",
        "resource_id": 6867,
        "resource_type": "reglet",
        "started_at": "2018-07-12 01:31:44",
        "status": "in-progress",
        "type": "start"
    }
}
```

---

#### Включение и выключение бекапирования <a name="enable_disable_backups"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/switch_backups.html

**Аргументы:**
* `reglet_id` - Идентификатор сервера
* `action` - Тип действия:
  * `enable_backups` - Включает бэкапирование
  * `disable_backups` - Выключает бэкапирование

**Функция:**
```python
api.actions(reglet_id=6867, action='enable_backups')
```

**Ответ:**
```json
{
    "action":{
        "status":"completed"
    },
    "reglet_id":"15751"
}
```

---

#### Восстановление из бекапа <a name="restore_from_backup"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/restore.html

**Аргументы:**
* `reglet_id` - Идентификатор сервера
* `action` (`restore`) - Тип действия
* `image` - Уникальный идентификатор бекапа (id)

**Функция:**
```python
api.actions(reglet_id=6891, action='restore', image=19922)
```

**Ответ:**
```json
{
    "action": {
        "completed_at": "2018-07-18 00:15:20",
        "created_at": "2019-03-04 18:11:01",
        "id": 121237,
        "region_slug": "msk1",
        "resource_id": 6891,
        "resource_type": "reglet",
        "started_at": "2018-07-18 00:15:19",
        "status": "in-progress",
        "type": "restore"
    }
}
```

---

#### Удаление сервера <a name="delete_reglet"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/delete.html

**Аргументы:**
* `reglet_id` - Идентификатор сервера

**Функция:**
```python
api.delete_reglet(reglet_id=6867)
```

В случае успеха будет возвращено **булево значение**:
```python
True
``` 

---

#### Список удаленных серверов <a name="get_removed_reglets"></a>

**Функция:**
```python
api.get_removed_reglets()
```

**Ответ:**
```json
[
  {
    "image_id": 123456, 
    "name": "Cloud Server", 
    "reglet_id": 654321, 
    "remove_date": "2021-05-20 01:58:29", 
    "remove_reason": "stopped by client", 
    "size": {
      "archived": 0, 
      "benchmarks": {
        "geekbench": [
          {
            "score": 0, 
            "version": "4.4.3"
          }, 
          {
            "score": 0, 
            "version": "5.2.3"
          }
        ]
      }, 
      "benchmarks_multiplier": 0, 
      "disk": 5, 
      "id": 1085, 
      "memory": 512, 
      "name": "Start-0", 
      "price": "0.32", 
      "price_month": 215, 
      "regions": ["msk1"], 
      "slug": "start-0", 
      "vcpus": 1, 
      "weight": 1
    }
  }
]
``` 

---

#### Восстановление удаленного сервера <a name="restore_removed"></a>

Восстановление удаленного сервера происходит при помощи той же функции, как и в создании нового сервера - [Создание сервера](#create_reglet).

Но есть отличие - для восстановления сервера нужно указать `size` и `image` удаленного сервера.

В примере ниже возьмем данные из раздела [Список удаленных серверов](#get_removed_reglets).

**Пример:**
```python
api.create_reglet(size='start-0', image=123456)
```

---

#### Получить VNC-ссылку <a name="vnc"></a>

**Функция:**
```python
api.get_vnc_url(reglet_id=654321)
```

**Ответ:**
```json
{
  "vnc": {
    "link": "https://node123-msk1.cloudvps.reg.ru/vnc_auto.html?path=?token=fxr6u1xhdvqlwaxchilsmqqhm4n20ck3"
  }
}
```


## Снэпшоты <a name="snapshots"></a>

* [Просмотр списка снэпшотов](#get_snapshots)
* [Создание снэпшота](#snapshot)
* [Создание сервера из снэпшота](#create_reglet_snapshot)
* [Переустановка сервера из снэпшота](#rebuild_snapshot)
* [Удаление снэпшота](#delete_snapshot)

---

### Просмотр списка снэпшотов <a name="get_snapshots"></a>

> Описание метода - https://developers.cloudvps.reg.ru/snapshots/list.html

**Функция:**
```python
api.get_snapshots()
```

**Ответ:**
```json
{
    "snapshots": [
        {
            "created_at": "2018-07-12 02:42:00",
            "distribution": "ubuntu-16.04",
            "id": 6893,
            "min_disk_size": "10.00",
            "name": "snapshot 1",
            "private": 1,
            "size_gigabytes": "1.05",
            "slug": null,
            "type": "snapshot"
        }
    ]
}
```

---

### [Создание снэпшота](#snapshot)

---

### [Создание сервера из снэпшота](#create_reglet_snapshot)

---

### [Переустановка сервера из снэпшота](#rebuild_snapshot)

---

### Удаление снэпшота <a name="delete_snapshot"></a>

> Описание метода - https://developers.cloudvps.reg.ru/reglets/delete.html

**Аргументы:**
* `snap_id` - Идентификатор снэпшота

**Функция:**
```python
api.delete_snapshot(snap_id=6893)
```

В случае успеха будет возвращено **булево значение**:
```python
True
```

## Дополнительные IP-адреса <a name="additional_ip"></a>

* [Просмотр списка дополнительных IP](#get_additional_ips)
* [Добавление нового IP-адреса](#add_additional_ips)
* [Удаление дополнительного IP](#delete_additional_ips)

---

### Просмотр списка дополнительных IP <a name="get_additional_ips"></a>

> Описание метода - https://developers.cloudvps.reg.ru/add-ip/list.html

**Аргументы:**
* `reglet_id` - Идентификатор сервера
* `ip` - IP-адрес

Для данной функции аргументы необязательны, но в совокупности с аргументами функцию можно использовать по-разному.

#### Если аргументы отсутствуют:

**Функция:**
```python
api.get_additional_ips()
```

**Ответ:**
```json
{
    "ips": [
        {
            "created_at": "2018-07-12 02:42:00",
            "id": 6893,
            "ip": "2a00:f940:2:4:4::e",
            "ptr": "2a00-f940-2-4-4-e.cloudvps.regruhosting.ru",
            "region_slug": "msk1",
            "reglet_id": "3319",
            "status": "active",
            "type": "ipv6"
        }
    ]
}
```

---

#### Если передается `reglet_id`:

**Функция:**
```python
api.get_additional_ips(reglet_id=3319)
```

---

#### Если передается `ip`:

**Функция:**
```python
api.get_additional_ips(ip='2a00:f940:2:4:4::e')
```

---

### Добавление нового IP-адреса <a name="add_additional_ips"></a>

> Описание метода - https://developers.cloudvps.reg.ru/add-ip/add.html

**Аргументы:**
* `reglet_id` (_**Обязательный**_) - ID сервера к которому привяжется IP
* `ipv4_count` (_**Зависимый**_) - Количество IP адресов типа ipv4
* `ipv6_count` (_**Зависимый**_) - Количество IP адресов типа ipv6

> Из двух аргументов ipv4_count и ipv6_count хотя бы один должен быть обязательно указан!

**Функция:**
```python
api.add_additional_ips(reglet_id=3319, ipv4_count=3)
```

**Ответ:**
```json
{
    "ips": {
        "ipv4_count": 3
    },
    "links": {
        "actions": []
    }
}
```

---

### Удаление дополнительного IP <a name="delete_additional_ips"></a>

> Описание метода - https://developers.cloudvps.reg.ru/add-ip/delete.html

**Аргументы:**
* `ip` - IP-адрес

**Функция:**
```python
api.delete_additional_ips(ip='193.124.204.254')
```

В случае успеха будет возвращено **булево значение**:
```python
True
```

## Приватные сети <a name="private_networks"></a>

* [Просмотр списка приватных сетей](#get_vpcs)
* [Получение одной приватной сети](#get_vpcs_info)
* [Добавление приватной сети](#add_vpcs)
* [Переименовать приватную сеть](#rename_vpcs)
* [Удаление приватной сети](#delete_vpcs)
* [Список ресурсов подключенных к приватной сети](#get_vpcs_members)
* [Присоединить к приватной сети](#join_vpcs_member)
* [Отсоединить от приватной сети](#disconnect_vpcs_member)

---

### Просмотр списка приватных сетей <a name="get_vpcs"></a>

> Описание метода - https://developers.cloudvps.reg.ru/vpcs/list.html

**Функция:**
```python
api.get_vpcs()
```

**Ответ:**
```json
[
  {
    "resource_id": "123",
    "name": "My private network",
    "region_slug": "msk1",
    "members": [
      1111, 1112, 1113
    ]
  }
]
```

---

### Получение одной приватной сети <a name="get_vpcs_info"></a>

> Описание метода - https://developers.cloudvps.reg.ru/vpcs/single.html

**Аргументы:**
* `vpcs_id` - Идентификатор ресурса сети

**Функция:**
```python
api.get_vpcs_info(vpcs_id=123)
```

**Ответ:**
```json
[
  {
    "resource_id": "123",
    "name": "My private network",
    "region_slug": "msk1",
    "members": [
      1111, 1112, 1113
    ]
  }
]
```

---

### Добавление приватной сети <a name="add_vpcs"></a>

> Описание метода - https://developers.cloudvps.reg.ru/vpcs/add.html

**Аргументы:**
* `name` - Имя сети

**Функция:**
```python
api.add_vpcs(name='Приватная сеть № 1')
```

**Ответ:**
```json
{
  "members": [],
  "name": "Приватная сеть № 1",
  "region_slug": "msk1",
  "resource_id": "123"
}
```

---

### Переименовать приватную сеть <a name="rename_vpcs"></a>

> Описание метода - https://developers.cloudvps.reg.ru/vpcs/rename.html

**Аргументы:**
* `vpcs_id` - Идентификатор ресурса сети
* `name` - Новое имя приватной сети

**Функция:**
```python
api.rename_vpcs(vpcs_id=123, name='My new name private net')
```

**Ответ:**
```json
{
    "resource_id": "123",
    "name": "My new name private net",
    "region_slug": "msk1",
    "members": [
      1111, 1112, 1113
    ]
}
```

---

### Удаление приватной сети <a name="delete_vpcs"></a>

> Описание метода - https://developers.cloudvps.reg.ru/vpcs/delete.html

**Аргументы:**
* `vpcs_id` - Идентификатор ресурса сети

**Функция:**
```python
api.delete_vpcs(vpcs_id=123)
```

В случае успеха будет возвращено **булево значение**:
```python
True
```

---

### Список ресурсов подключенных к приватной сети <a name="get_vpcs_members"></a>

> Описание метода - https://developers.cloudvps.reg.ru/vpcs/members.html

**Аргументы:**
* `vpcs_id` - Идентификатор ресурса сети

**Функция:**
```python
api.get_vpcs_members(vpcs_id=123)
```

**Ответ:**
```json
 "members": [
      1111, 1112
]
```

---

### Присоединить к приватной сети <a name="join_vpcs_member"></a>

> Описание метода - https://developers.cloudvps.reg.ru/vpcs/attach.html

**Аргументы:**
* `reglet_id` - Идентификатор сервера
* `vpcs_id` - Идентификатор ресурса сети

**Функция:**
```python
api.join_vpcs_member(reglet_id=123456, vpcs_id=123)
```

**Ответ:**
```json
{
  "action_id": 111301
}
```

---

### Отсоединить от приватной сети <a name="disconnect_vpcs_member"></a>

> Описание метода - https://developers.cloudvps.reg.ru/vpcs/detach.html

**Аргументы:**
* `reglet_id` - Идентификатор сервера
* `vpcs_id` - Идентификатор ресурса сети

**Функция:**
```python
api.disconnect_vpcs_member(reglet_id=123456, vpcs_id=123)
```

В случае успеха будет возвращено **булево значение**:
```python
True
```