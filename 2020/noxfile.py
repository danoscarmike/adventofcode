import nox

BLACK_PATHS = ["helpers", "."]


@nox.session(python="3.8")
def lint(session):
    """Run linters.
    """
    session.install("flake8", "black")
    session.run(
        "black",
        "--check",
        *BLACK_PATHS,
    )
    session.run("flake8", "*.py")


@nox.session(python="3.8")
def blacken(session):
    """Run black.
    Format code to uniform standard.
    """
    session.install("black")
    session.run(
        "black",
        *BLACK_PATHS,
    )


@nox.session(python="3.8")
def unit(session):
    """Run the unit test suite.
    """
    session.install("pytest")
    session.run("pytest")
