
import os
import io
import time

from skins_diffusion import dumps, loads

"""
dumps(element)

Serialize an XML element or XML string into BinaryX format.

The input may be either an xml.etree.ElementTree.Element object or
a Unicode XML string. If an Element object is supplied, its XML
representation is generated before serialization.

The resulting bytes use the BinaryX binary representation expected
by Skins Diffusion runtime assets.

Example:
    import xml.etree.ElementTree as ET
    from skins_diffusion import dumps

    root = ET.Element(
        "Element",
        {
            "nodeType": "Primitive",
            "runtimeType": "System.String",
        },
    )
    root.text = "Hello World"

    data = dumps(root)

The returned object is a bytes instance containing the serialized
BinaryX data.

A Unicode XML string can also be supplied directly.

    xml = '<Element nodeType="Primitive">Hello World</Element>'
    data = dumps(xml)

Note: Supplying a string does not mean that the string is encoded
directly into the BinaryX representation. It is first parsed as XML
and then serialized into BinaryX format.

loads(data)

Deserialize BinaryX-encoded bytes into an ElementTree object.

The input must be a bytes object containing a valid BinaryX binary
stream. The stream is decoded and reconstructed as an XML element
tree compatible with xml.etree.ElementTree.

Example:
    from skins_diffusion import dumps, loads

    data = dumps("<Element>Example</Element>")
    tree = loads(data)

    root = tree.getroot()
    print(root.tag)
    # Element

The returned object is an xml.etree.ElementTree.ElementTree instance.
Use getroot() to access the root Element and inspect or modify its
contents using the standard ElementTree API.

Details: dumps() and loads() are complementary operations. Data
serialized with dumps() can be passed to loads() to reconstruct
the corresponding XML tree, provided the BinaryX stream is valid
and compatible with the decoder.

Note: loads() expects BinaryX-encoded bytes, not an ordinary XML
string or the original XML file contents.
"""

TEST_DIR = os.path.join("tests", "fixtures")

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"

# The tag name of root element for assert.
ROOT_TAG = "ROOT"


def supports_color() -> bool:
    return hasattr(os.sys.stdout, "isatty") and os.sys.stdout.isatty()


def make_color(text: str, code: str) -> None:
    if not supports_color():
        return text
    return f"{code}{text}{RESET}"


def log_info(message: str) -> None:
    print(f"{make_color('INFO', CYAN):<15} {message}")


def log_pass(message: str) -> None:
    print(f"{make_color('PASSED', GREEN):<15} {message}")


def log_fail(message: str) -> None:
    print(f"{make_color('FAILED', RED):<15} {message}")


def log_section(title: str) -> None:
    print()
    print(make_color(f" {title}", BOLD))
    print(make_color(" " + "─" * 48, DIM))


def main() -> None:
    start_time = time.perf_counter()

    if not os.path.exists(TEST_DIR):
        log_fail(
            f"{TEST_DIR} is not exists."
        )
        return

    files = sorted(file for file in os.listdir(TEST_DIR)
                   if os.path.isfile(os.path.join(TEST_DIR, file)))

    if not files:
        log_fail(
            f"No fixture files found in {TEST_DIR}"
        )
        return

    passed = 0
    failed = 0

    log_section("Fixture Tests")

    print()

    log_info(f"Directory : {TEST_DIR}")
    log_info(f"Files     : {len(files)}")

    log_section("Running Tests")

    for index, file in enumerate(files, start=1):
        file_path = os.path.join(TEST_DIR, file)
        file_start = time.perf_counter()

        print()
        print(f"{make_color(f'[{index}/{len(files)}]', DIM)} {make_color(file, BOLD)}")
        print()

        try:
            with io.open(file_path, "rb") as stream:
                # IMPORTANT: Data must already be decompressed with Zstandard (zstd).
                data = stream.read()

            tree = loads(data)
            root = tree.getroot()
            assert root.tag == ROOT_TAG

            log_pass("Root element assertion passed.")

            binx = dumps(root)
            assert binx == data, "Binary serialization mismatch."

            log_pass("Binary serialization assertion passed.")

            elapsed = time.perf_counter() - file_start
            passed += 1

            log_info(f"Duration          : {elapsed:.4f}s")
        except Exception as e:
            elapsed = time.perf_counter() - file_start
            failed += 1

            log_info(f"Duration          : {elapsed:.4f}s")
            log_fail(e)

    total_time = time.perf_counter() - start_time

    log_section("Test Summary")

    total = passed + failed

    print(f"  Total fixtures : {total}")
    print(f"  Passed         : {make_color(str(passed), GREEN)}")
    print(f"  Failed         : {make_color(str(failed), RED if failed else GREEN)}")
    print(f"  Duration       : {total_time:.4f}s")
    print()

    if failed:
        log_fail("TESTS FAILED")
    else:
        log_pass("ALL TESTS PASSED")

if __name__ == "__main__":
    main()