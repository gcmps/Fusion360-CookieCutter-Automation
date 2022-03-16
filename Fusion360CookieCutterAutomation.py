import pyautogui
import time

def opensvg(): #Function to open Fusion 360 and open SVG file automatically.
    pyautogui.moveTo(467, 1063) #Move to Fusion 360 icon (depends on the location of your Fusion360 icon).
    pyautogui.click() #Open app.
    pyautogui.moveTo(155, 95) #Move to create drawing.
    pyautogui.click() #Click in create drawing.
    pyautogui.moveTo(1080, 565) #Move to top plane.
    pyautogui.click() #Select the plane.
    pyautogui.moveTo(1230, 125) #Move to insert.
    pyautogui.click() #Click on insert.
    pyautogui.moveTo(1308, 243) #Move to insert DXF.
    pyautogui.click() #Click on insert DXF.
    pyautogui.moveTo(1772, 331) #Move to insert from my computer.
    pyautogui.click() #Click on insert from my computer.
    pyautogui.moveTo(640, 73) #Move to file path.
    pyautogui.doubleClick() #Double click on file path.
    pyautogui.press('backspace', presses=50) #Erase current file path.
    pyautogui.write('D:\Designs\Illustrator\Cookie Cutters') #SVG file location.
    pyautogui.press('enter') #Press enter.
    pyautogui.alert(text='Select your SVG file.', title='Next step.', button='OK') #Alert box.

def offset(): #Function to offset outlines for cookie cutter cutting edges.
    pyautogui.alert(text='Select the outline of the cutter.', title='Next step', button='OK') #Select the cutter outline to offset.
    pyautogui.press('o') #Offset.
    time.sleep(5) #Waits 5 seconds.
    pyautogui.write('.75') #.75 mm Offset.
    pyautogui.press('enter') #Press enter.
    pyautogui.alert(text='Reselect the cutter outline.', title='Next step', button='OK') #Reselect the cutter outline to offset.
    pyautogui.press('o') #Offset.
    time.sleep(5) #Waits 5 seconds.
    pyautogui.write('1.75') #1.75 mm Offset.
    pyautogui.press('enter') #Press enter.
    pyautogui.alert(text='Reselect the cutter outline.', title='Next step', button='OK') #Reselect the cutter outline to offset.
    pyautogui.press('o') #Offset
    time.sleep(5) #Waits 5 seconds.
    pyautogui.write('6') #6 mm Offset.
    pyautogui.press('enter') #Press enter.

def extrude1(): #Function to extrude cookie cutter handle.
    pyautogui.press('e') #Extrude.
    pyautogui.alert(text='Select the face of the handle.', title='Next step', button='OK') #Select the face to extrude the handle.
    time.sleep(5) #Waits 5 seconds.
    pyautogui.write('2') #2 mm extrude.
    pyautogui.press('enter') #Press enter.

def extrude2(): #Function to extrude first cutting edge.
    pyautogui.moveTo(45, 301)
    pyautogui.click()
    pyautogui.moveTo(140, 319)
    pyautogui.click()
    pyautogui.press('v')
    pyautogui.press('e')
    pyautogui.alert(text='Select the face of the cutting edge closest to the center.', title='Next step', button='OK')
    time.sleep(7)
    pyautogui.write('9')
    pyautogui.press('enter')

def extrude3(): #Function to extrude second cutting edge.
    pyautogui.moveTo(45, 301)
    pyautogui.click()
    pyautogui.moveTo(140, 319)
    pyautogui.click()
    pyautogui.press('v')
    pyautogui.press('e')
    pyautogui.alert(text='Select the face of the cutting edge closest to the edge of the cookie cutter.', title='Next step', button='OK')
    time.sleep(7)
    pyautogui.write('8')
    pyautogui.press('enter')

def extrude4(): #Function to extrude cookie cutter figure.
    pyautogui.moveTo(45, 301)
    pyautogui.click()
    pyautogui.moveTo(140, 319)
    pyautogui.click()
    pyautogui.press('v')
    pyautogui.press('e')
    pyautogui.alert(text='Select the face of the figure.', title='Next step.', button='OK')
    time.sleep(10)
    pyautogui.write('6')
    pyautogui.press('enter')

def extrude5(): #Function to extrude cookie cutter figure supports.
    pyautogui.moveTo(45, 301)
    pyautogui.click()
    pyautogui.moveTo(140, 319)
    pyautogui.click()
    pyautogui.press('v')
    pyautogui.press('e')
    pyautogui.alert(text='Select the face of the figure supports', title='Next step.', button='OK')
    time.sleep(10)
    pyautogui.write('2')
    pyautogui.press('enter')

def save(): #Function to save STL file.
    pyautogui.moveTo(40, 272)
    pyautogui.click()
    pyautogui.moveTo(154, 300)
    pyautogui.click(button='right')
    pyautogui.moveTo(273, 504)
    pyautogui.click()
    pyautogui.moveTo(1798, 603)
    pyautogui.click()
    pyautogui.moveTo(640, 73) #Move to file path.
    pyautogui.doubleClick() #Double click on file path.
    pyautogui.press('backspace', presses=50) #Erase current file path (presses erase 50 times).
    pyautogui.write('D:\Designs\Cura\Cookie Cutters') #STL file location.

#opensvg() #Calls the opensvg function (only needed if you want to automate all opening Fusion360 and SVG file).
time.sleep(5) #Waits 5 seconds.
offset() #Calls the offset function.
time.sleep(5) #Waits 5 seconds.
extrude1() #Calls the extrude1 function.
time.sleep(5) #Waits 5 seconds.
extrude2() #Calls the extrude2 function.
time.sleep(5) #Waits 5 seconds.
extrude3() #Calls the extrude3 function.
time.sleep(5) #Waits 5 seconds.
extrude4() #Calls the extrude4 function.
time.sleep(5) #Waits 5 seconds.
extrude5() #Calls the extrude5 function (only needed if figure needs supports attached in cookie cutter).
time.sleep(5) #Waits 5 seconds.
save() #Calls the save function.



