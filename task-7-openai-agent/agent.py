from dataclasses import dataclass
from typing import Callable, TypeVar

ContextType = TypeVar("ContextType")

@dataclass
class SmartAgent:
    title: str
    behavior: str | Callable
    model_type: str
    context: ContextType | None = None
