#!/usr/bin/env pytghon
# -*- coding: utf-8 -*-

import argparse, re, os, shutil, subprocess, sys, inspect, datetime 

import myConditionsAndResults as mcar
import myLibrarySetting as mls 
import myLogicCell as mlc
import myExport as me
import myExportDoc as med
import numpy as np
from char_comb import runCombIn1Out1, runCombIn2Out1, runCombIn3Out1, runCombIn4Out1,  genFileLogic_trial1
from char_seq import runFlop, genFileFlop_trial1
from myFunc import my_exit, startup

def main():
  parser = argparse.ArgumentParser(description='argument')
  parser.add_argument('-b','--batch', type=str, help='inport batch file')
  args = parser.parse_args()
  #print(args.batch)

  targetLib = mls.MyLibrarySetting() 
  #startup()
  #history()

  num_gen_file = 0

# # file open
  with open(args.batch, 'r') as f:
    lines = f.readlines()
    
    for line in lines:
      line = line.strip('\n')
##-- set function : common settings--#
      ## set_lib_name
      if(line.startswith('set_lib_name')):
        targetLib.set_lib_name(line) 

      if(line.startswith('set_dotlib_name')):
        targetLib.set_dotlib_name(line) 

      if(line.startswith('set_doc_name')):
        targetLib.set_doc_name(line)
                
      if(line.startswith('set_verilog_name')):
        targetLib.set_verilog_name(line) 

      ## set_cell_name_suffix
      elif(line.startswith('set_cell_name_suffix')):
        targetLib.set_cell_name_suffix(line) 

      ## set_cell_name_prefix
      elif(line.startswith('set_cell_name_prefix')):
        targetLib.set_cell_name_prefix(line) 

      ## set_voltage_unit
      elif(line.startswith('set_voltage_unit')):
        targetLib.set_voltage_unit(line) 

      ## set_capacitance_unit
      elif(line.startswith('set_capacitance_unit')):
        targetLib.set_capacitance_unit(line) 

      ## set_resistance_unit
      elif(line.startswith('set_resistance_unit')):
        targetLib.set_resistance_unit(line) 

      ## set_time_unit
      elif(line.startswith('set_time_unit')):
        targetLib.set_time_unit(line) 

      ## set_current_unit
      elif(line.startswith('set_current_unit')):
        targetLib.set_current_unit(line) 

      ## set_leakage_power_unit
      elif(line.startswith('set_leakage_power_unit')):
        targetLib.set_leakage_power_unit(line) 

      ## set_energy_unit
      elif(line.startswith('set_energy_unit')):
        targetLib.set_energy_unit(line) 

      ## set_vdd_name
      elif(line.startswith('set_vdd_name')):
        targetLib.set_vdd_name(line) 

      ## set_vss_name
      elif(line.startswith('set_vss_name')):
        #print(line)
        targetLib.set_vss_name(line) 

      ## set_pwell_name
      elif(line.startswith('set_pwell_name')):
        #print(line)
        targetLib.set_pwell_name(line) 

      ## set_nwell_name
      elif(line.startswith('set_nwell_name')):
        targetLib.set_nwell_name(line) 

