"""
Test cases for common encoders.

Author: Aleksa Zatezalo
Date: January 2025
"""

import pytest
from shellkit.encoders.common import CharEncoder, WhitespaceEncoder, SpecialCharsEncoder


class TestCharEncoder:
    @pytest.fixture
    def encoder(self):
        return CharEncoder()

    def test_html_encoding(self, encoder):
        test_cases = [
            ("<script>", "&lt;script&gt;"),
            ('alert("test")', "alert(&quot;test&quot;)"),
            ("test's", "test&#39;s"),
        ]
        for input_str, expected in test_cases:
            assert encoder.encode(input_str, "html") == expected

    def test_unicode_encoding(self, encoder):
        test_cases = [
            ("A", "\\u0041"),
            ("<>", "\\u003c\\u003e"),
            ("test", "\\u0074\\u0065\\u0073\\u0074"),
        ]
        for input_str, expected in test_cases:
            assert encoder.encode(input_str, "unicode") == expected

    def test_hex_encoding(self, encoder):
        test_cases = [
            ("A", "\\x41"),
            ("<>", "\\x3c\\x3e"),
            ("test", "\\x74\\x65\\x73\\x74"),
        ]
        for input_str, expected in test_cases:
            assert encoder.encode(input_str, "hex") == expected


class TestWhitespaceEncoder:
    @pytest.fixture
    def encoder(self):
        return WhitespaceEncoder()

    def test_comment_encoding(self, encoder):
        input_str = "SELECT * FROM users"
        expected = "SELECT/**/*/**/FROM/**/users"
        assert encoder.encode(input_str, "comment") == expected

    def test_url_encoding(self, encoder):
        input_str = "SELECT * FROM users"
        expected = "SELECT%20*%20FROM%20users"
        assert encoder.encode(input_str, "url") == expected

    def test_decode(self, encoder):
        test_cases = [
            ("SELECT/**/*/**/FROM/**/users", "SELECT * FROM users"),
            ("SELECT%20*%20FROM%20users", "SELECT * FROM users"),
            ("SELECT\n*\nFROM\nusers", "SELECT * FROM users"),
        ]
        for input_str, expected in test_cases:
            assert encoder.decode(input_str) == expected


class TestSpecialCharsEncoder:
    @pytest.fixture
    def encoder(self):
        return SpecialCharsEncoder()

    def test_sql_encoding(self, encoder):
        test_cases = [
            ("O'Reilly", "O''Reilly"),
            ("test;test", "test\;test"),
            ("SELECT--comment", "SELECT\--comment"),
        ]
        for input_str, expected in test_cases:
            assert encoder.encode(input_str, "sql") == expected

    def test_shell_encoding(self, encoder):
        test_cases = [
            ('echo "test"', 'echo "test"'),
            ("ls | grep test", "ls \| grep test"),
            ("cat < file.txt", "cat \< file.txt"),
        ]
        for input_str, expected in test_cases:
            assert encoder.encode(input_str, "shell") == expected

    def test_decode(self, encoder):
        test_cases = [
            ("test\;test", "test;test", "sql"),
            ('echo "test"', 'echo "test"', "shell"),
        ]
        for input_str, expected, char_type in test_cases:
            assert encoder.decode(input_str, char_type) == expected
