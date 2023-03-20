from time import sleep

bcolors = {
    "HEADER": '\033[95m',
    "OKBLUE": '\033[94m',
    "OKCYAN": '\033[96m',
    "OKGREEN": '\033[92m',
    "WARNING": '\033[93m',
    "FAIL": '\033[91m',
    "ENDC": '\033[0m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m',
}

# colored string
def colstr(msg: str, color: str):
    # use -> colstr('[DEBUG]', bcolors.WARNING)
    return f"{bcolors[color]}{msg}{bcolors['ENDC']}"

def debug_print(*msg, **kwargs):
    print(f"{colstr('[DEBUG]', 'WARNING')} {' '.join(msg)}", **kwargs)

def print_notification(*msg, **kwargs):
    print(f"{colstr('[NOTICE]', 'HEADER')} {' '.join(msg)}", **kwargs)

def print_ok():
    print(f" {colstr('[ OK ]', 'OKGREEN')}")

def print_no():
    print(f" {colstr('[ NO ]', 'FAIL')}")

def connect_to_wifi(ssid, password):
    debug_print("connecting to wifi...", end = "")
    
    import network
    
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    
    while station.isconnected() == False:
        pass
    print_ok()
    
    debug_print("server listening on: " + station.ifconfig()[0])
    

def is_btn_pressed(btn):
    return not btn.value()

def blink_led(led, interval, iterations):
    for _ in range(iterations * 2):
        led.value(not led.value())
        sleep(interval)
        


def create_web_page():
    with open("webServer/index.html", "r") as htmlfile:
        html = "\n".join(htmlfile.readlines())
    
    # inject javascript in webpage
    with open("webServer/index.js", "r") as jsfile:
        
        html = html.replace(
            "<!-- inject js -->",
            "<script type='module'>" + "\n".join(jsfile.readlines()) + "</script>"
        )

    return html