##-- set function : characterization settings--#
      ## set_process
      elif(line.startswith('set_process')):
        targetLib.set_process(line) 

      ## set_temperature
      elif(line.startswith('set_temperature')):
        targetLib.set_temperature(line) 

      ## set_vdd_voltage
      elif(line.startswith('set_vdd_voltage')):
        targetLib.set_vdd_voltage(line) 

      ## set_vss_voltage
      elif(line.startswith('set_vss_voltage')):
        targetLib.set_vss_voltage(line) 

      ## set_pwell_voltage
      elif(line.startswith('set_pwell_voltage')):
        targetLib.set_pwell_voltage(line) 

      ## set_nwell_voltage
      elif(line.startswith('set_nwell_voltage')):
        targetLib.set_nwell_voltage(line) 

      ## set_logic_threshold_high
      elif(line.startswith('set_logic_threshold_high')):
        targetLib.set_logic_threshold_high(line) 

      ## set_logic_threshold_low
      elif(line.startswith('set_logic_threshold_low')):
        targetLib.set_logic_threshold_low(line) 

      ## set_logic_high_to_low_threshold
      elif(line.startswith('set_logic_high_to_low_threshold')):
        targetLib.set_logic_high_to_low_threshold(line) 

      ## set_logic_low_to_high_threshold
      elif(line.startswith('set_logic_low_to_high_threshold')):
        targetLib.set_logic_low_to_high_threshold(line) 
      ## set_energy_meas_low_threshold
      elif(line.startswith('set_energy_meas_low_threshold')):
        targetLib.set_energy_meas_low_threshold(line) 

      ## set_energy_meas_high_threshold
      elif(line.startswith('set_energy_meas_high_threshold')):
        targetLib.set_energy_meas_high_threshold(line) 

      ## set_energy_meas_time_extent
      elif(line.startswith('set_energy_meas_time_extent')):
        targetLib.set_energy_meas_time_extent(line) 

      ## set_energy_meas_time_extent
      elif(line.startswith('set_operating_conditions')):
        targetLib.set_operating_conditions(line) 

      ## set_load
      elif(line.startswith('set_load')):
        targetLib.set_load(line) 

      ## set_slope
      elif(line.startswith('set_slope')):
        targetLib.set_slope(line) 


##-- set function : characterizer settings--#
      ## set_work_dir
      elif(line.startswith('set_work_dir')):
        targetLib.set_work_dir(line) 

      ## set_tmp_dir
      elif(line.startswith('set_tmp_dir')):
        targetLib.set_tmp_dir(line) 

      ## set_tmp_file
      elif(line.startswith('set_tmp_file')):
        targetLib.set_tmp_file(line) 

      ## set_simulator
      elif(line.startswith('set_simulator')):
        targetLib.set_simulator(line) 

      ## set_runsim_option
      elif(line.startswith('set_run_sim')):
        targetLib.set_run_sim(line) 

      ## set_multithread_option
      elif(line.startswith('set_num_thread')):
        targetLib.set_num_thread(line) 

      ## set_simulator_nice
      elif(line.startswith('set_sim_nice')):
        targetLib.set_sim_nice(line) 

      ## set_supress_message
      elif(line.startswith('set_supress_message')):
        targetLib.set_supress_message(line) 

      ## set_supress_sim_message
      elif(line.startswith('set_supress_sim_message')):
        targetLib.set_supress_sim_message(line) 

      ## set_supress_debug_message
      elif(line.startswith('set_supress_debug_message')):
        targetLib.set_supress_debug_message(line) 

      ## set_compress_result
      elif(line.startswith('set_compress_result')):
        targetLib.set_compress_result(line) 

##-- add function : common for comb. and seq. --#
      ## add_cell
      elif(line.startswith('add_cell')):
        targetCell = mlc.MyLogicCell()
        targetCell.add_cell(line) 
        targetCell.set_supress_message(targetLib) 

      ## add_slope
      elif(line.startswith('add_slope')):
        targetCell.add_slope(targetLib, line) 

      ## add_load
      elif(line.startswith('add_load')):
        targetCell.add_load(targetLib, line) 

      ## add_area
      elif(line.startswith('add_area')):
        targetCell.add_area(line) 

      ## add_netlist
      elif(line.startswith('add_netlist')):
        targetCell.add_netlist(line) 

      ## add_model
      elif(line.startswith('add_model')):
        targetCell.add_model(line) 

      ## add_simulation_timestep
      elif(line.startswith('add_simulation_timestep')):
        targetCell.add_simulation_timestep(line) 

