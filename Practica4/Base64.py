import base64

file = open("encoded_msg.b64", "r") 
mensaje = file.read()
file.close

Decode = open ("Decode.txt", "wb")
Decode.write(base64.b64decode((mensaje)))
Decode.close()


fileIMG = open("mystery_img1.txt", "rb") 
IMGfile = fileIMG.read()
fileIMG.close

DecodeIMG = open ("DecodeIMG.jpeg", "wb")
DecodeIMG.write(base64.b64decode((IMGfile)))
DecodeIMG.close()
