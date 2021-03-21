import json
import requests
from regru_cloudapi.utils import Errors


class CloudAPI(object):

    def __init__(self, token=None):
        self.token = token
        self.api_url = 'https://api.cloudvps.reg.ru/v1'
        self.HEADERS = {'Content-Type': 'application/json'}

        if self.token is not None:
            self.HEADERS['Authorization'] = f'Bearer {self.token}'

    def get_tariffs(self):
        data = requests.get(f'{self.api_url}/sizes', headers=self.HEADERS).json()

        return data

    def get_prices(self):
        data = requests.get(f'{self.api_url}/prices', headers=self.HEADERS).json()

        return data

    def get_balance_data(self):
        data = requests.get(f'{self.api_url}/balance_data', headers=self.HEADERS).json()
        check_data = Errors(data).check_error()

        return check_data

    def images(self, param_type):
        Errors(parameter=param_type).check_images()

        params = {'type': param_type}

        data = requests.get(f'{self.api_url}/images', headers=self.HEADERS, params=params).json()
        check_data = Errors(data).check_error()

        return check_data

    def get_ssh_keys(self):
        data = requests.get(f'{self.api_url}/account/keys', headers=self.HEADERS).json()
        check_data = Errors(data).check_error()

        return check_data

    def add_ssh_key(self, name, pkey):
        data_params = {'name': name,
                       'public_key': pkey}

        data = requests.post(f'{self.api_url}/account/keys',
                             headers=self.HEADERS, data=json.dumps(data_params)).json()
        check_data = Errors(data).check_ssh_key()

        return check_data

    def rename_ssh_key(self, name, key_id):
        data_params = {'name': name}

        data = requests.put(f'{self.api_url}/account/keys/{key_id}',
                            headers=self.HEADERS, data=json.dumps(data_params)).json()
        check_data = Errors(data).check_ssh_key()

        return check_data

    def delete_ssh_key(self, key_id):
        data = requests.delete(f'{self.api_url}/account/keys/{key_id}',
                               headers=self.HEADERS)

        if data.status_code != 204:
            check_data = Errors(data.json()).check_ssh_key()

            return check_data
        else:
            return True

    def ptr(self, domain, ip):
        data_params = {'ptr': domain}

        data = requests.put(f'{self.api_url}/ips/{ip}',
                            headers=self.HEADERS, data=json.dumps(data_params)).json()
        check_data = Errors(data).check_error()

        return check_data

    def get_reglets(self):
        data = requests.get(f'{self.api_url}/reglets', headers=self.HEADERS).json()
        check_data = Errors(data).check_error()

        return check_data

    def create_reglet(self, size, image, name=None, ssh_keys=None, backups=None):
        data_params = {'size': size,
                       'image': image}

        if name is not None:
            data_params['name'] = name

        if ssh_keys is not None:
            data_params['ssh_keys'] = ssh_keys

        if backups is not None:
            data_params['backups'] = backups

        data = requests.post(f'{self.api_url}/reglets',
                             headers=self.HEADERS, data=json.dumps(data_params)).json()
        check_data = Errors(data).check_error()

        return check_data

    def actions(self, reglet_id, action, size=None, image=None, offline=None, name=None):
        Errors(parameter=action).check_actions()

        data_params = {'type': action}

        if action == 'resize':
            if size is not None:
                data_params['size'] = size
            else:
                raise ValueError('Значение size не может быть None')
        elif action == 'rebuild' or action == 'restore':
            if image is not None:
                data_params['image'] = image
            else:
                raise ValueError('Значение image не может быть None')
        elif action == 'clone' or action == 'snapshot':
            if offline is not None:
                data_params['offline'] = offline

            if name is not None:
                data_params['name'] = name

        data = requests.post(f'{self.api_url}/reglets/{reglet_id}/actions',
                             headers=self.HEADERS, data=json.dumps(data_params)).json()
        check_data = Errors(data).check_error()

        return check_data

    def rename_reglet(self, reglet_id, name):
        if name is not None:
            data_params = {'name': name}
        else:
            raise ValueError('Переменная name не может быть None')

        data = requests.put(f'{self.api_url}/reglets/{reglet_id}',
                            headers=self.HEADERS, data=json.dumps(data_params)).json()
        check_data = Errors(data).check_error()

        return check_data

    def delete_reglet(self, reglet_id):
        data = requests.delete(f'{self.api_url}/reglets/{reglet_id}',
                               headers=self.HEADERS)

        if data.status_code != 204:
            check_data = Errors(data.json()).check_error()

            return check_data
        else:
            return True

    def get_snapshots(self):
        data = requests.get(f'{self.api_url}/snapshots', headers=self.HEADERS).json()
        check_data = Errors(data).check_error()

        return check_data

    def delete_snapshot(self, snap_id):
        data = requests.delete(f'{self.api_url}/snapshots/{snap_id}', headers=self.HEADERS)

        if data.status_code != 204:
            check_data = Errors(data.json()).check_error()

            return check_data
        else:
            return True

    def get_additional_ips(self, reglet_id=None, ip=None):
        params = {}

        if reglet_id is not None:
            params['reglet_id'] = reglet_id

        if ip is None:
            data = requests.get(f'{self.api_url}/ips', headers=self.HEADERS, params=params).json()
        else:
            data = requests.get(f'{self.api_url}/ips/{ip}', headers=self.HEADERS).json()

        check_data = Errors(data).check_error()

        return check_data

    def add_additional_ips(self, reglet_id, ipv4_count=None, ipv6_count=None):
        data_params = {}

        if ipv4_count is not None:
            data_params['ipv4_count'] = ipv4_count
        elif ipv6_count is not None:
            data_params['ipv6_count'] = ipv6_count

        if data_params is not None:
            data_params['reglet_id'] = reglet_id

            data = requests.post(f'{self.api_url}/ips', headers=self.HEADERS, data=json.dumps(data_params)).json()
            check_data = Errors(data).check_error()

            return check_data
        else:
            raise ValueError('Не указан ни один из параметров - ipv4_count, ipv6_count')

    def delete_additional_ips(self, ip):
        if ip is not None:
            data = requests.delete(f'{self.api_url}/ips/{ip}', headers=self.HEADERS)

            if data.status_code == 204:
                return True
            else:
                check_data = Errors(data.json()).check_error()
                return check_data
        else:
            raise ValueError('Переменная ip не может быть None')

    def get_info_action(self, action_id):
        data = requests.get(f'{self.api_url}/actions/{action_id}', headers=self.HEADERS).json()
        check_data = Errors(data).check_error()

        return check_data

    def get_vpcs(self):
        data = requests.get(f'{self.api_url}/vpcs', headers=self.HEADERS).json()
        check_data = Errors(data).check_error()

        return check_data

    def get_vpcs_info(self, vpcs_id):
        data = requests.get(f'{self.api_url}/vpcs/{vpcs_id}', headers=self.HEADERS).json()
        check_data = Errors(data).check_error()

        return check_data

    def add_vpcs(self, name):
        data_params = {'name': name}

        data = requests.post(f'{self.api_url}/vpcs', headers=self.HEADERS,
                             data=json.dumps(data_params)).json()
        check_data = Errors(data).check_error()

        return check_data

    def rename_vpcs(self, vpcs_id, name):
        data_params = {'name': name}

        data = requests.put(f'{self.api_url}/vpcs/{vpcs_id}',
                            headers=self.HEADERS, data=json.dumps(data_params)).json()
        check_data = Errors(data).check_error()

        return check_data

    def delete_vpcs(self, vpcs_id):
        data = requests.delete(f'{self.api_url}/vpcs/{vpcs_id}', headers=self.HEADERS)

        if data.status_code == 204:
            return True
        else:
            check_data = Errors(data.json()).check_error()
            return check_data

    def get_vpcs_members(self, vpcs_id):
        data = requests.get(f'{self.api_url}/vpcs/{vpcs_id}/members', headers=self.HEADERS).json()
        check_data = Errors(data).check_error()

        return check_data

    def join_vpcs_member(self, reglet_id, vpcs_id):
        data_params = {'resource_id': reglet_id}

        data = requests.post(f'{self.api_url}/vpcs/{vpcs_id}/members',
                             headers=self.HEADERS, data=json.dumps(data_params)).json()
        check_data = Errors(data).check_error()

        return check_data

    def disconnect_vpcs_member(self, reglet_id, vpcs_id):
        data = requests.delete(f'{self.api_url}/vpcs/{vpcs_id}/members/{reglet_id}', headers=self.HEADERS)

        if data.status_code == 204:
            return True
        else:
            check_data = Errors(data.json()).check_error()
            return check_data
