from VirtualCopernicusNG import TkCircuit

# initialize the circuit inside the

configuration = {
    "name": "Lobby",
    "sheet": "sheet_smarthouse.png",
    "width": 332,
    "height": 300,
    "leds": [
        {"x": 112, "y": 70, "name": "LED 1", "pin": 21},
        {"x": 71, "y": 141, "name": "LED 2", "pin": 22}
    ],
    "buttons": [
        {"x": 242, "y": 146, "name": "Button 1", "pin": 11},
        {"x": 200, "y": 217, "name": "Button 2", "pin": 12},
    ],
    "buzzers": [
        {"x": 277, "y": 9, "name": "Buzzer", "pin": 16, "frequency": 440},
    ]
}

circuit = TkCircuit(configuration)


@circuit.run
def main():
    # now just write the code you would use on a real Raspberry Pi

    from gpiozero import LED, Button
    from time import sleep
    import socket

    MCAST_GRP = "236.0.0.0"
    MCAST_PORT = 3456

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    def button2_pressed():
        sock.sendto('f1;*;lamp;*;off'.encode('utf-8'), (MCAST_GRP, MCAST_PORT))
        led.off()

    led = LED(21)

    button1 = Button(11)
    button1.when_pressed = led.toggle

    button2 = Button(12)
    button2.when_pressed = button2_pressed

    while True:
        sleep(0.1)
