import csv
import struct

def main():
    bin_ary = bytearray([])
    with open('./input.csv') as f_in:
        reader = csv.reader(f_in)
        for row in reader:
            try:
                v = float(row[1])   # non comma is possible with index zero.
            except ValueError:
                print('ValueError')
            else:
                bin_ary.extend(struct.pack('<f', v)) # little endian, 32bit float : compatible for GRC File Sink Block
                # print(hex(struct.unpack('<L', struct.pack('<f', v))[0])) # debug
                
    with open('./output.flt', 'wb') as f_out:
        f_out.write(bin_ary)
        print('done')
        
main()
