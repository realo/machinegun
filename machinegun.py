import argparse
try:
	import tools.addons.clean
	import tools.addons.winpcap
	import tools.addons.logo
except ImportError:
	print("Failed import some modules")

def main():
	parser = argparse.ArgumentParser(description = "Denial-of-service ToolKit")
	parser.add_argument("--target", type = str, metavar = "<PHONE>",
					help = "Target ip:port, url or phone")
	parser.add_argument("--method", type = str, metavar = "<SMS>",
					help = "Attack method")
	parser.add_argument("--time", type = int, default = 10, metavar = "<time>",
					help = 'time in secounds')
	parser.add_argument("--threads", type = int, default = 3, metavar = "<threads>",
					help = "threads count (1-200)")


	args = parser.parse_args()
	threads = args.threads
	time = args.time
	method = str(args.method).upper()
	target = args.target

	if method == "SMS":
		from tools.SMS.main import SMS_ATTACK
		SMS_ATTACK(threads, time, target)

	else:
		parser.print_help()

if __name__ == '__main__':
	main()
