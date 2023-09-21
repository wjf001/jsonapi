import json
import pytest
from src.jsonapi.jsonapi import MyEncoder, MyDecoder

def test_custom_json_encoding():
    custom_data = {
        "complex_number": (2 + 3j),
        "range_object": range(1, 10, 2),
    }
    expected_json = (
        '{"complex_number": {"real": 2.0, "imag": 3.0}, '
        '"range_object": {"start": 1, "stop": 10, "step": 2}}'
    )
    encoded_json = json.dumps(custom_data, cls=MyEncoder)
    assert encoded_json == expected_json

def test_custom_json_decoding():
    encoded_json = (
        '{"complex_number": {"real": 2.0, "imag": 3.0}, '
        '"range_object": {"start": 1, "stop": 10, "step": 2}}'
    )
    expected_data = {
        "complex_number": (2 + 3j),
        "range_object": range(1, 10, 2),
    }
    decoded_data = json.loads(encoded_json, cls=MyDecoder)
    assert decoded_data == expected_data
