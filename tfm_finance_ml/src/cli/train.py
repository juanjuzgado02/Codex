"""CLI scaffold for future phases."""

import typer

app = typer.Typer(help="Pending implementation")


@app.command("todo")
def todo() -> None:
    typer.echo("Pending implementation in future phase")


if __name__ == "__main__":
    app()
