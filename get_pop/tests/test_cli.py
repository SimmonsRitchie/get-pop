import pytest
import subprocess
from pathlib import Path


def test_cli_creates_file(tmpdir):
    # test
    tmpdir = Path(tmpdir)
    subprocess.run(["getpop", "tx", "-d", tmpdir])

    # assert
    assert (tmpdir / "tx-county-pop.csv").is_file()
    assert not (tmpdir / "ny-county-pop.csv").is_file()


def test_cli_creates_files(states, tmpdir):
    # test
    tmpdir = Path(tmpdir)
    subprocess.run(["getpop", *states, "-d", tmpdir])

    # assert
    expected_paths = [tmpdir / f"{x}-county-pop.csv" for x in states]
    for path in expected_paths:
        assert path.is_file()
    assert not (tmpdir / "ca-county-pop.csv").is_file()
