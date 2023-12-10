import pytest_eldar.converter.main as converter
import pytest
import os

@pytest.fixture
def mock_curr_data():
    fake_data = {
        "RUB": 1,
        "USD": 0.01091224,
        "EUR": 0.010117269,
    }
    yield fake_data


@pytest.fixture
def get_data_from_api():
    data = converter.get_currencies_from_api()
    yield data
    os.remove("currencies.txt")



@pytest.fixture
def currencies_export():
    # I'll fix this
    rates = {
        "AUD": 0.0164887,
        "AZN": 0.0185508,
        "GBP": 0.008678416,
        "AMD": 4.400246,
        "BYN": 0.0349792,
        "BGN": 0.019814457,
        "BRL": 0.053411,
        "HUF": 3.8739569,
        "VND": 261.35932987,
        "HKD": 0.085104,
        "GEL": 0.029233868,
        "DKK": 0.075529,
        "AED": 0.04007518,
        "USD": 0.01091224,
        "EUR": 0.010117269,
        "EGP": 0.337113,
        "INR": 0.90964496557,
        "IDR": 169.5326155,
        "KZT": 5.018644,
        "CAD": 0.0148373676,
        "QAR": 0.0397205,
        "KGS": 0.97467786896,
        "CNY": 0.07819,
        "MDL": 0.19348497,
        "NZD": 0.01769169,
        "NOK": 0.1190765,
        "PLN": 0.04384657,
        "RON": 0.0502606,
        "XDR": 0.00821278,
        "SGD": 0.0145842,
        "TJS": 0.1196374,

    }

    return rates
