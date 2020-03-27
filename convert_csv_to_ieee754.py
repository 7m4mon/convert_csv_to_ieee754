import csv
import struct
import sys

def csv2float(in_file_name = './input.csv' , out_file_name = './output.flt', row_val = 1):
    bin_ary = bytearray([])
    with open(in_file_name) as f_in:
        reader = csv.reader(f_in)
        for row in reader:
            try:
                v = float(row[row_val])   # non comma is possible with index zero.
            except ValueError:
                print('ValueError')
            else:
                bin_ary.extend(struct.pack('<f', v)) # little endian, 32bit float : compatible for GRC File Sink Block
                # print(hex(struct.unpack('<L', struct.pack('<f', v))[0])) # debug
                
    with open(out_file_name, 'wb') as f_out:
        f_out.write(bin_ary)
        print('done')
        
if __name__ == '__main__':
    args = sys.argv
    if 4 <= len(args):
        csv2float(args[1], args[2], int(args[3]))
    elif 3 == len(args):
        csv2float(args[1], args[2])
    elif 2 == len(args):
        csv2float(args[1])
    else:
        print('input_file, output_file, row')
        
