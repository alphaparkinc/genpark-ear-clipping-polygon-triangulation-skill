import sys
import json
from client import EarClippingTriangulator

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "triangulate":
        t = EarClippingTriangulator()
        return t.triangulate(params.get("vertices", []))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
