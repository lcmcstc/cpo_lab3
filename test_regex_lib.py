import unittest

from regex_lib import *


class RegexLibTest(unittest.TestCase):

    def test_match(self):
        regex = '[0-9]+'
        text = '13506836172'
        self.assertRaises(TypeError, lambda: match(0, 1))
        self.assertEqual(match(regex, text), (0, len(text)))
        text = 'hello itmo'
        self.assertEqual(match(regex, text), None)
        regex = '^hello'
        self.assertEqual(match(regex, text), (0, 5))
        regex = 'itmo$'
        self.assertEqual(match(regex, text), None)

    def test_search(self):
        regex = '[0-9]+'
        text = 'hello13506836172itmo'
        self.assertRaises(TypeError, lambda: search(0, 1))
        self.assertEqual(search(regex, text), (5, 16))
        text = 'hello itmo'
        self.assertEqual(search(regex, text), None)
        regex = '^hello'
        self.assertEqual(search(regex, text), (0, 5))
        regex = 'itmo$'
        self.assertEqual(search(regex, text), (6, 10))

    def test_sub(self):
        regex = r' #.*$'
        text = '2009-959-559 # this is a phone number'
        self.assertRaises(TypeError, lambda: sub(0, 1, 2))
        self.assertEqual(sub(regex, "", text, 1), '2009-959-559')
        text = '2009-959-559'
        self.assertEqual(sub('-', "", text, 1), '2009959-559')

    def test_split(self):
        regex = r'\w+'
        text = 'lcmc，lx，lcmc，lx，lcmc'
        self.assertRaises(TypeError, lambda: split(0, 1))
        self.assertEqual(split(regex, text), ['', '，', '，', '，', '，', ''])
        self.assertEqual(split(regex, text, 1), ['', '，lx，lcmc，lx，lcmc'])
        regex = r'^lcmc'
        self.assertEqual(split(regex, text), ['', '，lx，lcmc，lx，lcmc'])
        regex = r'lcmc'
        self.assertEqual(split(regex, text, 2), ['', '，lx，', '，lx，lcmc'])
        regex = r'lcmc$'
        self.assertEqual(split(regex, text), ['lcmc，lx，lcmc，lx，', ''])

    def test_time_parsing(self):
        text = 'The system will be updated at 23:58:01 tomorrow'
        regex = '[0-2][0-9]:[0-5][0-9]:[0-5][0-9]'
        d = search(regex, text)
        self.assertEqual(text[d[0]:d[1]], '23:58:01')

    def test_email_parsing(self):
        json_text = r'{"code": 200, "message": "SUCCESS", "email": "lcmc@hdu.edu.cn", "result": { "gender": ' \
                    r'"男","patientId": "20210629-A-0001","svsPic": [{"dziURL": "/0_0.svs.dzi","name": "0.dzi"},{' \
                    r'"dziURL": "/0_1.svs.dzi","name": "1.dzi"}],"minority": "汉族","assistantExaminations": [{' \
                    r'"id": 107,"firstVisitId": 11805506,"time": "2022-05-14","description": "懂法发动","uri": null,' \
                    r'"type": null,"infoType": "assistantExaminations"},'
        regex = r'[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+'
        d = search(regex, json_text)
        self.assertEqual(json_text[d[0]:d[1]], 'lcmc@hdu.edu.cn')


if __name__ == '__main__':
    unittest.main()