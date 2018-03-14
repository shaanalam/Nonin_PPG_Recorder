# Nonin_PPG_Recorder
This python code lets you dump the raw PPG (Photoplethysmogram) data from Nonin PPG Device. <br />
<br />
Model - 3017LP <br />
Nonin P/N - 8898-001 <br />
Data Format - 7 <br />
<br />
Sampling Frequency  - 75 Hz <br />
Data Resolution     - 16-Bit <br />

## Before running the code in Linux
<br />
Connect the Nonin device and give the necessary serial port access permission <br />
--> sudo chmod 777 serialport <br />
--> Example : sudo chmod 777 /dev/ttyUSB0 <br />

## How to run?
<br />
--> ./Nonin_PPG_Recorder.py serialport output_file_name <br />
--> Example : ./Nonin_PPG_Recorder.py /dev/ttyUSB0 dump.csv <br />
<br />
Press Ctrl-C to stop data logging into file.


