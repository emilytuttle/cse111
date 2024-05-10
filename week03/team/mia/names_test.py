from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"

pytest.main(["-v", "--tb=line", "-rN", __file__])