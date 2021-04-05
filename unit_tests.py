# -*- encoding: UTF-8 -*-
# Copyright (C) 2021 Bartosz Rosiak. All rights reserved.

import pytest
from order import get_boxes, main
from unittest.mock import patch, ANY

@pytest.mark.parametrize(
    "input_value, expected_value", [(1, (1, 0, 0, 1)), (5, (0, 1, 0, 1)), (10, (1, 0, 1, 1)), (30, (1, 0, 3, 2)), (31, (0, 1, 3, 2)), (34, (0, 0, 4, 2))]
)
def test_get_boxes_correct_order_size(input_value, expected_value):
    assert get_boxes(input_value) == expected_value


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
