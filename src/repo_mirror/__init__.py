import click

@click.version_option(version="0.1.0")
@click.group()
def main() -> None:
    """Repository Mirror Tool"""
    pass

@main.command()
def test() -> None:
    """Run a test command."""
    click.echo("The test is working")

if __name__ == "__main__":
    main()
