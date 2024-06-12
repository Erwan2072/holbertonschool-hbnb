#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class Country:
    code: str
    name: str

# Pre-loaded countries (example)
COUNTRIES = [
    Country(code="US", name="United States"),
    Country(code="CA", name="Canada"),
    # Add other countries as needed
]
