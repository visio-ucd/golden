Testgen.py/ Testgen_normal.py
---------
### 1. Introduction  
The script is used to generate testbench and reference files for the [`bfloat16_adder`](https://github.com/athlaing/CNN/tree/verilog_dev/verilog/adder_comb) and [`mult_comb`.](https://github.com/athlaing/CNN/tree/verilog_dev/verilog/multiplier_comb)
The generated testbenches should be use in conjunction with the respective verilog module for simulation.
The reference csv files is used to compare and verify the correctness of add/mult modules.

### 2. Usage
`Python testgen.py [-n number_of_tests] [-m True/False] [-s TB_stepsize] [-a True/False] [-m True/False]`  

Options:
- -n --range 
  * Specifies the range of tests to be tested. The total cases generated will be range^2. Default value is 2.
- -r --random
  * if True, randomizes the test cases. Default is True.
- -s --stepsize 
  * Specifies the stepsize for simulation of the testbench file. Default is 20.
- -a --adder 
  * If True, testgen will generate adder testbench and reference files. Default is True.
- -m --mult 
   * If True, testgen will generate mult testbench and reference files. Default is True.
   
### 3. Important Details
Running `testgen.py` will generate files at the same directory as the script.   
Running generated testbench files (`mult_comb.vt` , `add_comb.vt`) til finish will produce an output (`*_out.csv`) file at the simulation directory. 
   
Checker.py
---
###1. Introduction   
The script diffs `add_out.csv` with `add_ref.csv` and `mult_out.csv` with `mult_ref.csv` to find difference in the two files.
The is use to check whether the add/mult modules produce the correct outputs. 

### 2. Usage
`Python check.py [-w True/False] [-a True/False] [-m True/False]`   
- -w --write
  - If True, writes output to a `diff_mult.txt` and/or `diff_add.txt` at the same directory as the script. Default is True.
- -a --adder
  - If True, checks adder output to adder reference. Default is False.
- -m --mult 
  - If True, checks mult output to mult reference. Default is False. 
  
### 3. Important Details
Both the `*_out.csv` and `*_ref.csv` must at the same directory as `checker.py`. See Testgen above to find out where `*_out.csv` is located initially.    

Testgen_normal.py will only generate normal numbers, whereas testgen.py will include denormal number.
