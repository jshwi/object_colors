#!/usr/bin/env python3
from object_colors import Color


class TestIgnoreCaseAndScatterColor:
    def test_exact_letter_in_string_color(
        self, colors, color_str, exact_idx_color, all_cs_color,
    ) -> None:
        colored_keys = colors.red.get_key(color_str, "c", case=True, any_=True)
        assert colored_keys == exact_idx_color

    def test_exact_word_in_string_color(
        self, colors, color_str, marked, all_cs_color,
    ) -> None:
        colored_keys = colors.red.get_key(
            color_str, "Cc:", case=True, any_=True
        )
        assert colored_keys == all_cs_color

    def test_word_in_string_color(
        self, colors, color_str, all_cs_color,
    ) -> None:
        colored_keys = colors.red.get_key(
            color_str, "cc:", case=True, any_=True
        )
        assert colored_keys == all_cs_color
