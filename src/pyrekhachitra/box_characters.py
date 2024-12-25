from dataclasses import dataclass
import json
from typing import Any, override
from enum import E
from unicode_character_info import UnicodeCharacterInfo


@dataclass(frozen=True)
class BoxCharacterInfo(UnicodeCharacterInfo):
    @property
    def name_split(self) -> list[str]:
        return super().name_split[2:]

    @property
    def is_line(self) -> bool:
        return ("AND" not in self.name_split) and (
            ("HORIZONTAL" in self.name_split) or ("VERTICAL" in self.name_split)
        )

    @override
    def to_json(self) -> dict[str, Any]:
        return {"character": self.character, "is_line": self.is_line}


box_drawing_character_list = [
    BoxCharacterInfo(unicode_int=unicode_index)
    for unicode_index in range(0x2500, 0x2580)
]

with open("box_char_report.json", "w+", encoding="utf-8") as f:
    json.dump(
        box_drawing_character_list,
        f,
        ensure_ascii=False,
        indent=2,
        default=lambda o: o.to_json(),
    )

# def generate_neighbor_criteria()
# class


# ─
# ━
# │
# ┃
# ┄
# ┅
# ┆
# ┇
# ┈
# ┉
# ┊
# ┋
# ┌
# ┍
# ┎
# ┏
# ┐
# ┑
# ┒
# ┓
# └
# ┕
# ┖
# ┗
# ┘
# ┙
# ┚
# ┛
# ├
# ┝
# ┞
# ┟
# ┠
# ┡
# ┢
# ┣
# ┤
# ┥
# ┦
# ┧
# ┨
# ┩
# ┪
# ┫
# ┬
# ┭
# ┮
# ┯
# ┰
# ┱
# ┲
# ┳
# ┴
# ┵
# ┶
# ┷
# ┸
# ┹
# ┺
# ┻
# ┼
# ┽
# ┾
# ┿
# ╀
# ╁
# ╂
# ╃
# ╄
# ╅
# ╆
# ╇
# ╈
# ╉
# ╊
# ╋
# ╌
# ╍
# ╎
# ╏
# ═
# ║
# ╒
# ╓
# ╔
# ╕
# ╖
# ╗
# ╘
# ╙
# ╚
# ╛
# ╜
# ╝
# ╞
# ╟
# ╠
# ╡
# ╢
# ╣
# ╤
# ╥
# ╦
# ╧
# ╨
# ╩
# ╪
# ╫
# ╬
# ╭
# ╮
# ╯
# ╰
# ╱
# ╲
# ╳
# ╴
# ╵
# ╶
# ╷
# ╸
# ╹
# ╺
# ╻
# ╼
# ╽
# ╾
# ╿
