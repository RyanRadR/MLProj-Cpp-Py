# Smoke test: verifies the package imports without error
def test_smoke():
    import mlproj_cpp_py  # If this fails, the package install or structure is broken
    assert mlproj_cpp_py.__version__ == "0.1.0"
