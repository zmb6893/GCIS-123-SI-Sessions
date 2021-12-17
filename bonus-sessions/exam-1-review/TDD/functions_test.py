'''
Sample code for TDD activity
@author: Zoe Bingham
'''

import functions

# What will happen when we run pytest?
def test_hello_AJ():
    # Setup
    expected = "Hello, AJ"
    name = "AJ"

    # Invoke
    result = functions.hello(name)

    # Analyze
    assert result == expected

def test_hello_Jaden():
    # Setup
    expected = "Hello, Jaden"
    name = "Jaden"

    # Invoke
    result = functions.hello(name)

    # Analyze
    assert result == expected

def test_hello_Robert():
    # Setup
    expected = "Hello, Robert"
    name = "Robert"

    # Invoke
    result = functions.hello(name)

    # Analyze
    assert result == expected

def test_hello_John():
    # Setup
    expected = "Hello, John"
    name = "John"

    # Invoke
    result = functions.hello(name)

    # Analyze
    assert result == expected

def test_hello_Christian():
    # Setup
    expected = "Hello, Christian"
    name = "Christian"

    # Invoke
    result = functions.hello(name)

    # Analyze
    assert result == expected

def test_hello_Juan():
    # Setup
    expected = "Hello, Juan"
    name = "Juan"

    # Invoke
    result = functions.hello(name)

    # Analyze
    assert result == expected