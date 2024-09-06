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
## Cell : DFFHQx1 
### Basics
| name | type | code | area | leak |
|----|----|----|----|----|
| DFFHQx1 | Sequential | DFF_PCPU | 1.0 | 5168.623200 |

### Clock pin : CLK
| direction | related pwr pin | related gnd pin | max trans | cap. |
|----|----|----|----|----|
| input | VDD | VSS | 0.025116 | 0.000274 |

### Input pin : D
| direction | related pwr pin | related gnd pin | max trans | cap. |
|----|----|----|----|----|
| input | VDD | VSS | 0.025116 | 0.000028 |

| direction | setup min. | setup center | setup max |
|----|----|----|----|
|rise_constraint|0.012378 | 0.012378 | 0.012378 |
|fall_constraint|0.096520 | 0.096520 | 0.096520 |

| direction | hold min. | hold center | hold max |
|----|----|----|----|
|rise_constraint|-0.005340 | -0.002720 | -0.001100 |
|fall_constraint|-0.013199 | -0.010579 | -0.007960 |

### Output pin : Q
| direction | func | max cap | leak | 
|----|----|----|----|
| output | IQ | 0.002835 | 5168.623200 |

#### related pin : CLK
| related pin | func | max cap |
|----|----|----|
| CLK | IQ | 0.002835 |

| direction | prop min. | prop center | prop max |
|----|----|----|----|
|cell_rise|0.016160 | 0.018745 | 0.023034 |
|cell_fall|0.157598 | 0.169618 | 0.180776 |

| direction | tran min. | tran center | tran max |
|----|----|----|----|
|rise_transition|0.001951 | 0.003509 | 0.006777 |
|fall_transition|0.008462 | 0.010461 | 0.013875 |

| direction | eintl min. | eintl center | eintl max |
|----|----|----|----|
|rise_power|0.001374 | 0.001699 | 0.002320 |
|fall_power|0.001518 | 0.001550 | 0.001551 |

| direction | ein min. | ein center | ein max |
|----|----|----|----|
|rise_power|0.000013 | 0.000013 | 0.000021 |

\newpage 
