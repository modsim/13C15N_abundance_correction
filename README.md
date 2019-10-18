# 13C15N_abundance_correction
Correction method as described in https://doi.org/10.1021/acs.analchem.9b01788

# Preparation

* have perl and python installed an running
* adjust the data in `data_template.txt` and save them as `measured_data.txt` (or any other name. Adjust accordingly in later steps)
* complete the model in `notation.fml` (can also be done afterwards)
* clone the repository recursively (to include ICT) `git clone --recurse-submodules git@github.com:modsim/13C15N_abundance_correction.git`

# Correction Workflow

* run ICT on the data: `./externals/isotope_correction_toolbox/ict.pl -c chemdata.txt -m measured_data.txt -o corrected_data.txt`
* watch for errors and fix them
* Optional: in the `ict2fluxml.py` file adjust the default standard deviation. By default it is set to 0.01
* convert the ICT output to `FluxML`: `./ict2fluxml.py corrected_data.txt`
* copy and past the output to the `notation.fml` file (inside the `<data>` tag)
