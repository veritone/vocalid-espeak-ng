import ctypes
import sys
import time

clib = ctypes.CDLL("./libespeak-ng.so")
clib.espeak_ng_InitializePath.argtypes = [ctypes.c_char_p]
clib.espeak_ng_InitializePath("/home/mtoman/espeak-ng".encode("UTF-8"))
clib.vocalid_TextToIPA.argtypes = [ctypes.c_char_p]
clib.vocalid_TextToIPA.restype = ctypes.c_char_p

for i in range(100000):
    for j in range(1):
        result = clib.vocalid_TextToIPA("This is a test, and more. Test".encode("UTF-8"), "en-us".encode("UTF-8"))
        #print(result.decode("UTF-8", errors='ignore'))
    #time.sleep(1)
