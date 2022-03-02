#!/usr/bin/env python3
""" Unittesting for client """

import unittest
from parameterized import parameterized, parameterized_class
import client
from unittest.mock import PropertyMock, patch
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Unittest for githuborclient """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, url, test_mock):
        """ test that GithubOrgClient.org returns the correct value """
        test_mock.return_value = True
        spec = client.GithubOrgClient(url)
        self.assertEqual(spec.org, True)
        test_mock.assert_called_once()

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        """ unit-test GithubOrgClient._public_repos_url """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = client.GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, test_mock):
        """ unit-test GithubOrgClient.public_repos """
        return_value = [{'name': 'google'}, {'name': 'abc'}]
        test_mock.return_value = return_value
        with patch('client.GithubOrgClient._public_repos_url',
                   PropertyMock(return_value=return_value)) as mocked_public:
            response = client.GithubOrgClient('test')
            self.assertEqual(response.public_repos(), ['google', 'abc'])
            test_mock.assert_called_once()
            mocked_public.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expectation):
        """ unit-test GithubOrgClient.has_license """
        result = client.GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expectation)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ test the GithubOrgClient.public_repos method in an integration test """
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_playload, cls.repos_playload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()
