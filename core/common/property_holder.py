from typing import Any

from dataclasses import dataclass


@dataclass
class PropertyHolder:
    name: str
    property: Any
