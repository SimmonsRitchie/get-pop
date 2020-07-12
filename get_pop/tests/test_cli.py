import pytest
import subprocess
from pathlib import Path


def test_cli_creates_file(tmpdir):
    # test
    tmpdir = Path(tmpdir)
    subprocess.run(["getpop", "tx", "--dir", tmpdir])

    # assert
    assert (tmpdir / "tx-county-pop.csv").is_file()
    assert not (tmpdir / "ny-county-pop.csv").is_file()
