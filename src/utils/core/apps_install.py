from rich.console import Console

from src.utils.shared.exec import execute_command
from src.utils.shared.uinput import uinput
from src.utils.shared.title_banner import title_banner
from src.utils.shared.log.logger import Logger


def app_install(
        log: Logger,
        console: Console,
        app_for_install: dict[str, dict[str, str]],
        verbose: bool = False
    ) -> None:
    """For installation of recommended applications selected by the user.

    Args:
        log -- instance of Logger
        app_for_install -- lists of the recommended applications including
            their application id (aid) and description
        verbose -- whether to display the process output or not
    """

    appindex: dict[int, str] = {
            index: aid for index, aid in zip(
                range(len(app_for_install.items())), app_for_install.keys()
            )
        }

    title_banner(
        "installation of recommended apps",
        "recommended apps flatpak"
    )

    appname: str
    for index, appname in appindex.items():
        console.print(
            (
                f"[bold cyan]{index:4}[/bold cyan] "
                f"[bold]{appname}[/bold] -- "
                f"{app_for_install.get(appname).get('sdesc')}"
            )
        )

    selected_app: list[int] = uinput(
            console, "Input the number of applications to install", 2
        )

    aindex: int
    for aindex in selected_app:
        sapp_id: str = app_for_install.get(
                appindex.get(aindex)).get("aid"
            )
        install_cmd: list[str] = [
                "flatpak",
                "install",
                "flatpak",
                sapp_id
            ]
        execute_command(log, install_cmd, verbose)

    return None
