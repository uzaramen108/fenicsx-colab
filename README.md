# FEniCSx Colab Quick Start

This single cell will set up FEniCSx on Google Colab and
register the `%%fenicsx` Jupyter cell magic.

**Features**

- 🖥 micromamba executable: `/content/micromamba/bin/micromamba` (Colab local)
- 💾 Package cache: Google Drive `/content/drive/MyDrive/mamba_pkgs`
- 🔄 Safe for repeated runs: existing repo/env will be skipped
- 🧹 `--clean` option to force environment reinstallation

---

```python
# ==================================================
# 1️⃣ Mount Google Drive (for cache)
# ==================================================
from google.colab import drive
import os

if not os.path.ismount("/content/drive"):
    drive.mount("/content/drive")

# ==================================================
# 2️⃣ Clone repository (skip if exists)
# ==================================================
!git clone https://github.com/seoultechpse/fenicsx-colab.git /content/fenicsx-colab \
  || echo "📦 Repo exists — skipping"

# ==================================================
# 3️⃣ Run setup (install FEniCSx environment + %%fenicsx magic)
# ==================================================
!python /content/fenicsx-colab/setup_fenicsx.py --clean
```

### Usage Examples

- Displays MPI implementation, Python version, FEniCSx version, and active environment info.

```python
%%fenicsx --info
```

- Runs your FEniCSx code using 4 MPI ranks.

```python
%%fenicsx --np 4
import dolfinx
print("Hello from 4 MPI ranks!")
```

### Options

- `--clean` : Remove existing environment and reinstall from scratch.
- `--time` : Measure execution time of the cell.

### Notes

- `micromamba` executable is local (`/content/micromamba/bin/micromamba`)
- Only package cache is stored on Drive (`/content/drive/MyDrive/mamba_pkgs`)
- Avoid placing the `micromamba` executable itself on Drive (permission issues may occur).
