# -*- encoding: UTF-8 -*-
# Copyright (C) 2021 Bartosz Rosiak. All rights reserved.

import pytest
from order import get_boxes, main
from unittest.mock import patch, ANY

expected_values =   [(1, 0, 0, 0)] * 3 + \
                    [(0, 1, 0, 0)] * 3 + \
                    [(0, 0, 1, 0)] * 3 + \
                    [(0, 2, 0, 1)] * 3 + \
                    [(0, 0, 2, 1)] * 6 + \
                    [(1, 0, 2, 1)] * 3 + \
                    [(0, 1, 2, 1)] * 3 + \
                    [(0, 0, 3, 1)] * 3 + \
                    [(1, 0, 3, 2)] * 3 + \
                    [(0, 1, 3, 2)] * 3 + \
                    [(0, 0, 4, 2)] * 3 + \
                    [(1, 0, 4, 2)] * 3 + \
                    [(0, 1, 4, 2)] * 3 + \
                    [(0, 0, 5, 2)] * 3 + \
                    [(1, 0, 5, 2)] * 3 + \
                    [(0, 1, 5, 2)] * 3 + \
                    [(0, 0, 6, 2)] * 3 + \
                    [(1, 0, 6, 3)] * 3 + \
                    [(0, 1, 6, 3)] * 3 + \
                    [(0, 0, 7, 3)] * 3 + \
                    [(1, 0, 7, 3)] * 3 + \
                    [(0, 1, 7, 3)] * 3 + \
                    [(0, 0, 8, 3)] * 3 + \
                    [(1, 0, 8, 3)] * 3 + \
                    [(0, 1, 8, 3)] * 3 + \
                    [(0, 0, 9, 3)] * 3 + \
                    [(1, 0, 9, 4)] * 3 + \
                    [(0, 1, 9, 4)] * 3 + \
                    [(0, 0, 10, 4)] * 3 + \
                    [(1, 0, 10, 4)] * 3 + \
                    [(0, 1, 10, 4)] * 3 + \
                    [(0, 0, 11, 4)] * 3 + \
                    [(1, 0, 11, 4)]





@pytest.mark.parametrize(
    "input_value", range(1,100)
)
def test_get_boxes_correct_order_size(input_value):
    assert get_boxes(input_value) == expected_values[input_value - 1]


@pytest.mark.parametrize("input_value", ["abc", 5.5, (10, 10)])
def test_get_boxes_invalid_input_value(input_value):
    with pytest.raises(TypeError):
        get_boxes(input_value)


@pytest.mark.parametrize("input_value", [-50, 0, 101])
def test_get_boxes_input_ouf_of_range(input_value):
    with pytest.raises(ValueError):
        get_boxes(input_value)


@pytest.fixture
def arg_parse_fixt():
    with patch("order.ArgumentParser") as mock:
        yield mock


@pytest.fixture
def get_boxes_fixt():
    with patch("order.get_boxes") as mock:
        yield mock


def test_main(arg_parse_fixt, get_boxes_fixt):
    main()
    arg_parse_fixt.assert_called_once_with()
    arg_parse_fixt.return_value.add_argument.assert_called_once_with(
        "order_size", help=ANY, type=int
    )
    arg_parse_fixt.return_value.parse_args.assert_called_once()
    get_boxes_fixt.assert_called_once_with(
        arg_parse_fixt.return_value.parse_args.return_value.order_size
    )
