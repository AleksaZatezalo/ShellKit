import pytest
from shellkit.encoders.shell import CommandEncoder, PowerShellEncoder, BashEncoder

class TestCommandEncoder:
    @pytest.fixture
    def encoder(self):
        return CommandEncoder()

    def test_basic_encoding(self, encoder):
        command = "dir & type file.txt"
        expected = "dir ^& type file.txt"
        assert encoder.encode(command) == expected

    def test_special_chars(self, encoder):
        test_cases = [
            ("dir > output.txt", "dir ^> output.txt"),
            ("type file.txt | findstr test", "type file.txt ^| findstr test"),
            ("echo test && dir", "echo test ^&^& dir")
        ]
        for input_cmd, expected in test_cases:
            assert encoder.encode(input_cmd) == expected

    def test_decode(self, encoder):
        encoded = "dir ^> output.txt"
        expected = "dir > output.txt"
        assert encoder.decode(encoded) == expected

class TestPowerShellEncoder:
    @pytest.fixture
    def encoder(self):
        return PowerShellEncoder()

    def test_escape_encoding(self, encoder):
        test_cases = [
            ('Get-Process | Select-Object Name',
             'Get-Process `| Select-Object Name'),
            ('$var = "test"',
             '`$var = `"test`"'),
            ('Get-Content "file.txt"',
             'Get-Content `"file.txt`"')
        ]
        for input_cmd, expected in test_cases:
            assert encoder.encode(input_cmd, 'escape') == expected

    def test_base64_encoding(self, encoder):
        command = "Get-Process"
        encoded = encoder.encode(command, 'base64')
        assert encoded.startswith("powershell -enc ")
        assert encoder.decode(encoded, 'base64') == command

    def test_encode_decode_cycle(self, encoder):
        original = 'Get-Process | Where-Object {$_.CPU -gt 50}'
        encoded = encoder.encode(original, 'escape')
        decoded = encoder.decode(encoded, 'escape')
        assert decoded == original

class TestBashEncoder:
    @pytest.fixture
    def encoder(self):
        return BashEncoder()

    def test_escape_encoding(self, encoder):
        test_cases = [
            ('cat file.txt | grep pattern',
             'cat\\ file.txt\\ \\|\\ grep\\ pattern'),
            ('echo "hello world"',
             'echo\\ \\"hello\\ world\\"'),
            ('ls -la > output.txt',
             'ls\\ -la\\ \\>\\ output.txt')
        ]
        for input_cmd, expected in test_cases:
            assert encoder.encode(input_cmd, 'escape') == expected

    def test_base64_encoding(self, encoder):
        command = "cat /etc/passwd"
        encoded = encoder.encode(command, 'base64')
        assert encoded.startswith("echo ")
        assert encoded.endswith(" | base64 -d | bash")
        assert encoder.decode(encoded, 'base64') == command

    def test_hex_encoding(self, encoder):
        command = "cat /etc/passwd"
        encoded = encoder.encode(command, 'hex')
        assert encoded.startswith("echo ")
        assert encoded.endswith(" | xxd -p -r | bash")
        assert encoder.decode(encoded, 'hex') == command

    def test_special_chars(self, encoder):
        test_cases = [
            ('echo $HOME', 'echo\\ \\$HOME'),
            ('rm -rf *', 'rm\\ -rf\\ \\*'),
            ('grep "test" file.txt', 'grep\\ \\"test\\"\\ file.txt')
        ]
        for input_cmd, expected in test_cases:
            assert encoder.encode(input_cmd, 'escape') == expected

    def test_invalid_method(self, encoder):
        with pytest.raises(ValueError):
            encoder.encode("test", "invalid_method")