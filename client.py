class EarClippingTriangulator:
    """Ear clipping triangulation algorithm for arbitrary simple 2D polygons."""
    def _area2(self, p0, p1, p2) -> float:
        return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p1[1] - p0[1]) * (p2[0] - p0[0])

    def _point_in_triangle(self, p, a, b, c) -> bool:
        d1 = self._area2(p, a, b)
        d2 = self._area2(p, b, c)
        d3 = self._area2(p, c, a)
        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
        return not (has_neg and has_pos)

    def triangulate(self, vertices: list[tuple[float, float]]) -> dict:
        n = len(vertices)
        if n < 3:
            return {"error": "At least 3 vertices required", "triangles": []}

        # Ensure counter-clockwise winding
        total_area = sum(vertices[i][0] * vertices[(i+1)%n][1] - vertices[(i+1)%n][0] * vertices[i][1] for i in range(n))
        poly = list(vertices)
        if total_area < 0:
            poly.reverse()

        indices = list(range(n))
        triangles = []

        while len(indices) > 3:
            ear_found = False
            for i in range(len(indices)):
                prev_i = indices[(i - 1) % len(indices)]
                curr_i = indices[i]
                next_i = indices[(i + 1) % len(indices)]

                p_prev = poly[prev_i]
                p_curr = poly[curr_i]
                p_next = poly[next_i]

                # Check if convex ear
                if self._area2(p_prev, p_curr, p_next) <= 0:
                    continue

                # Check if any other remaining vertex lies inside the triangle
                contains_other = False
                for j in range(len(indices)):
                    if j in ((i - 1) % len(indices), i, (i + 1) % len(indices)):
                        continue
                    if self._point_in_triangle(poly[indices[j]], p_prev, p_curr, p_next):
                        contains_other = True
                        break

                if not contains_other:
                    triangles.append([prev_i, curr_i, next_i])
                    indices.pop(i)
                    ear_found = True
                    break

            if not ear_found:
                break

        if len(indices) == 3:
            triangles.append([indices[0], indices[1], indices[2]])

        return {
            "vertex_count": n,
            "triangle_count": len(triangles),
            "triangles": triangles
        }
