
"""
The version 1 consists of two triple-channel SPDT switches (ADG633),
one 16-channel multiplexer (ADG1406), and a Raspberry pi pico 
to controll the chips.
The followings are describing the pin configurations for KU setup.
"""

# RPI pico pin configurations
"""
Pin number N denotes GPN pin (eg. 16->GP16).
|            | EN | A0 | A1 | A2 | A3 |
| ---------- | -- | -- | -- | -- | -- |
| ADG633  #1 |  0 |  1 |  2 |  3 |    | 
| ADG633  #2 |  4 |  5 |  6 |  7 |    | 
| ADG1406 #1 | 16 | 17 | 18 | 19 | 20 |  
"""

pin_ADG633_1 = [0, 1, 2, 3]
pin_ADG633_2 = [4, 5, 6, 7]
pin_ADG1406_1 = [16, 17, 18, 19, 20]

"""
# signal lines
* SN are channels on ADG1406
* PN are probe #N

## Between the chips
|            | S1A | S1B | S2A | S2B | S3A | S3B | D1 | D2 | D3 |
| ---------- | --- | --- | --- | --- | --- | --- | -- | -- | -- |
| ADG633  #1 |  S1 | GND |  S2 | GND |  S3 | GND | P1 | P4 |    |
| ADG633  #2 |  S4 | GND |  S5 | GND |  S6 | GND | P3 | P6 | P5 |

## Probe to sensor (Korea Univ.)
|      | Contact     |
| ---- | ----------- | 
| P1   | pad 1       |
| P2   | HV (bottom) |
| P3   | pad 3       |
| P4   | pad 2       |
| P5   | Guard ring  |
| P6   | pad 4       |

## Full connection path
 * Note that id numbers start from 1.
pad1 -> P1 -> #1 S1A -> S1
pad2 -> P4 -> #1 S2A -> S2
pad3 -> P3 -> #2 S1A -> S4
pad4 -> P6 -> #2 S2A -> S5
GDR  -> P5 -> #2 S3A -> S6
"""

# swithch = ij, where i is the ADG633 ID and j is switch id on ADG633

NC = -1
GDR = 5

probe1path = {"probe":1, "switch":11, "mux":1, "pad":1}
probe2path = {"probe":2, "switch":NC, "mux":NC, "pad":NC}
probe3path = {"probe":3, "switch":21, "mux":4, "pad":3}
probe4path = {"probe":4, "switch":12, "mux":2, "pad":2}
probe5path = {"probe":5, "switch":23, "mux":6, "pad":GDR}
probe6path = {"probe":6, "switch":22, "mux":5, "pad":4}
dummy      = {"probe":-1,"switch":13, "mux":3, "pad":NC}

probe_path = [probe1path, probe2path, probe3path, probe4path, probe5path, probe6path, dummy]


