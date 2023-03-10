from typing import Any, IO, NoReturn

from rich.console import Console

from src.utils.shared.misc.uinput import uinput
from src.utils.shared.log.logger import Logger


class VariantBasedOpt:
    """Optimizations for specific variant of Fedora OSTree."""

    def __init__(self, log: Logger, console: Console) -> None:
        self.log: Logger = log
        self.console: Console = console

    def _fetch_variant(self) -> str | Any:
        """Fetch the name of variant using /etc/os-release

        Returns:
            The VARIANT_ID or VARIANT declared in /etc/os-release
        """

        try:
            osr: IO[Any]; lines: str
            with open("/etc/os-release", "r", encoding="UTF-8") as osr:
                for lines in osr.readlines():
                    if lines.lower().startswith(("variant_id", "variant")):
                        return (
                                lines
                                    .removeprefix("variant_id")
                                    .removeprefix("variant")
                                    .replace(r"\n", "")
                            )
        except (FileNotFoundError, PermissionError) as Err:
            self.log.logger(
                "E", f"{Err}. Cannot find /etc/os-release file."
            )

        return uinput(
            self.console,
            "Kindly input the Fedora OSTree variant you are using",
            3
        )

    def remove_base_programs(self, variant: str) -> NoReturn | None: # type: ignore
        """Remove programs layered in base image of a given variant."""

        base_programs: dict[str, list[str]] = {
                "kinoite": [
                        ""
                    ],
                "silverblue": [
                        ""
                    ],
                "vauxite": [ #! from what ive heard this variant is still not yet official
                        ""
                    ]
            }

    def sys_opt(self, variant: str) -> NoReturn | None: # type: ignore
        """Removal/alteration of default settings that are
        known to be detrimental in terms of performance."""

        sys_opts: dict[str, list[str | list[str]]] = {
                "kinoite": [
                        ""
                    ],
                "silverblue": [
                        [ # disable gnome software from autostart
                            "sudo",
                            "rm",
                            (
                                "/etc/xdg/autostart/"
                                "org.gnome.Software.desktop"
                            )
                        ]
                    ],
                "vauxite": [
                        ""
                    ]
            }
