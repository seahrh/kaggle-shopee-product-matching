import re
from re import Pattern
from typing import Tuple, Set, NamedTuple

__all__ = ["Measurement", "get_measurements"]

FLAGS = re.IGNORECASE


class Rule(NamedTuple):
    pattern: Pattern
    uom: str
    scale: int


class Measurement(NamedTuple):
    quantity: int
    uom: str


RULES: Tuple[Rule, ...] = tuple(
    [
        Rule(
            pattern=re.compile(r"\b(\d+)\s*(g|gr|grams?)\b", FLAGS), uom="gram", scale=1
        ),
        Rule(
            pattern=re.compile(r"\b(\d+)\s*(kg|kilos?|kilograms?)\b", FLAGS),
            uom="gram",
            scale=1000,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+)\s*(mm|millimetres?|millimeters?)\b", FLAGS),
            uom="millimetre",
            scale=1,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+)\s*(cm|centimetres?|centimeters?)\b", FLAGS),
            uom="millimetre",
            scale=10,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+)\s*(m|metres?|meters?)\b", FLAGS),
            uom="millimetre",
            scale=1000,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+)\s*(ml|millilitres?|milliliters?)\b", FLAGS),
            uom="millilitre",
            scale=1,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+)\s*(l|litres?|liters?)\b", FLAGS),
            uom="millilitre",
            scale=1000,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+)\s*(pcs?|pieces?)\b", FLAGS),
            uom="piece",
            scale=1,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+)\s*(boxs?|boxes)\b", FLAGS), uom="box", scale=1,
        ),
    ]
)


def get_measurements(s: str, rules: Tuple[Rule, ...] = RULES) -> Set[Measurement]:
    res = set()
    for r in rules:
        m = r.pattern.search(s)
        if m:
            mt = Measurement(quantity=int(m.group(1)) * r.scale, uom=r.uom)
            res.add(mt)
    return res
