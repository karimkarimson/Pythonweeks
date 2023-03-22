jahr = input("Bitte gebe eine Jahreszahl ein: ")
jahr = int(jahr)
jahrDurchVier = jahr % 4
jahrDurchHundert = jahr % 100
jahrDurchVierhundert = jahr % 400
if jahrDurchVier != 0:
	print("Woiss nicht Digga, {} ist eher kein Schaltjoaah".format(str(jahr)))
elif jahrDurchVier == 0:
	print("Noice, {} ist ein Schaltjahr".format(str(jahr)))
elif jahrDurchHundert == 0:
    print("Woiss nicht Digga, {} ist eher kein Schaltjoaah".format(str(jahr)))
elif jahrDurchVierhundert == 0:
	print("Wer Mathe und Programmieren kann wird wissen, dass dieser Teil fuer immer unberuehrt bleibt")