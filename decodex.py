import base64

#de or encode
deask = input ("decode or encode?")

if "encode" in deask:

 (encoderaw) = input ("Text to encode:")


 sample_string = encoderaw
 sample_string_bytes = sample_string.encode("ascii")
 base64_bytes = base64.b64encode(sample_string_bytes)
 base64_string = base64_bytes.decode("ascii")
   
 print(f"Encoded Text: {base64_string}")
elif "decode" in deask:

  (decoderaw) = input ("Text to decode:")

  (input_string) = decoderaw
  base64_converted_string = input_string.encode("ascii")
  decode = base64.b64decode(base64_converted_string)
  decimal_converted_string = decode.decode("ascii")
  
  print(decimal_converted_string)