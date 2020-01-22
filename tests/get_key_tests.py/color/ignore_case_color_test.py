#!/usr/bin/env python3
from object_colors import Color


class TestIgnoreCaseColor:
    def test_exact_word_in_string_ignore_case_color(
        self,
        all_colors: Color,
        small_color_test_string,
        marked_word_color: str,
    ) -> None:
        """Test uncolored string entered in Color.get_key() to make sure
        an individual word which matches a word in the string exactly
        comes out colored if no scatter or ignore argument is given with
        "Cc:" key entered
        Ensure no other items are colored
        """
        colored_keys = all_colors.red.get_key(
            small_color_test_string, "Cc:", ignore_case=True
        )
        assert colored_keys == marked_word_color

    def test_word_in_string_ignore_case_color(
        self,
        all_colors: Color,
        small_color_test_string,
        marked_word_color: str,
    ) -> None:
        """Test uncolored string entered in Color.get_key() to make sure
        an individual word which does not match a word in the string
        exactly comes out the same way it came in if no scatter or
        ignore argument is given with "cc:" key entered
        """
        colored_keys = all_colors.red.get_key(
            small_color_test_string, "cc:", ignore_case=True
        )
        assert colored_keys == marked_word_color
