import base64
import argparse

# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument("--decodex", type=str)
# Parse the argument
args = parser.parse_args()
try:
 # decoding process
 (input_string) = args.decodex
 base64_converted_string = input_string.encode("ascii")
 decode = base64.b64decode(base64_converted_string)
 decimal_converted_string = decode.decode("ascii")
 print(decimal_converted_string)
except:
 # encoding process
 sample_string = args.decodex
 sample_string_bytes = sample_string.encode("ascii")
 base64_bytes = base64.b64encode(sample_string_bytes)
 base64_string = base64_bytes.decode("ascii")
 print({base64_string})
