import sys


class SimpleEngine:
    def __init__(self):
        self.moves = []

    def handle_command(self, line: str):
        line = line.strip()
        if line == "uci":
            print("id name SimplePythonUCI")
            print("id author ChatGPT")
            print("uciok")
        elif line == "isready":
            print("readyok")
        elif line.startswith("position"):
            parts = line.split("moves")
            if len(parts) > 1:
                moves_part = parts[1].strip()
                self.moves = moves_part.split()
            else:
                self.moves = []
        elif line.startswith("go"):
            print("bestmove e2e4")
        elif line == "quit":
            return False
        else:
            # Ignore any other commands.
            pass
        sys.stdout.flush()
        return True


def main():
    engine = SimpleEngine()
    for line in sys.stdin:
        if not engine.handle_command(line):
            break


if __name__ == "__main__":
    main()
