import random
import time
import os

def Jugar():
	os.system("cls")
	print("Quieres jugar piedra papel y tijera")
	Answer = str(input())
	if Answer == "Si"or Answer == "si" or Answer == "SI" or Answer == "sI":
		print("Elija entre piedra papel o tijera")
		Decision = str(input())
		time.sleep(0.5)
		print(".")
		time.sleep(0.5)
		print("..")
		time.sleep(0.5)
		print("...")
		time.sleep(1)
		Desafio(Decision)

def Desafio(Des):
	ED = None
	EA = ["Piedra", "Papel", "Tijera"]
	ED = random.choice(EA)
	if Des == "Papel" or Des == "papel":
		if ED == "Piedra":
			print("Ganaste por que rival escogio " + ED)
			time.sleep(10)
			print("Exit in 10 seconds")
		if ED == "Papel":
			print("Empate por que tu rival escogio " + ED)
			time.sleep(10)
			print("Exit in 10 seconds")
		if ED == "Tijera":
			print("Perdiste por que tu rival escogio " + ED)
			time.sleep(10)
			print("Exit in 10 seconds")

	if Des == "Piedra" or Des == "piedra":
		if ED == "Papel":
			print("Perdiste por que tu rival escogio " + ED)
			time.sleep(10)
			print("Exit in 10 seconds")
		if ED == "Piedra":
			print("Empate por que tu rival escogio " + ED)
			time.sleep(10)
			print("Exit in 10 seconds")
		if ED == "Tijera":
			print("Ganaste por que tu rival escogio " + ED)
			time.sleep(10)
			print("Exit in 10 seconds")
	
	if Des == "Tijera" or Des == "tijera" or Des == "Tijeras" or Des == "tijeras":
		if ED == "Papel":
			print("Ganaste por que tu rival escogio " + ED)
			time.sleep(10)
			print("Exit in 10 seconds")
		if ED == "Piedra":
			print("Perdiste por que tu rival escogio " + ED)
			time.sleep(10)
			print("Exit in 10 seconds")
		if ED == "Tijera":
			print("Empate por que tu rival escogio " + ED)
			time.sleep(10)
			print("Exit in 10 seconds")
Jugar()