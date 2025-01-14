"""
Test cases for HTTP encoder.

Author: Aleksa Zatezalo
Date: January 2025
"""

import pytest
from shellkit.encoders.http import HTTPEncoder

class TestHTTPEncoder:
    @pytest.fixture
    def encoder(self):
        return HTTPEncoder()

    def test_url_encoding(self, encoder):
        test_cases = [
            ('hello world', 'hello%20world'),
            ('test?param=value', 'test%3Fparam%3Dvalue'),
            ('user@example.com', 'user%40example.com')
        ]
        for input_str, expected in test_cases:
            assert encoder.encode(input_str, 'url') == expected

    def test_double_encoding(self, encoder):
        test_cases = [
            ('hello world', 'hello%2520world'),
            ('<script>', '%253Cscript%253E')
        ]
        for input_str, expected in test_cases:
            assert encoder.encode(input_str, 'double') == expected

    def test_form_encoding(self, encoder):
        test_cases = [
            ('hello world', 'hello+world'),
            ('test param', 'test+param')
        ]
        for input_str, expected in test_cases:
            assert encoder.encode(input_str, 'form') == expected

    def test_decode(self, encoder):
        test_cases = [
            ('hello%20world', 'hello world', 'url'),
            ('hello%2520world', 'hello world', 'double'),
            ('hello+world', 'hello world', 'form')
        ]
        for input_str, expected, encoding_type in test_cases:
            assert encoder.decode(input_str, encoding_type) == expected

    def test_encode_params(self, encoder):
        params = {
            'name': 'test user',
            'id': '123',
            'query': 'select * from users'
        }
        encoded = encoder.encode_params(params)
        assert 'name=test+user' in encoded
        assert 'id=123' in encoded
        assert 'query=select+%2A+from+users' in encoded

    def test_encode_headers(self, encoder):
        headers = {
            'User-Agent': 'test browser',
            'X-Custom-Header': 'test value'
        }
        encoded = encoder.encode_headers(headers)
        assert encoded['User-Agent'] == 'test%20browser'
        assert encoded['X-Custom-Header'] == 'test%20value'

    def test_encode_path(self, encoder):
        test_cases = [
            ('/path/to/file', '/path/to/file'),
            ('/path with spaces/', '/path%20with%20spaces/'),
            ('/test?param=value', '/test%3Fparam%3Dvalue')
        ]
        for input_str, expected in test_cases:
            assert encoder.encode_path(input_str) == expected

    def test_normalize_path(self, encoder):
        test_cases = [
            ('//path//to//file', '/path/to/file'),
            ('/path/ /to/file', '/path/%20/to/file'),
            ('//test//param?value', '/test/param%3Fvalue')
        ]
        for input_str, expected in test_cases:
            assert encoder.normalize_path(input_str) == expected

    def test_invalid_encoding_type(self, encoder):
        with pytest.raises(ValueError):
            encoder.encode("test", "invalid_type")
        with pytest.raises(ValueError):
            encoder.decode("test", "invalid_type")