def dist_squared(x1, y1, x2, y2):
  return (x1 - x2) ** 2 + (y1 - y2) ** 2

def dist_floor(x1, y1, x2, y2):
  d = dist_squared(x1, y1, x2, y2)
  lo, hi = 0, d
  while lo < hi:
    mid = (lo + hi + 1) // 2
    if mid ** 2 <= d:
      lo = mid
    else:
      hi = mid - 1
  return lo

def dist_ceil(x1, y1, x2, y2):
  d = dist_squared(x1, y1, x2, y2)
  lo, hi = 0, d
  while lo < hi:
    mid = (lo + hi) // 2
    if mid ** 2 >= d:
      hi = mid
    else:
      lo = mid + 1
  return lo

mini = 10 ** 10
for i in range(-600, 601):
  for j in range(-600, 601):
    mini = min(mini, 2 * (dist_floor(i, j, -100, -100) + dist_floor(i, j, 100, -100) + dist_floor(i, j, 0, 200)) - 3 * (dist_ceil(i, j, 0, 110) + dist_ceil(i, j, 0, -110)))
print(mini)
