def test_result_template(test_name, name):
    return {'name': name, 'test_type': test_name, 'notes': list(),
            'result': 'fail', 'expected': 'pass', 'descr': ''}

class Users:
    def test_has_public_keys(self, test_name):
        result = test_result_template(test_name, self.name)
        result['descr'] = "Pub Keys"
        if 'public_keys' in self.data:
            if isinstance(self.data['public_keys'], list):
                if len(self.data['public_keys']) > 0:
                    result['result'] = 'pass'
                    return result
        return result
