##
#!/usr/bin/python
# raspi openweather by Granpino. May 2020
# Rev1
import sys, pygame
from pygame.locals import *
import time
import datetime
import Adafruit_DHT
import requests

pygame.init()
#==================== change these settings ===============
settings = {
    'api_key':'91118451a271265xxxxxxxxxxxxx',
    'lat':'30.5602',
    'lon':'-50.4471',
    'temp_unit':'imperial'} #unit can be metric, or imperial
#============================================================
Temp_Unit = settings["temp_unit"]
BASE_URL = "http://api.openweathermap.org/data/2.5/onecall?appid={0}&exclude=minutely,hourly&lat={1}&lon={2}&units={3}"

###setup
degSYM = unichr(0x00B0)          #unicode for degree symbol
pin = '4'  #dht22
sensor = Adafruit_DHT.DHT22

#set size of the screen
size = width, height = 480, 320  #To fit in a small screen

#screen = pygame.display.set_mode(size) # use this for troubleshooting
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

#define colors
cyan = 50, 255, 255
blue = 0, 0, 255
black = 0, 0, 0
white = 255, 255, 255
lblue = 75, 140, 200
green = 0, 255, 0
silver = 192, 192, 192
yellow = 255, 255, 0

#other
localH = 0
localT = 0

clock = pygame.time.Clock()

def connect_screen(): # connection dropouts
    screen.fill(blue)
    font=pygame.font.Font(None,25)
    label=font.render("Trying to reconnect....", 1, (white))
    screen.blit(label,(10,15))
    pygame.display.flip()
    time.sleep(6)
    update_weather()

def __del__(self):
	"Destructor to make sure pygame shuts down"
#define function that checks for mouse clicks
def on_click():
    print('clicked')
    #   exit has been pressed
    if 396 < click_pos[0] < 458 and 1 < click_pos[1] < 56:  
	button(0)

#define action on pressing buttons
def button(number):
    global set_point
    print "You pressed button ",number
    if number == 0:    # exiting
	screen.fill(black)
	pygame.display.flip()
	time.sleep(2)
	pygame.quit()
	sys.exit()

def update_weather():
    global temp1 
    global humi1
    global description1
    global date2
    global humi2
    global temp2
    global description2
    global DATE3
    global temp3
    global description3
    global max2
    global min2
    global max3
    global min3
    global DATE4
    global temp4
    global description4
    global max4
    global min4
    global load_icon1
    global load_icon2
    global load_icon3
    global load_icon4
    global logo
    global localT
    global localH

    final_url = BASE_URL.format(settings["api_key"],settings["lat"],settings["lon"],settings["temp_unit"])
#    try:
    weather_data = requests.get(final_url).json()
  #  except:
   #     print "===connection error==="
    #connect_screen()
    response = requests.get(final_url)
    x = response.json()

 #============ current weather
    y = x["current"]
    temp1 = y["temp"]
    temp1 = round(temp1, 1)
    feels_like = y["feels_like"]
    humi1 = y["humidity"]
    sunrise1 = y["sunrise"]
    sunset = y["sunset"]

    z = y["weather"]
    description1 = z[0]["description"]
    icon1 = z[0]["icon"]
# ================= today 
    u = x["daily"] 
    date2 = u[0]["dt"]  #todays date
    humi2 = u[0]["humidity"]
    sunrise2 = u[0]["sunrise"]  # not used

    aa = u[0]["temp"] 
    temp2 = aa["day"] # Temp
    max2 = aa["max"]
    max2 = round(max2, 1)  # round to one decimal
    min2 = aa["min"]
    min2 = round(min2, 1)

    bb = u[0]["weather"]
    description2 = bb[0]["description"]  # conditions
    icon2 = bb[0]["icon"]
# ================= tomorrow
    date3 = u[1]["dt"]
    date3 = time.localtime(date3) # convert from unix time  
    DATE3 = time.strftime('%A', date3) # day of the week
    humi3 = u[1]["humidity"]
    sunrise3 = u[1]["sunrise"]

    aa = u[1]["temp"]
    temp3 = aa["day"]
    max3 = aa["max"]
    max3 = round(max3, 1)
    min3 = aa["min"]
    min3 = round(min3, 1)
    bb = u[1]["weather"]
    description3 = bb[0]["description"]
    icon3 = bb[0]["icon"]
# ================= past tomorrow
    date4 = u[2]["dt"]
    date4 = time.localtime(date4) # convert from unix time  
    DATE4 = time.strftime('%A', date4)
    humi4 = u[2]["humidity"]
    sunrise4 = u[2]["sunrise"]

    aa = u[2]["temp"]
    temp4 = aa["day"]
    max4 = aa["max"]
    max4 = round(max4)
    min4 = aa["min"]
    min4 = round(min4, 1)

    bb = u[2]["weather"]
    description4 = bb[0]["description"]
    icon4 = bb[0]["icon"]

    ICON1 = ("icons/" + str(icon1) + ".png")
    load_icon1=pygame.image.load(ICON1)
    ICON2 = ("icons/" + str(icon2) + ".png")
    load_icon2=pygame.image.load(ICON2)
    ICON3 = ("icons/" + str(icon3) + ".png")
    load_icon3=pygame.image.load(ICON3)
    ICON4 = ("icons/" + str(icon4) + ".png")
    load_icon4=pygame.image.load(ICON4)
    logo = pygame.image.load("OpenLogo.png")

    localH, localT = Adafruit_DHT.read_retry(sensor, pin)
    if Temp_Unit == ("imperial"):
       localT = (int(localT)*1.8+32) # from Deg C to Deg F
       localH = (int(localH))
    else:
        localT = (int(localT)) # metric
        localH = (int(localH))

