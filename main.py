import dearpygui.dearpygui as dpg
import webbrowser
from just_playback import Playback
import threading

pb = Playback() 
pb.set_volume(0.5)

def moreInfo():
	webbrowser.open('https://darioarzaba.vercel.app/blog/programming/morsecode')

dpg.create_context()
dpg.create_viewport(title='Morse Code Learning App', width=1200, height=800, small_icon='img\icon.ico', large_icon='img\icon.ico')

def sound(morseChar, threadCreatedFlag):
		pb.load_file('mp3\\' + morseChar + '.mp3')
		t = threading.Thread(target=pb.play, args=(), daemon=True)
		t.stoprequest = threading.Event()
		t.start()
		threadCreated = True
		return threadCreated

def change_text(sender, app_data):
	threadCreated = False
	if pb.playing == False:
		pb.stop()
		if threadCreated == True:
			t.stoprequest.set()
			threadCreated = False
	userInputString = dpg.get_value("userInput")
	for cdata in (list(map(chr, range(97, 123))) +  list(map(chr, range(44, 47))) + list(map(chr, range(48, 58)))):
		if chr(app_data).lower() == cdata: 
			threadCreated = sound(chr(app_data).lower(), threadCreated)
	if len(userInputString) < 50:
		dpg.set_value("userInput", userInputString + chr(app_data) )
	else:
		dpg.set_value("userInput", chr(app_data) )

with dpg.handler_registry():
    dpg.add_key_press_handler(callback=change_text)

width, height, channels, data = dpg.load_image("img\MorseCode.png")

with dpg.texture_registry():
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="morseCodeTag")

with dpg.window(tag="Primary Window"):
	dpg.add_text("Morse Code is the oldest electronic means of public communication. Originally designed in 1838 by Samuel Morse and perfected by Alfred Vail.")
	dpg.add_text("In order to send the code Samuel and Alfred contributed to the creation of the electrical telegraph in 1836")
	dpg.add_text("finally testing the encoding as we know it in 1844 with the message 'What hath god wrought' sent from Washington to Baltimore.")

	dpg.add_text("1. The dot is the basic unit of time measurement.")
	dpg.add_text("2. Dashes last three dots.")
	dpg.add_text("3. Between every dot and dash there is dot of signal absence called space.")
	dpg.add_text("4. Between each character there are three spaces.")
	dpg.add_text("5. Between each word there are seven spaces.")
	dpg.add_spacer()
	dpg.add_button(label="Learn More", callback=moreInfo)
	dpg.add_spacer()
	dpg.add_separator()
	dpg.add_spacer()
	dpg.add_text("Morse Code Keyboard (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,0,1,2,3,4,5,6,7,8,9)")
	dpg.add_input_text(tag="userInput", width=500)
	dpg.add_spacer()
	dpg.add_separator()
	dpg.add_spacer()
	dpg.add_image("morseCodeTag")




    






dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()


