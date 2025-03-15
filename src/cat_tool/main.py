from pathlib import Path
import sys
import io


def main(
    *,
    file: Path,
    file2: Path | None = None,
    output: io.StringIO = sys.stdout,
    number: bool = False,
    number_nonblank: bool = False,
) -> None:
    content = file.read_text()
    if file2:
        content += file2.read_text()

    lines = content.splitlines()

    if number:
        lines = [f"{num + 1} {line}" for num, line in enumerate(lines)]
    if number_nonblank:
        count = 1
        new_lines = []
        for line in lines:
            if line.strip():
                new_lines.append(f"{count} {line}")
                count += 1
            else:
                new_lines.append(line)
        lines = new_lines

    output.write("\n".join(lines) + "\n")
    output.flush()


def _cli() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_cccat = subparsers.add_parser("cccat")
    parser_cccat.add_argument("file", type=Path)
    parser_cccat.add_argument("file2", nargs="?", type=Path, default=None)
    parser_cccat.add_argument("-n", "--number", action="store_true")
    parser_cccat.add_argument("-b", "--number-nonblank", action="store_true")

    args = parser.parse_args()

    if args.command == "cccat":
        main(
            file=args.file,
            file2=args.file2,
            number=args.number,
            number_nonblank=args.number_nonblank,
        )


if __name__ == "__main__":
    _cli()
