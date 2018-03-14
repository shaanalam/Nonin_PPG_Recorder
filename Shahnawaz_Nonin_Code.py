#!/usr/bin/env python
import sys, serial, argparse, csv, time
import datetime

class LiveDataPoint(object):
    def __init__(self, data): 
	self.pulseWaveform=data

    def getBytes(self):
        result = [0]

        result[0] = self.pulseWaveform
        return result

    @staticmethod
    def getCsvColumns():
        return []

    def getCsvData(self):
	#print self.pulseWaveform
	return [self.pulseWaveform]



class Nonin(object):
    def __init__(self, port):
        self.port = port
        self.conn = None

    def isConnected(self):
        return type(self.conn) is serial.Serial and self.conn.isOpen()

    def connect(self):
        if self.conn is None:
            self.conn = serial.Serial(port = self.port,
                                      baudrate = 9600,
                                      parity = serial.PARITY_NONE,
                                      stopbits = serial.STOPBITS_ONE,
                                      bytesize = serial.EIGHTBITS)
        elif not self.isConnected():
            self.conn.open()

    def disconnect(self):
        if self.isConnected():
            self.conn.close()

    def getByte(self):
        char = self.conn.read()
        if len(char) == 0:
            return None
        else:
            return ord(char)

    def getLiveData(self):
        try:
            self.connect()
	    N=20
	    temp=0

            while True:
	        #Pattern Recognition
                byte1 = self.getByte() & 0xff
                if byte1 is None:
                    break
	        byte2 = self.getByte() & 0xff
                if byte2 is None:
                    break
	        byte3 = self.getByte() & 0xff
                if byte3 is None:
                    break
        	byte4 = self.getByte() & 0xff
                if byte4 is None:
                    break
	        byte5 = self.getByte() & 0xff
                if byte5 is None:
                    break
	
	        if byte5 !=  (byte1 + byte2 + byte3 + byte4) % 256:
		    r=byte1 + byte2 + byte3 + byte4;
		    byte6 = self.getByte() & 0xff
		    if byte6 is None:
		        break
		    
		    if byte6 !=  (byte2 + byte3 + byte4 + byte5) % 256:
			byte7 = self.getByte() & 0xff
			if byte7 is None:
			    break
	
			if byte7 !=  (byte3 + byte4 + byte5 + byte6) % 256:
			    byte8 = self.getByte() & 0xff
			    if byte8 is None:
				break

			    if byte8 !=  (byte4 + byte5 + byte6 + byte7) % 256:
			        byte9 = self.getByte() & 0xff
			        if byte9 is None:
				    break

	        counter=0
            	while True:
                    byte = self.getByte()
            	    
                    if byte is None:
                        break

		    if counter==1:
		        counter=2
		        msb=byte & 0xff;
			
		        msb1=msb<<8
			
		        byte = self.getByte()
		        if byte is None:
                    	    break
		        lsb=byte & 0xff;
		        ppg=msb1+lsb
			print(ppg)
		        yield LiveDataPoint(ppg)

		    counter+=1
		    counter=counter%5
        except:
            self.disconnect()


def dumpData(port, filename):
    print "Saving real-time data..."
    print "Press CTRL-C or disconnect the device to terminate data collection."
    oximeter = Nonin(port)
    measurements = 0
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(LiveDataPoint.getCsvColumns())
        for liveData in oximeter.getLiveData():
            writer.writerow(liveData.getCsvData())
            measurements += 1

     

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Nonin Data Downloader - Shahnawaz")
    parser.add_argument("serialport", help="The device's virtual serial port.")
    parser.add_argument("output", help="Output CSV file.")

    args = parser.parse_args()

    dumpData(args.serialport, args.output)

    print ""
    print "Done."
