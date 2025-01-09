from rdkit import Chem
from mordred import HydrogenBond, SLogP, Polarizability, Weight, Lipinski

HA = HydrogenBond.HBondAcceptor()
HD = HydrogenBond.HBondDonor()
logP = SLogP.SLogP()
PoA = Polarizability.APol()
PoB = Polarizability.BPol()
M = Weight.Weight()
L = Lipinski.Lipinski()

związki = ['Cl[Pt@SP1--](Cl)([NH3+])[NH3+]', 
'[NH3+][Pt--]1([NH3+])OC(=O)C2(CCC2)C(=O)O1', 
'O=C1O[Pt--]2([NH2+][C@@H]3CCCC[C@@H]3[NH2+]2)OC1=O', 
'[NH3+][Pt--]1([NH3+])OCC(=O)O1', 
'C[C@H]1CC(=O)O[Pt--]2([NH2+]CC3CCC3C[NH2+]2)O1', 
'CC(C)C1OC2C[NH2+][Pt--]3([NH2+]CC2O1)OC(=O)CC(=O)O3', 
'CC(=O)O[Pt@OH2--]([NH3+])(Cl)(Cl)([NH2+]C1CCCCC1)OC(C)=O',
'Clc1c[nH]c2[n+](cccc12)[Pt@SP1--](Cl)(Cl)[n+]1cccc2c(Cl)c[nH]c12', 
'Cl[Pt@SP1--](Cl)([n+]1cccc2c(I)c[nH]c12)[n+]1cccc2c(I)c[nH]c12', 
'Cl[Pt@SP1--](Cl)([n+]1cc(Br)cc2cc[nH]c12)[n+]1cc(Br)cc2cc[nH]c12', 
'Clc1c[nH]c2[n+](cccc12)[Pt--]1(OC(=O)C(=O)O1)[n+]1cccc2c(Cl)c[nH]c12', 
'Ic1c[nH]c2[n+](cccc12)[Pt--]1(OC(=O)C(=O)O1)[n+]1cccc2c(I)c[nH]c12', 
'Brc1c[n+](c2[nH]ccc2c1)[Pt--]1(OC(=O)C(=O)O1)[n+]1cc(Br)cc2cc[nH]c12', 
'CC(C)Oc1cccc(OC(C)C)c1[N+]1=CC=[N+](c2c(OC(C)C)cccc2OC(C)C)[Pt--]1(Cl)Cl', 
'COC1=[N+](c2c(OC)cc(OC)cc2OC)[Pt--](Cl)(Cl)[N+](=C1OC)c1c(OC)cc(OC)cc1OC', 
'COC1=[N+](c2c(OC(C)C)cccc2OC(C)C)[Pt--](Cl)(Cl)[N+](=C1OC)c1c(OC(C)C)cccc1OC(C)C', 
'CC(=C)[C@@H]1CC[C@@]2(CC[C@]3(C)C(CCC4[C@@]5(C)CC[C@H](OC(C)=O)C(C)(C)C5CC[C@@]34C)C12)C(=O)NCC[NH+]1CC[NH2+][Pt--]1(Cl)[S+](C)(C)=O', 
'CC(=C)[C@@H]1CC[C@@]2(CC[C@]3(C)C(CCC4[C@@]5(C)CC[C@H](OC(C)=O)C(C)(C)C5CC[C@@]34C)C12)C(=O)NCC[NH+]1CC[NH2+][Pt--]1(Cl)Cl', 
'C[S+](C)(=O)[Pt--]1(Cl)[NH2+]CC(O)C[NH2+]1', 
'OC1C[NH2+][Pt--](Cl)(Cl)[NH2+]C1', 
'ClCN1C=[N+](C2=C1C=CC=C2)[Pt@SP1--](Cl)(Cl)[N+]1=CN(CCl)C2=C1C=CC=C2', 
'CC(=O)OCN1C=[N+](C2=C1C=CC=C2)[Pt@SP1--](Cl)(Cl)[N+]1=CN(COC(C)=O)C2=C1C=CC=C2', 
'OCCN1C=[N+](C2=C1C=CC=C2)[Pt@SP1--](Cl)(Cl)[N+]1=CN(CCO)C2=C1C=CC=C2', 
'CC1=[N+](C2=C(C=CC=C2)N1CCl)[Pt@SP1--](Cl)(Cl)[N+]1=C(C)N(CCl)C2=C1C=CC=C2', 
'CC(=O)OCN1C(C)=[N+](C2=C1C=CC=C2)[Pt@SP1--](Cl)(Cl)[N+]1=C(C)N(COC(C)=O)C2=C1C=CC=C2', 
'CC1=[N+](C2=C(C=CC=C2)N1CCO)[Pt@SP1--](Cl)(Cl)[N+]1=C(C)N(CCO)C2=C1C=CC=C2']

plik = open(r'C:\Users\admin\Documents\pajton\.pum\pum_mordred.csv', 'w')
plik.write('SMILES,hydrogen_bond_acceptor,hydrogen_bond_donor,SLogP,atomic_polarizability,bond_polarizability,weight,Lipinski\n')
for mol in związki:
    plik.write(mol)
    print(mol)
    m = Chem.MolFromSmiles(mol, sanitize=True)
    for op in (HA, HD, logP, PoA, PoB, M, L):
        w = op(m)
        print(w)
        plik.write(f',{w}')
    plik.write('\n')
    print()
plik.close()
