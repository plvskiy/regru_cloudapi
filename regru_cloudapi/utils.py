class Errors(object):
    def __init__(self, data=None, parameter=None, token=None):
        self.data = data
        self.parameter = parameter
        self.token = token

    def check_error(self):
        if 'error' in self.data:
            if self.data['error'] == 'Authorization required':
                raise ValueError('Ключ API неверный. Проверь ключ API в Личном Кабинете Reg.ru услуги Облачные сервера')
        elif 'action' in self.data:
            if self.data['action'] is None:
                raise KeyError('Задание с таким id не найдено')
        elif 'detail' in self.data:
            detail = self.data['detail']

            if 'is too short' in detail and 'ptr' in detail:
                raise ValueError('Предоставленный домен неверен')
            elif 'does not match' in self.data['detail'] and \
                    '^(?:([0-9]{1,3}\\\\.){3}[0-9]{1,3})' in detail:
                raise ValueError('Предоставленный домен неверен')
            elif 'The server encountered an internal error and was unable to complete your request' in detail:
                raise ValueError('Вероятно был использован неверный id')
            else:
                return self.data
        elif 'code' in self.data:
            code = self.data['code']

            if 'IP_NOT_FOUND' in code:
                raise ValueError('Такой IP-адрес не найден')
            elif 'NO_SUCH_REGLET' in code:
                raise ValueError('Такой сервер отсутствует')
            elif 'NO_SUCH_SNAPSHOT' in code:
                raise ValueError('Такой снэпшот отсутствует')
            elif 'NOT_IMPLEMENTED' in code:
                raise ValueError('Такой id отсутствует')
            elif 'VALIDATION_ERROR' in code and 'data' in self.data:
                if 'image' in self.data['data'][0]:
                    raise ValueError('Проверь значение image')
                elif 'size' in self.data['data'][0]:
                    raise ValueError('Проверь значение size')
                elif 'ssh_key_id' in self.data['data'][0]:
                    raise ValueError('Проверь значение ssh_keys')
                elif self.data['data'][0] == 'id':
                    raise KeyError('Сервер с таким id не существует. Проверь id сервера')
                elif self.data['data'][0] == 'name':
                    raise ValueError('Неверное название сервера')
                else:
                    return self.data
            elif 'SSH_KEY_DOES_NOT_EXIST' in code:
                raise KeyError('SSH-ключ с этим id не существует')
            elif 'RESOURCE_LOCKED' in code:
                raise RuntimeError('Реглет заблокирован, так как задание уже выполняется')
            elif 'RESOURCE_NOT_FOUND' in code:
                raise KeyError('Ресурс не был найден. '
                               'Вероятно был указан неверный id ресурса, либо он не существует')
            elif 'ERROR_IP_COUNT' in code:
                raise KeyError('Ошибка в количестве IP-адресов')
            else:
                return self.data
        else:
            return self.data

    def check_images(self):
        params = ['distribution', 'application', 'snapshot', 'backup']
        if self.parameter not in params:
            raise KeyError('Отсутствующее значение. Используй одно из значений: '
                           'distribution, application, snapshot, backup')

    def check_actions(self):
        params = ['reboot', 'password_reset', 'start', 'stop', 'enable_backups', 'disable_backups', 'resize',
                  'rebuild', 'restore', 'clone', 'snapshot']

        if self.parameter not in params:
            raise KeyError('Такой тип операции отсутстсвует. Используй одно из значений: '
                           'reboot, password_reset, start, stop, enable_backups, disable_backups, resize,'
                           'rebuild, restore, clone, snapshot')

    def check_ssh_key(self):
        if 'detail' in self.data:
            if 'does not match' in self.data['detail']:
                if 'name' in self.data['detail']:
                    raise ValueError('Неверное имя ключа')
                elif 'public_key' in self.data['detail']:
                    raise ValueError('Предоставленный SSH-ключ неверен')
        elif 'code' in self.data:
            if self.data['code'] == 'SSH_KEY_ALREADY_EXIST':
                raise ValueError(f'Предоставленный SSH-ключ уже существует: {self.data}')
            elif self.data['code'] == 'SSH_KEY_DOES_NOT_EXIST':
                raise KeyError(f'SSH-ключ с этим id не существует: {self.data}')
        else:
            return Errors(self.data).check_error()
