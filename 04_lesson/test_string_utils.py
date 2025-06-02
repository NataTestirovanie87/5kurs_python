# начинаем тестирование string_utils
import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("Skypro", "Skypro"),
        ("s", "S"),
        ("hello friend", "Hello friend")
    ])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative1(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str",
    [
        (None)
    ])
def test_capitalize_negative2(input_str):
    with pytest.raises(AttributeError):
        string_utils.capitalize(input_str)


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        ("skypro", "skypro"),
        ("   ", ""),
        ("", "")
    ])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("sky pro", "sky pro"),
        ("skypro   ", "skypro   ")
    ])
def test_trim_negative1(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str",
    [
        (None)
    ])
def test_trim_negative2(input_str):
    with pytest.raises(AttributeError):
        string_utils.trim(input_str)


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, input_symbol, expected",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "k", True),
        ("SkyPro!", "!", True),
        ("SkyPro", "o", True),
        ("SkyPro", "P", True),
        ("Mississippi", "s", True)
    ])
def test_contains_positive(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, input_symbol",
    [
        ("SkyPro", None),  # ожидать TypeError
        ("SkyPro", 5)  # ожидать TypeError
    ])
def test_contains_negative1(input_str, input_symbol):
    with pytest.raises(TypeError):
        string_utils.contains(input_str, input_symbol)


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, input_symbol",
    [
        (None, "o")  # ожидать AttributeError
    ])
def test_contains_negative2(input_str, input_symbol):
    with pytest.raises(AttributeError):
        string_utils.contains(input_str, input_symbol)


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, input_symbol, expected",
    [
        ("SkyPro", "Pro", "Sky"),
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "U", "SkyPro"),
        ("Natalia", "a", "Ntli"),
        ("SkyPro", "5", "SkyPro")
    ])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, input_symbol",
    [
        (None, "k"),  # ожидать AttributeError
        (12345, "a")  # ожидать AttributeError
    ])
def test_delete_symbol_negative1(input_str, input_symbol):
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(input_str, input_symbol)


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, input_symbol",
    [
        ("test", None)  # ожидать TypeError
    ])
def test_delete_symbol_negative2(input_str, input_symbol):
    with pytest.raises(TypeError):
        string_utils.delete_symbol(input_str, input_symbol)
