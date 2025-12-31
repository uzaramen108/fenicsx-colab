from mpi4py import MPI
import dolfinx
from dolfinx.mesh import create_unit_interval

comm = MPI.COMM_WORLD

mesh = create_unit_interval(comm, 8)

if comm.rank == 0:
    print("  ✅ dolfinx import OK")
    print("  ✅ MPI size   :", comm.size)
    print("  ✅ Mesh cells :", mesh.topology.index_map(1).size_global)