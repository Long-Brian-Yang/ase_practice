from ase.build import bulk, fcc111
from ase.calculators.vasp import Vasp

# Calculate the surface energy of a Cu(111) surface
bulk_cu = bulk('Cu', 'fcc', a=3.615, cubic=True)
bulk_calc = Vasp(xc='PBE', kpts=(9, 9, 9), encut=400)
bulk_cu.set_calculator(bulk_calc)
bulk_energy = bulk_cu.get_potential_energy()

# Generate a Cu(111) surface
slab = fcc111('Cu', size=(2, 2, 5), vacuum=15.0)
slab_calc = Vasp(xc='PBE', kpts=(5, 5, 1), encut=400)
slab.set_calculator(slab_calc)
slab_energy = slab.get_potential_energy()

# Calculate the surface energy
area = slab.get_cell()[0, 0] * slab.get_cell()[1, 1]  # area of the surface
surface_energy = (slab_energy - 5 * bulk_energy) / (2 * area)
print(f"surface energy: {surface_energy} eV/Å²")
