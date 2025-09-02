# import sys, json
# try:
#     from .milestone2 import solve
# except ImportError:
#     from milestone2 import solve

# def main():
#     if len(sys.argv) < 2:
#         print("Provide a problem string")
#         raise SystemExit(1)
#     q = sys.argv[1]
#     r = solve(q)
#     print(json.dumps(r, indent=2))

# if __name__ == "__main__":
#     main()
import sys, json
from src.milestone2 import solve

def main():
    if len(sys.argv) < 2:
        print("Provide a problem string")
        raise SystemExit(1)
    q = " ".join(sys.argv[1:])
    r = solve(q)
    print(json.dumps(r, indent=2))

if __name__ == "__main__":
    main()
