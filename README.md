# Nuitka Testing
[![Test Code](https://github.com/CuckooEXE/Nuitka-Test/actions/workflows/code-test.yml/badge.svg)](https://github.com/CuckooEXE/Nuitka-Test/actions/workflows/code-test.yml)
This is just a tiny repo to demonstrate how to compile a Python program to a statically-compiled C program that is capable of running on a system with no Python interpreter/libraries.

## Building
To build, just build the Docker container:
```bash
sudo docker build --tag nuitka-test .
```

## Running
The test script uses HTTP(S) functionality (via `requests`) and calls a shared-object (via `ctypes`), you can run it with python via:
```bash
test_library=$PWD/test_library.so python3 nuitka-test.py
```

Or the compiled version via:
```bash
test_library=$PWD/test_library.so ./nuitka-test.bin
```