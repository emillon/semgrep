from __future__ import annotations

from typing import List
from typing import Optional
from typing import Union

IntOrFloat = Union[int, float]

def ceil(x: IntOrFloat, options: list[IntOrFloat] | None = ...) -> int: ...
def clamp(
    x: IntOrFloat, lower: IntOrFloat = ..., upper: IntOrFloat = ...
) -> IntOrFloat: ...
def floor(x: IntOrFloat, options: list[IntOrFloat] | None = ...) -> int: ...
