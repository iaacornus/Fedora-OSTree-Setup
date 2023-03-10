from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text


def section(title_: str, msg_: Optional[str] = None) -> None:
    """For displaying of title in major operation.

    Args:
        txt -- main txt to display
        title -- title of the section
    """

    if not msg_:
        msg_, title_ = title_, None # type: ignore

    Console().print(
        Panel(
            Align(
                Text(
                    msg_.upper(),
                    justify="center"
                ),
                vertical="middle",
                align="center"
            ),
            title=title_
        )
    )

    return None
