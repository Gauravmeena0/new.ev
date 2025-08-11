import subprocess

def test_uci_flow():
    proc = subprocess.Popen([
        "python", "-u", "uci_app.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    out, _ = proc.communicate("uci\nisready\ngo\nquit\n", timeout=5)
    lines = [line.strip() for line in out.splitlines() if line.strip()]
    assert "uciok" in lines
    assert "readyok" in lines
    assert "bestmove e2e4" in lines
