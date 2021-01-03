def box_size(coord):
    a1, b1, a2, b2 = coord
    return (a2 - a1) * (b2 - b1)

def find_boxes(row, col, threshold, num_boxes, image):
    boxes = []
    visited = set()
    for i in range(row):
        for j in range(col):
            if (i, j) in visited or image.item(i, j) >= threshold:
                continue
            coord = _flood_fill(i, j, visited, row, col, image, threshold)
            boxes.append(coord)
            boxes.sort(key=box_size, reverse=True)
            if len(boxes) > num_boxes:
                boxes.pop()
    return boxes

def _flood_fill(i, j, visited, row, col, image, threshold):
    r1 = r2 = i
    c1 = c2 = j
    stack = [(i, j)]
    visited.add((i, j))
    while stack:
        r, c = stack.pop()
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if nr < 0 or nc < 0 or nr >= row or nc >= col:
                continue
            if (nr, nc) in visited or image.item(nr, nc) >= threshold:
                continue
            r1 = min(nr, r1)
            r2 = max(nr, r2)
            c1 = min(nc, c1)
            c2 = max(nc, c2)
            stack.append((nr, nc))
            visited.add((nr, nc))
    return (c1, r1, c2, r2)