# Nonin_PPG_Recorder
This python code lets you dump the raw PPG (Photoplethysmogram) data from Nonin PPG Device (Model - 3017LP, Nonin P/N - 8898-001, Data Format - 7)

Sampling Frequency  - 75 Hz
Data Resolution     - 16-Bit

## Before running the code in Linux

Connect the Nonin device and give the necessary serial port access permission
--> sudo chmod 777 serialport
--> Example : sudo chmod 777 /dev/ttyUSB0

## How to run?

--> ./Nonin_PPG_Recorder.py serialport output_file_name
--> Example : ./Nonin_PPG_Recorder.py /dev/ttyUSB0 dump.csv

Press Ctrl-C to stop data logging into file.


