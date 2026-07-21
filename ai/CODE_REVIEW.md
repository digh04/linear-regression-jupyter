# Code Review: `assignment3` → `main`

**Review date:** 2026-07-20  
**Base branch:** `main`  
**Compare branch:** `assignment3`  
**Commits in PR:** 2  
**Diff scope:** 22 files changed, 855 insertions(+), 2395 deletions(-)

| Commit     | Message |
|------------|---------|
| `84e2b65`  | Assignment 3: Regression annotations, diagnostics, and plots |
| `6dec060`  | Enhance ai/ linear model workflow with diagnostics and annotated plots |

---

## Summary

This pull request extends Assignment 2 linear regression work into Assignment 3 by:

1. Replacing basic `regression_*` / `linear_regression_*` artifacts with **`linear_model_*`** scripts and notebooks in both **`manual/`** and **`ai/`**.
2. Adding **slope**, **intercept**, **Pearson's r**, and **MSE** to console/notebook output.
3. Adding **annotated scatter plots** with a fitted line, equation, and correlation.
4. Saving PNG outputs as **`regression_plot_python.png`** and **`regression_plot_r.png`**.
5. Replacing the root **`README.md`** with IPIR/process documentation for the assignment workflow.

The **`ai/`** implementation is the strongest part of the PR: it meets the Assignment 3 functional requirements, uses consistent labeling, and produces matching Python/R results.

---

## Assignment requirements checklist

| Requirement | `ai/` | `manual/` | Notes |
|-------------|-------|-----------|-------|
| Fit linear regression (X vs Y) | Yes | Yes | Both use `YearsExperience` → `Salary` |
| Print slope & intercept | Yes | Yes | |
| Print Pearson's r | Yes | Yes | `manual/` labels output as `r:` only |
| Print MSE | Yes | Yes | |
| Scatter + fitted line | Yes | Yes | |
| Plot annotation: equation + r | Yes | Partial | `manual/` also includes MSE on plot |
| Script saves PNG | Yes | Yes | |
| Notebook markdown: what is calculated | Yes | Yes | `ai/` structure is clearer |
| Notebook markdown: interpretation | Yes | Yes | `manual/` embeds hard-coded numeric examples |
| Use `7030_class_2` kernels | Yes | Yes | Notebook metadata present |
| Renamed to `linear_model_*` | Yes | Yes | |
| Updated readme in `ai/` | Yes | N/A | `ai/README_AI.md` reflects new workflow |

**Verdict:** Assignment 3 functional goals are **met**, especially in **`ai/`**.

---

## Verified behavior (`ai/` scripts)

Both scripts were run successfully against `../manual/regression_data.csv` with `YearsExperience` and `Salary`:

```
Slope: 8285.29
Intercept: 29203.52
Correlation coefficient (Pearson's r): 0.89
Mean Squared Error (MSE): 17523844.08
```

Python and R agree on all four metrics. PNG files are written to the working directory as expected.

---

## Strengths

### `ai/` scripts (`linear_model.py`, `linear_model.R`)

- Preserve the Assignment 2 **CLI interface** (`<filename> <x_column> <y_column>`), which keeps the scripts reusable beyond this dataset.
- Use clear, assignment-aligned labels (`Correlation coefficient (Pearson's r)`, `Mean Squared Error (MSE)`).
- Plot annotation placement scales with the data (`x.min() + 0.1`, `y.max() * 0.92`), avoiding the coordinate bug present in some `manual/` plots.
- Python uses `scipy.stats.linregress` and `sklearn.metrics.mean_squared_error`; R uses `lm()`, `cor()`, and manual MSE — appropriate and consistent.

### `ai/` notebooks

- Good separation of **explanation** (markdown) and **computation** (code).
- Interpretation section correctly cautions that the intercept at zero years is **extrapolation** outside the observed x-range.
- Kernels target **`7030_class_2`** / **`ir_7030_class_2`** as required.

### `ai/README_AI.md`

- Accurately documents filenames, commands, outputs, and expected approximate results.
- Workflow diagram matches the current file layout.

### Overall refactor

- Removing large legacy notebooks (`regression_python.ipynb`, `linear_regression_python.ipynb`, etc.) significantly reduces repo noise while keeping the core analysis.

---

## Issues and recommendations

### High priority (consider fixing before merge)

1. **Root `README.md` is process notes, not project documentation**  
   The PR replaces the repository README with “README EDITS / Demonstrates IPIR” instructions (clone steps, gedit, squash merge, tags). That may satisfy an IPIR assignment, but it removes user-facing documentation for the linear regression project itself.  
   **Recommendation:** Either restore a project README and move IPIR notes to a separate file (e.g. `IPIR.md`), or add a brief project overview section at the top of `README.md` so newcomers understand what the repo contains.

2. **`manual/` and `ai/` implementations diverge in quality**  
   - `manual/linear_model.py` reads like a **nbconvert export** (cell markers like `# In[6]:`, duplicated imports, commentary as `#` comments instead of notebook markdown).  
   - It contains a typo: `print(f"Slope: = {slope:.2f}")`.  
   - Plot text uses `plt.text(1.5, max(y) - 1, ...)`, which places the annotation near **y ≈ 63,217** instead of a readable in-plot position (the `- 1` is negligible on a ~60k scale).  
   **Recommendation:** Align `manual/` scripts/notebooks with the cleaner `ai/` patterns, or document why the two folders intentionally differ.

