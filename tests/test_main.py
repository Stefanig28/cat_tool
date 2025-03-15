import pytest
import pathlib
import io

from src.cat_tool.main import main


@pytest.mark.parametrize(
    "content, expected",
    [
        ("abc123", "abc123\n"),
        ("", "\n"),
        ("line1\nline2\nline3", "line1\nline2\nline3\n"),
    ],
)
def test_main(tmp_path: pathlib.Path, content, expected):
    file_path = tmp_path / "test.txt"
    file_path.write_text(content)

    out = io.StringIO()
    main(file=file_path, output=out)

    assert out.getvalue() == expected


@pytest.mark.parametrize(
    "file, file2, expected",
    [
        ("abc", "123", "abc123\n"),
        ("", "", "\n"),
        ("line1\nline2\n", "line3", "line1\nline2\nline3\n"),
    ],
)
def test_main_with_two_files(tmp_path: pathlib.Path, file, file2, expected):
    file_path = tmp_path / "test.txt"
    file2_path = tmp_path / "test2.txt"

    file_path.write_text(file)
    file2_path.write_text(file2)

    out = io.StringIO()
    main(file=file_path, file2=file2_path, output=out)

    assert out.getvalue() == expected


@pytest.mark.parametrize(
    "content, expected",
    [
        ("abc123", "1 abc123\n"),
        ("", "\n"),
        ("line1\nline2\nline3\n", "1 line1\n2 line2\n3 line3\n"),
    ],
)
def test_main_number(tmp_path: pathlib.Path, content, expected):
    file_path = tmp_path / "test.txt"
    file_path.write_text(content)

    out = io.StringIO()
    main(file=file_path, output=out, number=True)

    assert out.getvalue() == expected


@pytest.mark.parametrize(
    "file, file2, expected",
    [
        ("abc", "123", "1 abc123\n"),
        ("", "", "\n"),
        ("line1\nline2\n", "line3\n", "1 line1\n2 line2\n3 line3\n"),
    ],
)
def test_main_number_with_two_files(tmp_path: pathlib.Path, file, file2, expected):
    file_path = tmp_path / "test.txt"
    file2_path = tmp_path / "test2.txt"

    file_path.write_text(file)
    file2_path.write_text(file2)

    out = io.StringIO()
    main(file=file_path, file2=file2_path, output=out, number=True)

    assert out.getvalue() == expected


@pytest.mark.parametrize(
    "content, expected",
    [
        ("abc\n\n123", "1 abc\n\n2 123\n"),
        ("", "\n"),
        ("line1\nline2\n\nline3", "1 line1\n2 line2\n\n3 line3\n"),
    ],
)
def test_main_number_nonblank(tmp_path: pathlib.Path, content, expected):
    file_path = tmp_path / "test.txt"
    file_path.write_text(content)

    out = io.StringIO()
    main(file=file_path, output=out, number_nonblank=True)

    assert out.getvalue() == expected


@pytest.mark.parametrize(
    "file, file2, expected",
    [
        ("abc", "123", "1 abc123\n"),
        ("", "", "\n"),
        ("line1\nline2\n", "line3\n", "1 line1\n2 line2\n3 line3\n"),
    ],
)
def test_main_number_nonblank_with_two_files(
    tmp_path: pathlib.Path, file, file2, expected
):
    file_path = tmp_path / "test.txt"
    file2_path = tmp_path / "test2.txt"

    file_path.write_text(file)
    file2_path.write_text(file2)

    out = io.StringIO()
    main(file=file_path, file2=file2_path, output=out, number_nonblank=True)

    assert out.getvalue() == expected
