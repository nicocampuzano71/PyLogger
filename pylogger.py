Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import socket
>>> scksv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
>>> listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
>>> def conectar(host,port): #Host como cadena, entre "",port es un entero
	scksv.connect((host,port)) #Las direcciones son tuplas -> (host,puerto)
	listener.bind(("",port)) # "" en el host indica que es válida cualquier dirección de la máquina local
	listener.listen(10)#El backlog(10) realmente importa poco, por si se desconecta y vuelve a conectar...creo que con 1 valdría
	sckcl, address = listener.accept()
	
	while 1:
		svdata = scksv.recv(7072) #7072 es el numero de bytes, aproximadamente 800 caracteres para packets largos clientside, mejor multiplos de 8
		if svdata.decode("utf-8") != "": #Para leerlo en ascii se decodifica según la codificación utf-8, permite imprimir char(0)
			sckcl.send(svdata) #Mantiene comunicación
			print("[+] Server --> " + svdata.decode("utf-8"))
		cldata = sckcl.recv(7072)
		if cldata.decode("utf-8") != "":
			scksv.send(cldata)
			print("[+] Client --> " + cldata.decode("utf-8"))


>>> 
