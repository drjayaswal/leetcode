# LeetCode 

This will be our shared repository! This will be a space to track our progress, share solutions, and level up algorithmic thinking together.


| Username | Branch | Status |
| :--- | :--- | :--- |
| **@drjayaswal** | `/dhruv` | NIL |
| **@gungunvyas** | `/gungun` | NIL |

---

## Repository Structure

Each of us works on our own dedicated branch to avoid merge conflicts. We organize our solutions by difficulty or topic:

```text
.
├── easy/
│   ├── problem_name.py
│   └── problem_name.java
├── medium/
│   └── problem_name.cpp
└── hard/
    └── problem_name.py
```

---

## Getting Started

### 1. Clone and Setup
```bash
git clone <repository-url>
cd leetcode-solutions
```

### 2. Create Your Branch
```bash
git checkout -b /your-username
git push -u origin /your-username
```


---

## Contribution Guidelines

### File Naming Convention
- Format: `{problem-number}-{problem-name}.{extension}`
- Example: `1-two-sum.py`, `15-3sum.java`
- Use lowercase with hyphens for readability

### Solution Template
Each solution should include:
```python
"""
Problem: [Problem Title]
Difficulty: [Easy/Medium/Hard]
URL: [LeetCode URL]

Approach: [Brief description of your approach]
Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def solutionMethod(self, params):
        # Your solution here
        pass
```

### Commit Message Format
- `feat: add solution for problem {number} - {title}`
- `fix: update solution for problem {number}`
- `docs: add explanation for problem {number}`

---



### Branch Management
```bash
# Work on your branch
git checkout /your-username

# Regular updates
git add .
git commit -m "feat: add solution for problem X"
git push origin /your-username

# Stay updated with main
git checkout main
git pull origin main
git checkout /your-username
git merge main
```

---

### Study Materials
- [LeetCode Patterns](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)
- [Algorithm Visualizations](https://visualgo.net/)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
