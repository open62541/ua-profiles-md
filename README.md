# OPC UA Markdown Profiles Generator

This repository contains a generator which is using the OPC UA profiles description and generates a markdown file with the list of supported profiles.

An example output file is contained in this repository: [PROFILES.md](PROFILES.md)

A full list of OPC UA Profiles can be found in Part 7 of the specification.
The required input files for this generater are contained in the official Compliance Test Toolkit (CTT) installation.

`C:\Program Files (x86)\OPC Foundation\UA 1.03\Compliance Test Tool\ServerProjects`
and
`C:\Program Files (x86)\OPC Foundation\UA 1.03\Compliance Test Tool\ClientProjects`


In the CTT you can select a subset of tests which are executed and you get the test results.
Save your project somewhere and you will get two files:

* `selection.xml`
* `results.xml`

These two files are an additional input to the generator to show the test results for each conformance unit.
Based on the containing conformance units, the profiles and facets are also marked with the combined test results.

## How to run

Due to licensing issues, you need to copy some files from your CTT installation into this project.

1. Make sure that you have a valid license of the CTT tools and you installed it on a PC
2. Copy all the folders from `C:\Program Files (x86)\OPC Foundation\UA 1.03\Compliance Test Tool` into the subfolder `CTT` within this project
3. Run the CTT with your own settings and save the project configuration
4. The CTT should give you a `results.xml` and `selection.xml` file.
5. Run the `generate_results_md.py` script and pass the correct path to your results (`--results`) and selection (`--selection`) file.
```bash
python3 generate_results_md.py --results=./example.results.xml --selection=./example.selection.xml PROFILES.md
```
6. Check the output of the script by opening `PROFILES.md` file. You can also paste it into https://jbt.github.io/markdown-editor/
