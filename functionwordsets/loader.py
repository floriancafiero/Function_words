from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True, slots=True)
class FunctionWordSet:
    name: str
    language: str
    period: str
    categories: dict[str, frozenset[str]]

    @property
    def all(self) -> frozenset[str]:
        return frozenset().union(*self.categories.values())

    def subset(self, keys: Iterable[str]) -> frozenset[str]:
        return frozenset().union(*(self.categories[k] for k in keys))

# Nouveau : liste des identifiants disponibles (à la main ou automatisée plus tard)
_AVAILABLE_IDS = [
    "fr_21c",
    "en_21c",
    "gr_5cbc",
]

def available_ids() -> list[str]:
    return _AVAILABLE_IDS

def load(id_: str = "fr_21c") -> FunctionWordSet:
    if id_ not in _AVAILABLE_IDS:
        raise ValueError(f"unknown function-word set: {id_}")
    
    # Import dynamique du module de données
    mod = __import__(f"functionwordsets.datasets.{id_}", fromlist=["data"])
    raw = mod.data

    # Conversion en frozenset pour respecter le typage
    cats = {k: frozenset(v) for k, v in raw["categories"].items()}
    
    return FunctionWordSet(
        name=raw["name"],
        language=raw["language"],
        period=raw["period"],
        categories=cats,
    )
