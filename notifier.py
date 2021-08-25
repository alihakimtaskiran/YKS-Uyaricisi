import requests as req
from playsound import playsound
import time
siren_path="/home/ali/Downloads/VideoDownloader/Nuclear Alarm Siren - 10 minutes (Official 2020 Theme).mp3"
while True:
	if "YKS" in req.get("https://ais.osym.gov.tr").text:
		req.get("https://ali.local/alarm",verify=False)
		playsound(siren_path)
	time.sleep(3)
	
