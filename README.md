# 13C15N_abundance_correction
Correction method as described in https://doi.org/10.1021/acs.analchem.9b01788

This method relies on the *Isotope correction Toolbox* as described in [this paper by Jungreuthmayer et al.](https://doi.org/10.1093/bioinformatics/btv514)

# Preparation

* have perl and python installed an running
    * for perl setup we refer to [ict](https://github.com/jungreuc/isotope_correction_toolbox/blob/master/doc/ict.pdf)
    * python version 3 with the modules argparse, numpy and csv is needed
* adjust the data in `data_template.txt` and save them as `measured_data.txt` (or any other name. Adjust accordingly in later steps)
* complete the model in `notation.fml` (can also be done afterwards)
    * In case of questions regarding the atom numbering refer to the images inside the InChI folder
* clone the repository recursively (to include ICT) `git clone --recurse-submodules git@github.com:modsim/13C15N_abundance_correction.git`

# Correction Workflow

* run ICT on the data: `./externals/isotope_correction_toolbox/ict.pl -c chemdata.txt -m measured_data.txt -o corrected_data.txt`
    * watch for errors and fix them
* Optional: in the `ict2fluxml.py` file adjust the default standard deviation. By default it is set to 0.01
* convert the ICT output to [FluxML](https://github.com/modsim/FluxML): `./ict2fluxml.py corrected_data.txt`
* copy and past the output to the `notation.fml` file (inside the `<data>` tag)
* execute your regular flux estimation workflow
