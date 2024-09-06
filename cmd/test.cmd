# common settings for library
set_lib_name         OSU350_5P0V_25C
set_dotlib_name      OSU350_5P0V_25C.lib
set_doc_name      OSU350_5P0V_25C.md
set_verilog_name     OSU350.v
set_cell_name_suffix OSU350_
set_cell_name_prefix _V1
set_voltage_unit V
set_capacitance_unit pf
set_resistance_unit kohm
set_current_unit mA
set_leakage_power_unit pW 
set_energy_unit fJ 
set_time_unit ns
set_vdd_name VDD
set_vss_name VSS
set_pwell_name VPW
set_nwell_name VNW
# characterization conditions 
set_process 1.0
set_temperature 25.0
set_vdd_voltage 0.65
set_vss_voltage 0
set_pwell_voltage 0
set_nwell_voltage 0.65
set_logic_threshold_high 0.7
set_logic_threshold_low 0.3
set_logic_high_to_low_threshold 0.5
set_logic_low_to_high_threshold 0.5
set_energy_meas_low_threshold 0.01
set_energy_meas_high_threshold 0.99
set_energy_meas_time_extent 10
set_operating_conditions PVT_0P65V_25C
set_slope slope1 {0.012376 0.025116} 
set_load  load1 {0.001396 0.002835} 
# characterizer settings 
set_work_dir work
set_tmp_dir work
set_tmp_file _tmp__
set_simulator Xyce
set_run_sim true
set_mt_sim true
set_sim_nice 19
set_compress_result False
set_supress_message true
set_supress_sim_message true
set_supress_debug_message true
# initialize workspace
initialize

## add circuit
add_cell -n INVx1 -l INV -i A -o Y -f Y=!A 
add_slope slope1 
add_load  load1 
add_area 1
add_netlist HUAZI/INVx1.cdl
add_model HUAZI/MODEL/model_TT.sp
add_simulation_timestep auto slope1

characterize
export



exit