##-- add function : for seq. cell --#
      ## add_flop
      elif(line.startswith('add_flop')):
        targetCell = mlc.MyLogicCell()
        targetCell.add_flop(line) 
        targetCell.set_supress_message(targetLib) 

      ## add_clock_slope
      elif(line.startswith('add_clock_slope')):
        targetCell.add_clock_slope(line) 

      ## add_simulation_setup_auto
      elif(line.startswith('add_simulation_setup_auto')):
        tmp_array = line.split()
        targetCell.add_simulation_setup_lowest('add_simulation_setup_lowest auto '+str(tmp_array[1])) 
        targetCell.add_simulation_setup_highest('add_simulation_setup_highest auto '+str(tmp_array[1])) 
        targetCell.add_simulation_setup_timestep('add_simulation_setup_timestep auto '+str(tmp_array[1])) 

      ## add_simulation_setup_lowest
      elif(line.startswith('add_simulation_setup_lowest')):
        targetCell.add_simulation_setup_lowest(line) 

      ## add_simulation_setup_highest
      elif(line.startswith('add_simulation_setup_highest')):
        targetCell.add_simulation_setup_highest(line) 

      ## add_simulation_setup_timestep
      elif(line.startswith('add_simulation_setup_timestep')):
        targetCell.add_simulation_setup_timestep(line) 

      ## add_simulation_hold_auto
      elif(line.startswith('add_simulation_hold_auto')):
        tmp_array = line.split()
        targetCell.add_simulation_hold_lowest('add_simulation_hold_lowest auto '+str(tmp_array[1])) 
        targetCell.add_simulation_hold_highest('add_simulation_hold_highest auto '+str(tmp_array[1])) 
        targetCell.add_simulation_hold_timestep('add_simulation_hold_timestep auto '+str(tmp_array[1])) 

      ## add_simulation_hold_lowest
      elif(line.startswith('add_simulation_hold_lowest')):
        targetCell.add_simulation_hold_lowest(line) 

      ## add_simulation_hold_highest
      elif(line.startswith('add_simulation_hold_highest')):
        targetCell.add_simulation_hold_highest(line) 

      ## add_simulation_hold_timestep
      elif(line.startswith('add_simulation_hold_timestep')):
        targetCell.add_simulation_hold_timestep(line) 

##-- execution --#
      ## initialize
      elif(line.startswith('create')):
        initializeFiles(targetLib, targetCell) 

      ## create
      elif(line.startswith('characterize')):
        harnessList2 = characterizeFiles(targetLib, targetCell) 
        os.chdir("../")
        #print(len(harnessList))

      ## export
      elif(line.startswith('export')):
        me.exportFiles(targetLib, targetCell, harnessList2) 
        med.exportDoc(targetLib, targetCell, harnessList2) 
        num_gen_file += 1

      ## exit
      elif(line.startswith('quit') or line.startswith('exit')):
        me.exitFiles(targetLib, num_gen_file) 



def initializeFiles(targetLib, targetCell):
  ## initialize working directory
  if (targetLib.runsim.lower() == "true"):
    if os.path.exists(targetLib.work_dir):
      shutil.rmtree(targetLib.work_dir)
    os.mkdir(targetLib.work_dir)
  elif (targetLib.runsim.lower() == "false"):
    print("save past working directory and files\n")
  else:
    print ("illigal setting for set_runsim option: "+targetLib.runsim+"\n")
    my_exit()
  

