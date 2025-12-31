import os, subprocess, sys

REPO_URL = "https://github.com/seoultechpse/fenicsx-colab.git"
REPO_DIR = "/content/fenicsx-colab"
INSTALL = "setup/install_fenicsx.sh"
MAGIC = "magic/fenicsx_magic.py"

def run(cmd, cwd=None):
    print("$", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)

# --------------------------------------------------
# Drive
# --------------------------------------------------
if not os.path.exists("/content/drive"):
    print("❌ Google Drive not mounted")
    sys.exit(1)

# --------------------------------------------------
# Clone
# --------------------------------------------------
if not os.path.exists(REPO_DIR):
    run(["git", "clone", REPO_URL, REPO_DIR])
else:
    print("📦 Repo exists")

# --------------------------------------------------
# Install
# --------------------------------------------------
opts = sys.argv[1:]   # e.g. --force / --clean
run(["bash", INSTALL, *opts], cwd=REPO_DIR)

# --------------------------------------------------
# Magic
# --------------------------------------------------
with open(os.path.join(REPO_DIR, MAGIC)) as f:
    exec(f.read(), globals())

print("🎉 fenicsx ready")

print("\n🧪 Running fenicsx self-test...")

subprocess.run(
    [
        "micromamba", "run", "-n", "fenicsx",
        "mpiexec", "-n", "4", "python",
        str( "tests" / "test_fenicsx_basic.py")
    ],
    check=True
)

print("🧪 fenicsx self-test passed")