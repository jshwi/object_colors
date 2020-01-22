#!/usr/bin/env python3
from object_colors import Color


class TestIgnoreCaseAndScatterColor:
    def test_exact_letter_in_string_color(
        self,
        all_colors: Color,
        small_color_test_string,
        all_cs_marked_color: str,
    ) -> None:
        colored_keys = all_colors.red.get_key(
            small_color_test_string, "c", case=True, any_=True
        )
        assert colored_keys == (
            "\u001b[0;32;40m\u001b[0;31;40mC\u001b[0;32;40m\u001b[0;31;40mc"
            "\u001b[0;32;40m: My Business <me@mybusiness.\u001b[0;31;40mc"
            "\u001b[0;32;40mom>;\u001b[0;0m"
        )

    def test_exact_word_in_string_color(
        self,
        all_colors: Color,
        small_color_test_string,
        marked_word: str,
        all_cs_marked_color: str,
    ) -> None:
        colored_keys = all_colors.red.get_key(
            small_color_test_string, "Cc:", case=True, any_=True
        )
        assert colored_keys == all_cs_marked_color

    def test_word_in_string_color(
        self,
        all_colors: Color,
        small_color_test_string,
        all_cs_marked_color: str,
    ) -> None:
        colored_keys = all_colors.red.get_key(
            small_color_test_string, "cc:", case=True, any_=True
        )
        assert colored_keys == all_cs_marked_color
