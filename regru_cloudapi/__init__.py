import json

import requests


class CloudAPI(object):

    def __init__(self, token):
        self.token = token
        self.api_url = 'https://api.cloudvps.reg.ru/v1'
        self.HEADERS = {'Authorization': f'Bearer {self.token}',
                        'Content-Type': 'application/json'}

    def get_tariffs(self):
        data = requests.get(f'{self.api_url}/sizes', headers=self.HEADERS).json()

        return data

    def get_prices(self):
        data = requests.get(f'{self.api_url}/prices', headers=self.HEADERS).json()

        return data

    def get_balance_data(self):
        data = requests.get(f'{self.api_url}/balance_data', headers=self.HEADERS).json()

        return data

    def images(self, param_type):
        params = ['distribution', 'application', 'snapshot', 'backup']
        if param_type in params:
            PARAMS = {'type': param_type}
            data = requests.get('{}/images'.format(self.api_url), headers=self.HEADERS, params=PARAMS).json()

            return data
        else:
            return 'Error: Invalid type'

    def get_ssh_keys(self):
        data = requests.get('{}/account/keys'.format(self.api_url), headers=self.HEADERS).json()

        return data

    def add_ssh_key(self, name, pkey):
        DATA = {'name': name,
                'public_key': pkey}
        data = requests.post('{}/account/keys'.format(self.api_url),
                             headers=self.HEADERS, data=json.dumps(DATA)).json()

        return data

    def rename_ssh_key(self, name, key_id):
        DATA = {'name': name}
        data = requests.put('{}/account/keys/{}'.format(self.api_url, key_id),
                            headers=self.HEADERS, data=json.dumps(DATA)).json()

        return data

    def delete_ssh_key(self, key_id):
        data = requests.delete('{}/account/keys/{}'.format(self.api_url, key_id),
                               headers=self.HEADERS)
        if data.status_code == 204:
            return True
        else:
            return 'Error'

    def ptr(self, url, ip_vps):
        DATA = {'ptr': url}
        data = requests.put('{}/ips/{}'.format(self.api_url, ip_vps),
                            headers=self.HEADERS, data=json.dumps(DATA)).json()

        return data

    def get_reglets(self):
        data = requests.get('{}/reglets'.format(self.api_url), headers=self.HEADERS).json()
        return data

    def create_reglet(self, size, image, name=None, ssh_keys=None, backups=None):
        DATA = {'size': size,
                'image': image}

        if name is not None:
            DATA['name'] = name

        if ssh_keys is not None:
            DATA['ssh_keys'] = ssh_keys

        if backups is not None:
            DATA['backups'] = backups

        data = requests.post('{}/reglets'.format(self.api_url),
                             headers=self.HEADERS, data=json.dumps(DATA)).json()

        return data

    def actions(self, reglet_id, action, size=None, image=None, offline=None, name=None):
        params = ['reboot', 'password_reset', 'start', 'stop', 'enable_backups']
        if action in params:
            DATA = {'type': action}
        elif action == 'resize':
            DATA = {'type': action,
                    'size': size}
        elif action == 'rebuild':
            DATA = {'type': action,
                    'image': image}
        elif action == 'clone' or action == 'snapshot':
            DATA = {'type': action,
                    'offline': offline,
                    'name': name}
        elif action == 'restore':
            DATA = {'type': action,
                    'image': image}

        data = requests.post('{}/reglets/{}/actions'.format(self.api_url, reglet_id),
                             headers=self.HEADERS, data=json.dumps(DATA)).json()

        return data

    def rename_reglet(self, name, reglet_id):
        DATA = {'name': name}
        data = requests.put('{}/reglets/{}'.format(self.api_url, reglet_id),
                            headers=self.HEADERS, data=json.dumps(DATA)).json()

        return data

    def delete_reglet(self, reglet_id):
        data = requests.delete('{}/reglets/{}'.format(self.api_url, reglet_id),
                               headers=self.HEADERS).json()

        if data.status_code == 204:
            return True
        else:
            return 'Error'

    def get_snapshots(self):
        data = requests.get('{}/snapshots'.format(self.api_url), headers=self.HEADERS).json()

        return data

    def create_snapshot(self):
        data = requests.post('{}/snapshots'.format(self.api_url), headers=self.HEADERS).json()

        return data

    def delete_snapshot(self, snap_id):
        data = requests.delete('{}/snapshots/{}'.format(self.api_url, snap_id), headers=self.HEADERS).json()

        if data.status_code == 204:
            return True
        else:
            return 'Error'

    def get_additional_ips(self, reglet_id=None, ip=None):
        if reglet_id is None or ip is None:
            data = requests.get('{}/ips'.format(self.api_url), headers=self.HEADERS).json()
        elif reglet_id is not None and ip is None:
            PARAMS = {'reglet_id': reglet_id}
            data = requests.get('{}/ips'.format(self.api_url), headers=self.HEADERS, params=PARAMS).json()
        elif ip is not None and reglet_id is None:
            data = requests.get('{}/ips/{}'.format(self.api_url, ip), headers=self.HEADERS).json()

        return data

    def add_additional_ips(self, reglet_id, ipv4_count=None, ipv6_count=None):
        DATA = {'reglet_id': reglet_id}
        if ipv4_count is not None or ipv6_count is not None:
            if ipv4_count is not None:
                DATA['ipv4_count'] = ipv4_count
            elif ipv6_count is not None:
                DATA['ipv6_count'] = ipv6_count

            data = requests.put('{}/ips'.format(self.api_url, reglet_id),
                                headers=self.HEADERS, data=json.dumps(DATA)).json()

        return data

    def delete_additional_ips(self, ip):
        data = requests.delete('{}/ips/{}'.format(self.api_url, ip), headers=self.HEADERS).json()

        if data.status_code == 204:
            return True
        else:
            return 'Error'

    def action(self, id):
        data = requests.get('{}/actions/{}'.format(self.api_url, id), headers=self.HEADERS).json()

        return data

    def get_vpcs(self):
        data = requests.get('{}/vpcs'.format(self.api_url), headers=self.HEADERS).json()

        return data

    def get_vpcs_info(self, vpcs_id):
        data = requests.get('{}/vpcs/{}'.format(self.api_url, vpcs_id), headers=self.HEADERS).json()

        return data

    def add_vpcs(self, name):
        DATA = {'name': name}
        data = requests.post('{}/vpcs'.format(self.api_url), headers=self.HEADERS, data=json.dumps(DATA)).json()

        return data

    def rename_vpcs(self, name, vpcs_id):
        DATA = {'name': name}
        data = requests.put('{}/vpcs/{}'.format(self.api_url, vpcs_id),
                            headers=self.HEADERS, data=json.dumps(DATA)).json()

        return data

    def delete_vpcs(self, vpcs_id):
        data = requests.delete('{}/vpcs/{}'.format(self.api_url, vpcs_id), headers=self.HEADERS).json()

        return data

    def get_vpcs_members(self, vpcs_id):
        data = requests.get('{}/vpcs/{}/members'.format(self.api_url, vpcs_id), headers=self.HEADERS).json()

        return data

    def join_vpcs_member(self, reglet_id, vpcs_id):
        DATA = {'resource_id': reglet_id}
        data = requests.post('{}/vpcs/{}/members'.format(self.api_url, vpcs_id),
                             headers=self.HEADERS, data=json.dumps(DATA)).json()

        return data

    def disconnect_vpcs_member(self, vpcs_id, reglet_id):
        data = requests.delete('{}/vpcs/{}/members/{}'.format(self.api_url, vpcs_id, reglet_id),
                               headers=self.HEADERS).json()

        return data
