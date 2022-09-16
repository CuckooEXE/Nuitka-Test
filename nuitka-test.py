"""
Nuitka Test - Test Nuitka with using various packages from Python to show functionality
"""


"""
Imported Libraries

unittest - Unit Test the code
requests - HTTP(S) functionality
ctypes - Load a shared-object and call functions from it
os - Get environment variable
"""
import unittest
import requests
import ctypes
import os


class Nuitka_Test(unittest.TestCase):

    def setUp(self) -> None:
        if not os.getenv("test_library"):
            raise ValueError("test_library environment variable must be set!")
        self.test_library = ctypes.cdll.LoadLibrary(os.getenv("test_library"))


    def test_library_add(self):
        a = ctypes.c_int(4)
        b = ctypes.c_int(2)
        self.assertEqual(self.test_library.add(a, b), a.value + b.value)
    

    def test_library_dump(self):
        s = ctypes.create_string_buffer(13)
        self.assertEqual(self.test_library.dump((ctypes.c_char_p)(ctypes.addressof(s))), 13)
        self.assertEqual(s.raw.decode()[:13], "Hello, world!")

    
    def test_requests(self):
        r = requests.get('https://httpbin.org/get?test=abc')
        r.raise_for_status()
        self.assertTrue('"args": {\n    "test": "abc"\n  },' in r.text)


if __name__ == '__main__':
    unittest.main()