def characterizeFiles(targetLib, targetCell):
  print ("characterize\n")
  os.chdir(targetLib.work_dir)

  ## Register lut_template
  targetLib.gen_lut_templates(targetCell)
  targetCell.gen_lut_templates()

  ## Branch to each logic function
  if(targetCell.logic == 'INV'):
    print ("INV\n")
    ## [in0, out0]
    expectationList2 = [['01','10'],['10','01']]
    return runCombIn1Out1(targetLib, targetCell, expectationList2,"neg")

  elif(targetCell.logic == 'BUF'):
    print ("BUF\n")
    ## [in0, out0]
    expectationList2 = [['01','01'],['10','10']]
    return runCombIn1Out1(targetLib, targetCell, expectationList2,"pos")

  elif(targetCell.logic == 'DEL'):
    print ("DEL\n")
    ## [in0, out0]
    expectationList2 = [['01','01'],['10','10']]
    return runCombIn1Out1(targetLib, targetCell, expectationList2,"pos")

  elif(targetCell.logic == 'AND2'):
    print ("AND2\n")
    ## [in0, in1, out0]
    expectationList2 = [['01','1','01'],['10','1','10'],['1','01','01'],['1','10','10']]
    return runCombIn2Out1(targetLib, targetCell, expectationList2,"pos")

  elif(targetCell.logic == 'AND3'):
    print ("AND3\n")
    ## [in0, in1, in2, in3, out0]
    expectationList2 = [['01','1','1','01'],['10','1','1','10'],\
                        ['1','01','1','01'],['1','10','1','10'],\
                        ['1','1','01','01'],['1','1','10','10']]
    return runCombIn3Out1(targetLib, targetCell, expectationList2,"pos")

  elif(targetCell.logic == 'AND4'):
    print ("AND4\n")
    ## [in0, in1, in2, in3,  out0]
    expectationList2 = [['01','1','1','1','01'],['10','1','1','1','10'],\
                        ['1','01','1','1','01'],['1','10','1','1','10'],\
                        ['1','1','01','1','01'],['1','1','10','1','10'],\
                        ['1','1','1','01','01'],['1','1','1','10','10']]
    return runCombIn4Out1(targetLib, targetCell, expectationList2,"pos")
  
  elif(targetCell.logic == 'OR2'):
    print ("OR2\n")
    ## [in0, in1, out0]
    expectationList2 = [['01','0','01'],['10','0','10'],['0','01','01'],['0','10','10']]
    return runCombIn2Out1(targetLib, targetCell, expectationList2,"pos")

  elif(targetCell.logic == 'OR3'):
    print ("OR3\n")
    ## [in0, in1, in2, out0]
    expectationList2 = [['01','0','0','01'],['10','0','0','10'],\
                        ['0','01','0','01'],['0','10','0','10'],\
                        ['0','0','01','01'],['0','0','10','10']]
    return runCombIn3Out1(targetLib, targetCell, expectationList2,"pos")

  elif(targetCell.logic == 'OR4'):
    print ("OR4\n")
    ## [in0, in1, in2, in3, out0]
    expectationList2 = [['01','0','0','0','01'],['10','0','0','0','10'],\
                        ['0','01','0','0','01'],['0','10','0','0','10'],\
                        ['0','0','01','0','01'],['0','0','10','0','10'],\
                        ['0','0','0','01','01'],['0','0','0','10','10']]
    return runCombIn4Out1(targetLib, targetCell, expectationList2,"pos")

  elif(targetCell.logic == 'NAND2'):
    print ("NAND2\n")
    ## [in0, in1, out0]
    expectationList2 = [['01','1','10'],\
                        ['10','1','01'],\
                        ['1','01','10'],\
                        ['1','10','01']]
    return runCombIn2Out1(targetLib, targetCell, expectationList2,"neg")

  elif(targetCell.logic == 'NAND3'):
    print ("NAND3\n")
    ## [in0, in1, in2, out0]
    expectationList2 = [['01','1','1','10'],['10','1','1','01'],\
                        ['1','01','1','10'],['1','10','1','01'],\
                        ['1','1','01','10'],['1','1','10','01']]
    return runCombIn3Out1(targetLib, targetCell, expectationList2,"neg")

  elif(targetCell.logic == 'NAND4'):
    print ("NAND4\n")
    ## [in0, in1, in2, out0]
    expectationList2 = [['01','1','1','1','10'],['10','1','1','1','01'],\
                        ['1','01','1','1','10'],['1','10','1','1','01'],\
                        ['1','1','01','1','10'],['1','1','10','1','01'],\
                        ['1','1','1','01','10'],['1','1','1','10','01']]
    return runCombIn4Out1(targetLib, targetCell, expectationList2,"neg")

  elif(targetCell.logic == 'NOR2'):
    print ("NOR2\n")
    ## [in0, in1, out0]
    expectationList2 = [['01','0','10'],['10','0','01'],['0','01','10'],['0','10','01']]
    return runCombIn2Out1(targetLib, targetCell, expectationList2,"neg")

  elif(targetCell.logic == 'NOR3'):
    print ("NOR3\n")
    ## [in0, in1, in2, out0]
    expectationList2 = [['01','0','0','10'],['10','0','0','01'],\
                        ['0','01','0','10'],['0','10','0','01'],\
                        ['0','0','01','10'],['0','0','10','01']]
    return runCombIn3Out1(targetLib, targetCell, expectationList2,"neg")

  elif(targetCell.logic == 'NOR4'):
    print ("NOR4\n")
    ## [in0, in1, in2, in3, out0]
    expectationList2 = [['01','0','0','0','10'],['10','0','0','0','01'],\
                        ['0','01','0','0','10'],['0','10','0','0','01'],\
                        ['0','0','01','0','10'],['0','0','10','0','01'],\
                        ['0','0','0','01','10'],['0','0','0','10','01']]
    return runCombIn4Out1(targetLib, targetCell, expectationList2,"neg")

  elif(targetCell.logic == 'AO21'):
    print ("AO21\n")
    ## [in0, in1, out0]
    expectationList2 = [['10','1','0','10'],['01','1','0','01'],\
                        ['1','10','0','10'],['1','01','0','01'],\
                        ['0','0','10','10'],['0','0','01','01']]
    return runCombIn3Out1(targetLib, targetCell, expectationList2,"pos")

  elif(targetCell.logic == 'AO22'):
    print ("AO22\n")
    ## [in0, in1, out0]
    expectationList2 = [['10','1','0','0','10'],['01','1','0','0','01'],\
                        ['1','10','0','0','10'],['1','01','0','0','01'],\
                        ['0','0','10','1','10'],['0','0','01','1','01'],\
                        ['0','0','1','10','10'],['0','0','1','01','01']]
    return runCombIn4Out1(targetLib, targetCell, expectationList2,"pos")

  elif(targetCell.logic == 'OA21'):
    print ("OA21\n")
    ## [in0, in1, out0]
    expectationList2 = [['10','0','1','10'],['01','0','1','01'],\
                        ['0','10','1','10'],['0','01','1','01'],\
                        ['0','1','10','10'],['0','1','01','01']]
    return runCombIn3Out1(targetLib, targetCell, expectationList2,"pos")

  elif(targetCell.logic == 'OA22'):
    print ("OA22\n")
    ## [in0, in1, out0]
    expectationList2 = [['10','1','0','1','10'],['01','1','0','1','01'],\
                        ['0','10','0','1','10'],['0','01','0','1','01'],\
                        ['0','1','10','0','10'],['0','1','01','0','01'],\
                        ['0','1','0','10','10'],['0','1','0','10','01']]
    return runCombIn4Out1(targetLib, targetCell, expectationList2,"pos")

  elif(targetCell.logic == 'AOI21'):
    print ("AOI21\n")
    ## [in0, in1, out0]
    expectationList2 = [['10','1','0','01'],['01','1','0','10'],\
                        ['1','10','0','01'],['1','01','0','10'],\
                        ['0','0','10','01'],['0','0','01','10']]
    return runCombIn3Out1(targetLib, targetCell, expectationList2,"neg")

  elif(targetCell.logic == 'AOI22'):
    print ("AOI22\n")
    ## [in0, in1, out0]
    expectationList2 = [['10','1','0','0','01'],['01','1','0','0','10'],\
                        ['1','10','0','0','01'],['1','01','0','0','10'],\
                        ['0','0','10','1','01'],['0','0','01','1','10'],\
                        ['0','0','1','10','01'],['0','0','1','01','10']]
    return runCombIn4Out1(targetLib, targetCell, expectationList2,"neg")

  elif(targetCell.logic == 'OAI21'):
    print ("OAI21\n")
    ## [in0, in1, out0]
    expectationList2 = [['10','0','1','01'],['01','0','1','10'],\
                        ['0','10','1','01'],['0','01','1','10'],\
                        ['0','1','10','01'],['0','1','01','10']]
    return runCombIn3Out1(targetLib, targetCell, expectationList2,"neg")

  elif(targetCell.logic == 'OAI22'):
    print ("OAI22\n")
    ## [in0, in1, in2, out0]
    expectationList2 = [['10','0','1','1','01'],['01','0','1','1','10'],\
                        ['0','10','1','1','01'],['0','01','1','1','10'],\
                        ['1','1','10','0','01'],['1','1','01','0','10'],\
                        ['1','1','0','10','01'],['1','1','0','01','10']]
    return runCombIn4Out1(targetLib, targetCell, expectationList2,"neg")

  elif(targetCell.logic == 'XOR2'):
    print ("XOR2\n")
    ## [in0, in1, out0]
    expectationList2 = [['01','0','01'],['10','0','10'],\
                        ['01','1','10'],['10','1','01'],\
                        ['0','01','01'],['0','10','10'],\
                        ['1','01','10'],['1','10','01']]
    return runCombIn2Out1(targetLib, targetCell, expectationList2,"pos")

  elif(targetCell.logic == 'XNOR2'):
    print ("XNOR2\n")
    ## [in0, in1, out0]
    expectationList2 = [['01','0','10'],['10','0','01'],\
                        ['01','1','01'],['10','1','10'],\
                        ['0','01','10'],['0','10','01'],\
                        ['1','01','01'],['1','10','10']]
    return runCombIn2Out1(targetLib, targetCell, expectationList2,"pos")

  elif(targetCell.logic == 'SEL2'):
    print ("SEL2\n")
    ## [in0, in1, sel, out]
    expectationList2 = [['01','0','0','01'],['10','0','0','10'],\
                        ['0','01','1','01'],['0','10','1','10'],\
                        ['1','0','01','10'],['1','0','10','01'],\
                        ['0','1','01','01'],['0','1','10','10']]
    return runCombIn3Out1(targetLib, targetCell, expectationList2,"pos")


  ## Branch to sequencial logics
  elif(targetCell.logic == 'DFF_PCPU'):
    print ("DFF, positive clock, positive unate\n")
    ## D1 & C01 -> Q01
    ## D0 & C01 -> Q10
    ##                   [D,   C,     Q]
    expectationList2 = [['01','0101', '01'], \
                        ['10','0101', '10']] 
    ## run spice deck for flop
    return runFlop(targetLib, targetCell, expectationList2)

  elif(targetCell.logic == 'DFF_PCNU'):
    print ("DFF, positive clock, negative unate\n")
    ## D1 & C01 -> Q01
    ## D0 & C01 -> Q10
    ##                   [D,   C,     Q]
    expectationList2 = [['01','0101', '10'], \
                        ['10','0101', '01']] 
    ## run spice deck for flop
    return runFlop(targetLib, targetCell, expectationList2)

  elif(targetCell.logic == 'DFF_NCPU'):
    print ("DFF, negative clock, positive unate\n")
    ## D1 & C01 -> Q01
    ## D0 & C01 -> Q10
    ##                   [D,   C,     Q]
    expectationList2 = [['01','1010', '01'], \
                        ['10','1010', '10']] 
    ## run spice deck for flop
    return runFlop(targetLib, targetCell, expectationList2)

  elif(targetCell.logic == 'DFF_NCNU'):
    print ("DFF, negative clock, negative unate\n")
    ## D1 & C01 -> Q01
    ## D0 & C01 -> Q10
    ##                   [D,   C,     Q]
    expectationList2 = [['01','1010', '10'], \
                        ['10','1010', '01']] 
    ## run spice deck for flop
    return runFlop(targetLib, targetCell, expectationList2)

  elif(targetCell.logic == 'DFF_PCPU_NR'):
    print ("DFF, positive clock, positive unate, async neg-reset\n")
    ## D1 & C01 -> Q01
    ## D0 & C01 -> Q10
    ## R10      -> Q10
    ##                   [D,   C,    R,    Q]
    expectationList2 = [['01','0101', '1', '01'], \
                        ['10','0101', '1', '10'], \
                        [ '1', '0101','10', '10']]
    ## run spice deck for flop
    return runFlop(targetLib, targetCell, expectationList2)

  ## Not checked yet 24/05/15
  elif(targetCell.logic == 'DFF_PCPU_PR'):
    print ("DFF, positive clock, positive unate, async pos-reset\n")
    ## D1 & C01 -> Q01
    ## D0 & C01 -> Q10
    ## R01      -> Q10
    ##                   [D,   C,    R,    Q]
    expectationList2 = [['01','0101', '0', '01'], \
                        ['10','0101', '0', '10'], \
                        [ '1', '0101','01', '10']]
    ## run spice deck for flop
    return runFlop(targetLib, targetCell, expectationList2)

  elif(targetCell.logic == 'DFF_PCPU_NS'):
    print ("DFF, positive clock, positive unate, async neg-set\n")
    ## D1 & C01 -> Q01
    ## D0 & C01 -> Q10
    ## S10      -> Q10
    ##                   [D,   C,    S,    Q]
    expectationList2 = [['01','0101', '1', '01'], \
                        ['10','0101', '1', '10'], \
                        [ '0', '0101','10', '01']]
    ## run spice deck for flop
    return runFlop(targetLib, targetCell, expectationList2)

  ## Not checked yet 24/05/15
  elif(targetCell.logic == 'DFF_PCPU_PS'):
    print ("DFF, positive clock, positive unate, async pos-set\n")
    ## D1 & C01 -> Q01
    ## D0 & C01 -> Q10
    ## S01      -> Q10
    ##                   [D,   C,    S,    Q]
    expectationList2 = [['01','0101', '0', '01'], \
                        ['10','0101', '0', '10'], \
                        [ '0', '0101','01', '01']]
    ## run spice deck for flop
    return runFlop(targetLib, targetCell, expectationList2)

  elif(targetCell.logic == 'DFF_PCPU_NRNS'):
    print ("DFF, positive clock, positive unate, async neg-reset, async neg-set\n")
    ## D1 & C01 -> Q01 QN10
    ## D0 & C01 -> Q10 QN01
    ## S10      -> Q01 QN10
    ## R10      -> Q10 QN01
    ##                   [D,   C,  S,   R,    Q]
    expectationList2 = [['01','0101', '1', '1', '01'], \
                        ['10','0101', '1', '1', '10'], \
                        ['0', '0101','10', '1', '01'], \
                        ['1', '0101', '1','10', '10']]

    ## run spice deck for flop
    return runFlop(targetLib, targetCell, expectationList2)


  elif(targetCell.logic == 'DFF_NCPU_NRNS'):
    print ("DFF, negative clock, positive unate, async neg-reset, async neg-set\n")
    ## D1 & C01 -> Q01 QN10
    ## D0 & C01 -> Q10 QN01
    ## S10      -> Q01 QN10
    ## R10      -> Q10 QN01
    ##                   [D,   C,  S,   R,    Q]
    expectationList2 = [['01','1010','1',  '1', '01'], \
                        ['10','1010','1',  '1', '10'], \
                        ['0' ,'1010','10', '1', '01'], \
                        ['1' ,'1010', '1','10', '10']]

    ## run spice deck for flop
    return runFlop(targetLib, targetCell, expectationList2)

  else:
    print ("Target logic:"+targetCell.logic+" is not registered for characterization!\n")
    print ("Add characterization function for this program! -> die\n")
    my_exit()



if __name__ == '__main__':
 main()

