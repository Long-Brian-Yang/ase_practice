from ase.build import bulk, surface
from ase.io.vasp import write_vasp
Pt_bulk = bulk('Pt', 'fcc', a=3.98, cubic=True)
Pt_slab = surface(Pt_bulk, (1, 0, 0), layers=2, vacuum=10)
write_vasp('Pt100.vasp', Pt_slab,direct=True,vasp5=True)