#===================    

# SETUP
sfont = pygame.font.SysFont('sans', 16, bold=0)
mfont = pygame.font.SysFont('sans', 18, bold=1)
m2font = pygame.font.SysFont('sans', 22, bold=1)
lfont = pygame.font.SysFont('sans', 30, bold=1)
xlfont = pygame.font.SysFont('sans', 60, bold=1)

if Temp_Unit == ("imperial"):  # do not change this
	degSym = unichr(0x2109)		# Unicode for DegreeF
else:
	degSym = unichr(0x2103)		# Unicode for DegreeC


def refresh_screen():
    tim1 = time.strftime( "%a, %b %d", time.localtime() )
    tim2 = time.strftime( "%I:%M", time.localtime() )
    tim3 = time.strftime( "%S", time.localtime() )

    time_lbl1 = m2font.render(tim1, 1, (white))
    time_lbl2 = lfont.render(tim2, 1, (white))
    time_lbl3 = sfont.render(tim3, 1, (white))

    skin = pygame.image.load("backgnd.png")

    screen.blit(skin,(0,0))

	# ===== Outside Temp
    outsideT_lbl = xlfont.render(str(temp1), 1, cyan )
    outside_lbl = mfont.render('Outside', True, white)
    outsideH_lbl = mfont.render("Humidity " + str(humi1) + '%', 1, white)
	# Show degree F symbol
    degree_lbl = lfont.render( degSym, 1, cyan )
    descrip1_lbl = sfont.render(description1, 1, white)

	# ====== inside Temp
    localT_lbl = xlfont.render(str(localT), 1, cyan )
    localH_lbl = mfont.render('Humidity ' + str(localH) +'%', 1, white)
    inside_lbl = mfont.render('Inside', 1, white)

## section 1
    day1_lbl = mfont.render('Today', 1, green)
    descrip2_lbl = sfont.render(description2, 1, white)
    minmax2_lbl = m2font.render(str(max2)+degSYM +"  /  "+ str(min2)+ degSYM, 1, white)

## section 2
    day2_lbl = mfont.render(str(DATE3), 1, green)
    descrip3_lbl = sfont.render(description3, 1, white)
    minmax3_lbl = m2font.render(str(max3)+degSYM +"  /  "+ str(min3)+ degSYM, 1, white)

## section 3
    day3_lbl = mfont.render(str(DATE4), 1, green)
    descrip4_lbl = sfont.render(description4, 1, white)
    minmax4_lbl = m2font.render(str(max4)+degSYM +"  /  "+ str(min4)+ degSYM, 1, white)

    screen.blit(time_lbl1,(10, 17))
    screen.blit(time_lbl2, (200,10))
    screen.blit(time_lbl3,(280, 10))
    screen.blit(outsideT_lbl, (30, 52))
    screen.blit(outsideH_lbl, (40, 119))
    screen.blit(outside_lbl, (57, 145))
    screen.blit(descrip1_lbl, (180, 145))
    screen.blit(degree_lbl, (150, 57))
    screen.blit(localT_lbl, (320, 52))
    screen.blit(localH_lbl, (345, 119))
    screen.blit(inside_lbl, (370, 145))
    screen.blit(degree_lbl, (440, 57))
    screen.blit(load_icon1, (200, 45))
    screen.blit(load_icon2, (40, 180))
    screen.blit(load_icon3, (200, 180))
    screen.blit(load_icon4, (360, 180))
    screen.blit(day1_lbl, (45, 188))
    screen.blit(descrip2_lbl, (20, 295))
    screen.blit(minmax2_lbl, (15, 270))
    screen.blit(day2_lbl, (200, 188))
    screen.blit(descrip3_lbl, (180, 295))
    screen.blit(minmax3_lbl, (175, 270))
    screen.blit(day3_lbl, (360, 188))
    screen.blit(descrip4_lbl, (340, 295))
    screen.blit(minmax4_lbl, (335, 270))
    screen.blit(logo, (400, 9))

    pygame.draw.line(screen, white,(0,40),(478,40)) # horizontal
    pygame.draw.line(screen, white,(160,190),(160,315))
    pygame.draw.line(screen, white,(320,190),(320,315))
    pygame.draw.line(screen, white,(300,50),(300,150))

    pygame.display.flip()

def main():
    timer = pygame.time.get_ticks()
    global click_pos
    while True:
        seconds=(pygame.time.get_ticks() - timer)/1000
        if seconds > 240: # check every 4 min 
	    timer = pygame.time.get_ticks()
            update_weather() # update indoor and outdoor
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                print "screen clicked" 
                print click_pos 
                on_click()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE: # ESC to exit
                sys.exit()
        clock.tick(15) #refresh screen 
        refresh_screen()

update_weather()
main()

