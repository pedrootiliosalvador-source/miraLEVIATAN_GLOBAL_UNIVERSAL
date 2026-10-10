from leviathan_universal.core import build_message, get_project_summary


def test_build_message():
    assert build_message("Alice") == "Mira Leviathan Global Universal initialized for Alice."


def test_project_summary():
    summary = get_project_summary()
    assert summary["name"] == "miraLEVIATAN_GLOBAL_UNIVERSAL"
    assert summary["language"] == "python"
