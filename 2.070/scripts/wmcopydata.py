# WM_COPYDATA, python ... try with py27 first - ASCII
# За toshko2.py, праща съобщение до синтезатора на реч Тошко 2.
# Използва се от POST-сървъра toshko2.py
# Author: Todor Arnaudov
# http://twenkid.com/software/toshko2
#-*-
import win32api
import win32gui
import win32con
import struct
import array

def wmcopydataB(say):	
	print("wmcopydataB(say)")
	import binascii
	s = "abcdef"
	d = binascii.a2b_qp(s)
	#print(d)
    #b'abcdef'

	#k = 0	
	#for i in range(1,60):	abv.append(k%60+190); k=k+1;

	#char_buffer = array.array('B', abv)
	print('before: char_buffer = array.array('B', binascii.a2b_qp(say))')
	
	#char_buffer = array.array('B', binascii.a2b_qp(say))
	#sayUTF = say.decode('utf-8') #windows-1251') 
	#say1251 = sayUTF.encode("windows-1251", "ignore")

	char_buffer = array.array('B', binascii.a2b_qp(say)) #1251))
	
	
	print('before: char_buffer')
	print(char_buffer)

	char_buffer_address, char_buffer_size = char_buffer.buffer_info()
	copy_struct = struct.pack("PLP", 2, char_buffer_size, char_buffer_address) #GLAS_CMDS_SPEAK=1, ..SIMPLE=2
	print(char_buffer_size)
	print(char_buffer_address)
	hwnd = win32gui.FindWindow(None, "WM_COPYDATA_GLAS")
	win32gui.SendMessage(hwnd, win32con.WM_COPYDATA, None, copy_struct)
	#Play
	#copy_struct = struct.pack("PLP", 1, char_buffer_size, char_buffer_address)
	#win32gui.SendMessage(hwnd, win32con.WM_COPYDATA, None, copy_struct)

def test():
  s1 = '$$$Ехооо...123456789'  #Add 3 or more padding spaces
  s2 = s1.decode(encoding='utf-8') #windows-1251')
  say = s2.encode('windows-1251')
  wmcopydataB(say)
