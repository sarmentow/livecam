ffmpeg -i "rtsp://localhost:8554/proxied" -vf mpdecimate -c:v h264 -flags +cgop -g 30 -hls_time 1 static/index.m3u8


