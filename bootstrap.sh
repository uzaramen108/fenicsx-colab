#!/usr/bin/env bash
set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "${REPO_DIR}"

# --------------------------------------------------
# 1. Install FEniCSx (Drive optional)
# --------------------------------------------------
bash setup/install_fenicsx.sh "$@"

# --------------------------------------------------
# 2. Register %%fenicsx magic in THIS kernel
# --------------------------------------------------
python setup_fenicsx.py

echo "🎉 FEniCSx bootstrap complete"