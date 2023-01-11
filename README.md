# Livecam
An RTSP server that allows retransmission of RTSP sources behind a protected network without the need of port forwarding + a website to watch the live feed

## How it works
The RTSP source (there's some code in the repo for an ESP32 cam which was the device I had while developing this, but the RTSP source could be any other device) checks for the address of the retransmitter (stored in a webpage somewhere, in this specific implementation the ESP32 looks for it at a github pages domain) and establishes a TCP connection with it.

On the retransmission server side, it waits for the TCP connection to be established and then simply acts as if itself was the client, not the server (since it wasn't the TCP connection initiator).

This way there's no need for port forwarding.

## Open source code used
- simple-rtsp-server with custom Golang code for establishing the connection with the camera source (for the rtsp retransmission)
- ESP32-devcam with custom Arduino code for finding the address of the retransmission server

## Footage
The ESP32 that served as the RTSP source
![ESP32 that served as the RTSP source](https://user-images.githubusercontent.com/48866794/211899196-f07802fb-2508-46b7-a2cc-6316f61e7ee8.JPG)

[Video footage of the camera working with port forwarding](https://user-images.githubusercontent.com/48866794/211899417-b91a475a-fb35-4c94-bd1a-341dc810951d.mov)

TODO: add footage of the camera working at the beach recording waves without port forwarding
