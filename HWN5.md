# Library settings 
| lib. name | delay model |
|----|----|
| HWN5 | table_lookup |

## Units 
| cap | volt | cur | leak | time | res |
|----|----|----|----|----|----|
| pF | V  | mA | pW | ns | Ohm |

## Voltage terminals 
| vdd | vss | gnd | pwell | nwell |
|----|----|----|----|----|
| VDD | VSS  | gnd | VPW | VNW |

## Operating conditions 
| operationg cond. | temperature | voltage  |
|----|----|----|
| PVT_0P65V_25C | 25.0 | 0.65 |

## Logic threshold 
| input rise | input fall | output rise | output fall |
|----|----|----|----|
| 50.0 | 50.0 | 50.0 | 50.0 |

\newpage 
# Cell settings 
## Cell : INVx1 
### Basics
| name | type | code | area | leak |
|----|----|----|----|----|
| INVx1 | Combinational | INV | 1.0 | 8418.897500 |

### Input pin : A
| direction | related pwr pin | related gnd pin | max trans | cap. |
|----|----|----|----|----|
| input | VDD | VSS | 0.10164 | 0.002717 |

### Output pin : Y
| direction | func | max cap | leak | 
|----|----|----|----|
| output | !A | 0.011469 | 8418.897500 |

#### related pin : A
| related pin | func | max cap |
|----|----|----|
|A|!A | 0.011469 |

| direction | prop min. | prop center | prop max |
|----|----|----|----|
|cell_fall|0.001217 | 0.004497 | 0.024831 |
|cell_rise|0.001200 | 0.003860 | 0.022410 |

| direction | tran min. | tran center | tran max |
|----|----|----|----|
|fall_transition|0.000388 | 0.002660 | 0.015961 |
|rise_transition|0.000363 | 0.002644 | 0.015955 |

| direction | eintl min. | eintl center | eintl max |
|----|----|----|----|
|fall_power|0.000040 | 0.000316 | 0.002959 |
|rise_power|0.000002 | 0.001321 | 0.006962 |


\newpage 
