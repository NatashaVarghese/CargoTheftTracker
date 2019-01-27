
import csv_reader


def main():
	data = csv_reader.readMyFile("ITM_20190121.csv")
	for i in range(130):
		print(data['1084067241'][9][i])

main()