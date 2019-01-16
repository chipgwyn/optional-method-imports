#!/usr/bin/env python


import yaml
import funcs


data = {}
with open('users.yml') as yf:
    data = yaml.load(yf.read())


def test_result_template(test_name, name):
    return {'name': name, 'test_type': test_name, 'notes': list(),
            'result': 'fail', 'expected': 'pass', 'descr': ''}


class Model(object):
    """docstring for Model"""

    def __init__(self, name=''):
        super(Model, self).__init__()
        self.name = name.strip()
        self.obj_type = self.__class__.__name__
        self.poop = 5
        self.test_results = self.obj_results_template()

    def obj_results_template(self):
        return {self.name: {'name': self.name, 'obj_type': self.obj_type, 'tests': [], 'children': []}}

    def obj_tests(self):
        """ Given an object, this will generate a list of all the functions, limiting to functions that are named starting
        with "test_".
        :param: some object
        :return: list of test functions the object implements
        """
        return [func for func in dir(self) if callable(getattr(self, func)) and func.startswith("test_")]

    def run_tests(self):
        """Runs each test implemented in the object's class and stores the results a list: 'test_results'
        :param: some object
        :return: Nothing
        """
        for test_name in self.obj_tests():
            func = getattr(self, test_name)
            self.test_results[self.name]['tests'].append(func(test_name))


class User(Model,funcs.Users):
    """docstring for User"""

    def __init__(self, name, data):
        super(User, self).__init__()
        self.data = data
        self.name = name
        self.test_results = self.obj_results_template()

    def test_has_full_name(self, test_name):
        result = test_result_template(test_name, self.name)
        result['descr'] = "Full Name"
        try:
            if self.data['full_name'] and len(self.data['full_name']) > 1:
                result['result'] = 'pass'
                return result
            return result
        except:
            return result

users = list()
for user in data['users']:
    if 'public_keys' in data['users'][user]:
        u = User(name=user, data=data['users'][user])
        users.append(u)


print(len(users))

for user in users:
    user.run_tests()
    print(user.test_results)

