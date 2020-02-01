#!/usr/bin/env python3
from object_colors import Color


def test_color_string(str_, color_str) -> None:
    assert color_str == f"\u001b[0;32;40m{str_}\u001b[0;0m"


def test__getattr__():
    color = Color()
    hasattr(color, "__self__") and color.__self__ is color.get


def test__dir__(color, capsys):
    instances = color.__dir__()
    assert instances == [
        "text",
        "effect",
        "background",
        "bold",
        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "purple",
        "cyan",
        "white",
    ]


def test_pop_result(color):
    assert hasattr(color, "red")
    red = color.pop("red")
    assert "red" not in color.__dict__
    red_string = red.get("This is red")
    assert red_string == f"\u001b[0;31;40mThis is red\u001b[0;0m"


def test_pop_no_result():
    color = Color()
    assert "red" not in color.__dict__
    red = color.pop("red")
    assert red is None


def test_str_args():
    color = Color("red", "bold")
    assert color.text == 1
    assert color.effect == 1


def test_str_ints():
    color = Color(1, 1)
    assert color.text == 1
    assert color.effect == 1


def test_tuple_return(color):
    tup = color.red.get("t", "u", "p")
    assert tup == (
        "\u001b[0;31;40mt\u001b[0;0m",
        "\u001b[0;31;40mu\u001b[0;0m",
        "\u001b[0;31;40mp\u001b[0;0m",
    )


def test_color_print(color, capsys):
    color.red.print("This stdout is red")
    captured = capsys.readouterr()
    assert captured.out == "\u001b[0;31;40mThis stdout is red\u001b[0;0m\n"


def test_int_dict():
    color = Color(orange=1)
    assert color.text == 7


def test_rainbow(color, str_, capsys):
    rb = color.multicolor(str_)
    print(rb)