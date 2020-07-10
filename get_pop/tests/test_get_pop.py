import pytest
import logging
from pathlib import Path
from get_pop.get_pop import get_pop


def test_get_pop_creates_file(tmpdir):
    # test
    tmpdir = Path(tmpdir)
    input_state = ["ny"]
    get_pop(input_state, save_dir=tmpdir)

    # assert
    p = tmpdir.glob("**/*")
    assert (tmpdir / "ny-county-pop.csv").is_file()
    assert not (tmpdir / "tx-county-pop.csv").is_file()


def test_get_pop_creates_files(states, tmpdir):
    # test
    tmpdir = Path(tmpdir)
    get_pop(states, save_dir=tmpdir)

    # assert
    expected_paths = [tmpdir / f"{x}-county-pop.csv" for x in states]
    for path in expected_paths:
        assert path.is_file()
    assert not (tmpdir / "ca-county-pop.csv").is_file()
