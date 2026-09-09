from client import EarClippingTriangulator

def main():
    print("=== Ear Clipping Polygon Triangulator ===")
    triangulator = EarClippingTriangulator()

    # L-shaped simple polygon (6 vertices)
    poly = [(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2)]
    res = triangulator.triangulate(poly)
    print("Triangulation result:", res["triangle_count"], "triangles generated.")
    assert res["triangle_count"] == 4 # (N - 2) triangles for N=6

    print("Ear Clipping Triangulator verified successfully!")

if __name__ == "__main__":
    main()
