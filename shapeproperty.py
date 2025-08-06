'''
🔍 Understanding .shape = (2, 2, 2):
1st 2 → Number of blocks (or outermost lists):
→ There are 2 big groups:
[[1,2],[3,4]] and [[2,9],[6,7]]

2nd 2 → Number of rows in each block:
Each block has 2 sublists (like rows):
[[1,2], [3,4]] → 2 rows

3rd 2 → Number of elements in each row:
Each row has 2 elements: [1,2], [3,4]...

🧠 Corrected Notes:
✅ .shape works for any regular NumPy array (not just square matrices).
It’s not limited to square matrices — it applies to all arrays that are well-formed.

🔍 Understanding .shape = (2, 2, 2):
1st 2 → Number of blocks (or outermost lists):
→ There are 2 big groups:
[[1,2],[3,4]] and [[2,9],[6,7]]

2nd 2 → Number of rows in each block:
Each block has 2 sublists (like rows):
[[1,2], [3,4]] → 2 rows

3rd 2 → Number of elements in each row:
Each row has 2 elements: [1,2], [3,4]...

🧠 Corrected Notes:
✅ .shape works for any regular NumPy array (not just square matrices).
It’s not limited to square matrices — it applies to all arrays that are well-formed.


🔄 Correction:

.shape is applicable to all properly structured (regular) arrays, whether square or not.
Even for a shape like (2, 3, 4) or (1, 5) — .shape still works.

'''
import numpy as np
array_md = np.array([[[1,2],[3,4]],[[2,9],[6,7]]])
print(array_md.shape)