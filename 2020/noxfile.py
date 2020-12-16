import nox

BLACK_PATHS = ["helpers", "."]


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
    """Run the unit test suite."""
    session.install("pytest")
    session.run("pytest")
