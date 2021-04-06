# -*- encoding: UTF-8 -*-
# Copyright (C) 2021 Bartosz Rosiak. All rights reserved.

from math import ceil
from argparse import ArgumentParser

MIN_ORDER_SIZE = 1
MAX_ORDER_SIZE = 100

SMALL_BOX_SIZE = 3
MEDIUM_BOX_SIZE = 6
BIG_BOX_SIZE = 9
SUMMARY_BOX_SIZE = 3


def get_boxes(order_size: int) -> tuple:
    """This function returns number of each type of boxes needed for order.

    Args:
        order_size (int): Size of the order [1..100].

    Raises:
        TypeError: Raises TypeError when the order_size differs from int.
        ValueError: Raises ValueError when the order_size is outside the allowable range [1..100].

    Returns:
        tuple: returns tuple in form (small_boxes, medium_boxes, big_boxes, summary_boxes)
    """

    if not isinstance(order_size, int):
        raise TypeError("Invalid type, expected int")
    if order_size < MIN_ORDER_SIZE or order_size > MAX_ORDER_SIZE:
        raise ValueError(f"Value out of range {MIN_ORDER_SIZE}..{MAX_ORDER_SIZE}")

    small_boxes = 0
    medium_boxes = 0
    big_boxes = 0
    summary_boxes = 0
    boxes_to_pack = order_size

    while MEDIUM_BOX_SIZE < boxes_to_pack:
        big_boxes += 1
        boxes_to_pack -= BIG_BOX_SIZE

    if SMALL_BOX_SIZE < boxes_to_pack:
        medium_boxes += 1
    elif 0 < boxes_to_pack:
        small_boxes += 1

    sum_of_boxes = sum([small_boxes, medium_boxes, big_boxes])
    if sum_of_boxes > 1:
        summary_boxes = ceil(sum_of_boxes / SUMMARY_BOX_SIZE)

    return small_boxes, medium_boxes, big_boxes, summary_boxes


def main():
    """This function runs get_boxes function.
    """
    parser = ArgumentParser()
    parser.add_argument(
        "order_size", help="Enter size of the order", type=int
    )
    args = parser.parse_args()
    print(get_boxes(args.order_size))


if __name__ == "__main__":
    main()
