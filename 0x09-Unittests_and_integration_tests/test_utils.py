#!/usr/bin/env python3
""" Unisttesting for utils """

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """ class to test nested map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, map):
        """ test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), map)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test that a KeyError is raised """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ class to test get__json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_playload):
        """ Test get json function """
        test_mock = unittest.mock.Mock()
        test_mock.json.return_value = test_playload
        with patch('request.get', return_value=test_mock):
            test_json = get_json(test_url)
            test_mock.json.assert_called_once()
            self.assertEqual(test_json, test_playload)


class TestMemoize(unittest.TestCase):
    """ class to test for memoize """

    def test_memoize(self):
        """ Test memoize """
        class TestClass:
            """ Class to test """

            def a_method(self):
                """ method that returns 42 """
                return 42

            @memoize
            def a_property(self):
                """ method that returns a_method """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as test_mock:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            test_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
