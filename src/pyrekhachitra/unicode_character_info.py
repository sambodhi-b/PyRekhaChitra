from dataclasses import dataclass
from typing import Any
import unicodedata


@dataclass(frozen=True)
class UnicodeCharacterInfo:
    unicode_int: int

    @property
    def unicode_hex(self) -> str:
        return hex(self.unicode_int)

    @property
    def character(self) -> str:
        return chr(self.unicode_int)

    @property
    def full_name(self) -> str:
        return unicodedata.name(self.character)

    @property
    def name_split(self) -> list[str]:
        return self.full_name.split(" ")

    def to_json(self) -> dict[str, Any]:
        return {
            "unicode_int": self.unicode_int,
            "unicode_hex": self.unicode_hex,
            "character": self.character,
            "full_name": self.full_name,
            "name_split": self.name_split,
        }