3. **Stale HTML exports remain in `ai/`**  
   `linear_regression_python.html` and `linear_regression_R.html` are not part of the diff deletions but still reference the removed notebooks.  
   **Recommendation:** Regenerate HTML from `linear_model_python.ipynb` / `linear_model_r.ipynb`, or remove outdated exports to avoid confusion.

### Medium priority

4. **Duplicated PNG binaries**  
   The PR commits generated plots in both `manual/` and `ai/`. That is acceptable for submission evidence, but the images can drift if scripts change.  
   **Recommendation:** Document in readme that PNGs are script outputs, or add a short “regenerate plots” section.

5. **Minor polish in `manual/linear_model.r`**  
   - Annotation uses `y = max(dataset$Salary) - 0.5`; works for this dataset but is inconsistent with the scaled placement used in `ai/`.  
   - Missing trailing newline at EOF (also true for `manual/linear_model.py`).

6. **No input validation on CLI column names**  
   If a user passes a nonexistent column, both Python and R fail with library-specific errors. Acceptable for a classroom assignment; optional improvement would be a friendly error message.

7. **R loads `ggplot2` after computation**  
   Works fine, but moving `library(ggplot2)` to the top would match common R style.

### Low priority / nitpicks

8. **`manual/` notebook prose** uses lowercase “python” in places where “Python” is preferred for consistency with `ai/`.  
9. **Hard-coded interpretation numbers** in `manual/` notebooks (8285.29, 29203.52, etc.) will become stale if the dataset changes; `ai/` notebooks describe ranges (“near 8285”) which age better.  
10. **Commit history:** Two commits is reasonable; squash merge (as described in README) will produce a single clean commit on `main`.

---

## Consistency matrix

| Aspect | `ai/linear_model.py` | `manual/linear_model.py` | Match? |
|--------|----------------------|--------------------------|--------|
| CLI arguments | 3 args | Hard-coded CSV/columns | No |
| Console labels | Full Pearson/MSE labels | Shorter `r`, `MSE` labels | Partial |
| Plot line color | Blue | Red | No |
| Annotation content | Equation + r | Equation + r + MSE | Partial |
| Code style | Purpose-built script | Notebook export | No |

| Aspect | `ai/linear_model.R` | `manual/linear_model.r` | Match? |
|--------|---------------------|-------------------------|--------|
| CLI arguments | 3 args | Hard-coded | No |
| Console labels | Full labels | Shorter labels | Partial |
| Fitted line color | Blue | Red | No |

For grading, **`ai/`** is the reference implementation. **`manual/`** satisfies many of the same outcomes but with inconsistent polish.

---

## Security and dependencies

- No secrets, credentials, or unsafe patterns observed.
- Dependencies (`pandas`, `matplotlib`, `scipy`, `scikit-learn`, `ggplot2`) match the documented `7030_class_2` environment.
- No new network or shell execution beyond standard script behavior.

---

## Merge recommendation

**Approve with minor follow-ups.**

The PR successfully delivers Assignment 3 enhancements: renamed artifacts, required statistics, annotated plots, PNG outputs, and updated `ai/README_AI.md`. The **`ai/`** folder is merge-ready.

Before or immediately after merge, address:

1. Root **`README.md`** purpose (project docs vs IPIR notes only).  
2. **`manual/`** parity and typos (especially `Slope: =` and plot annotation coordinates).  
3. Stale **`ai/*.html`** exports tied to deleted notebooks.

---

## Suggested post-merge test plan

```bash
conda activate 7030_class_2
cd ai
python linear_model.py ../manual/regression_data.csv YearsExperience Salary
Rscript linear_model.R ../manual/regression_data.csv YearsExperience Salary
```

- [ ] Confirm four metrics print and match between Python and R  
- [ ] Confirm `regression_plot_python.png` and `regression_plot_r.png` are created  
- [ ] Run `linear_model_python.ipynb` and `linear_model_r.ipynb` top-to-bottom in Jupyter  
- [ ] Optionally repeat from `manual/` if those artifacts are part of the graded deliverable

---

## Files reviewed (PR diff)

**Added / replaced**

- `ai/linear_model.py`, `ai/linear_model.R`, `ai/linear_model_python.ipynb`, `ai/linear_model_r.ipynb`
- `ai/regression_plot_python.png`, `ai/regression_plot_r.png`
- `manual/linear_model.py`, `manual/linear_model.r`, `manual/linear_model_python.ipynb`, `manual/linear_model_r.ipynb`
- `manual/regression_plot_python.png`, `manual/regression_plot_r.png`
- `README.md` (IPIR/process content)

**Removed**

- `ai/linear_regression_python.py`, `ai/linear_regression_R.R`, `ai/linear_regression_python.ipynb`, `ai/linear_regression_R.ipynb`
- `manual/regression_python.py`, `manual/regression_R.r`, `manual/regression_python.ipynb`, `manual/regression_R.ipynb`

**Modified**

- `ai/README_AI.md`

**Not in diff but still present (stale)**

- `ai/linear_regression_python.html`, `ai/linear_regression_R.html`
