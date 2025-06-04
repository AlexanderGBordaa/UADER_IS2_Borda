#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pago_automatizado.py

Versión 1.2

Este programa automatiza la selección de cuentas bancarias para realizar pagos
utilizando los patrones Singleton, Chain of Responsibility e Iterator.

Autor: UADER - FCyT - IS2 ©2025
"""

import json
from collections import deque


class JsonReader:
    
    # singleton para leer claves de un archivo JSON.
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def read_key_from_file(self, filename, key):
        
        #Lee una clave específica desde un archivo JSON.
        
        try:
            with open(filename, "r", encoding="utf-8") as myfile:
                data = json.load(myfile)
                return str(data.get(key, f"Clave '{key}' no encontrada."))
        except FileNotFoundError:
            return f"Archivo '{filename}' no encontrado."
        except json.JSONDecodeError:
            return "Formato JSON inválido."
        except Exception as e:
            return f"Error inesperado: {str(e)}"


class Cuenta:
   # Representa una cuenta bancaria con saldo y token.

    def __init__(self, token, saldo_inicial):
        self.token = token
        self.saldo = saldo_inicial

    def puede_pagar(self, monto):
    
        #Verifica si hay saldo suficiente para pagar.
        
        return self.saldo >= monto

    def procesar_pago(self, monto):
        
        #Descuenta saldo y retorna clave de token.
    
        self.saldo -= monto
        return JsonReader().read_key_from_file("sitedata.json", self.token)


class Pago:

    #Representa un pago con número, token y monto.


    def __init__(self, numero, token, monto):
        self.numero = numero
        self.token = token
        self.monto = monto

    def __str__(self):
        return f"Pedido #{self.numero} - Token: {self.token} - Monto: ${self.monto}"


class HistorialPagos:

    #Contiene todos los pagos realizados y permite iterarlos.
    

    def __init__(self):
        self.pagos = []

    def agregar_pago(self, pago):
        """
        Agrega un pago al historial.
        """
        self.pagos.append(pago)

    def __iter__(self):
        return iter(self.pagos)


class ManejadorPagos:
    #Controla el flujo de pagos entre múltiples cuentas.
    #Aplica el patrón Chain of Responsibility.

    def __init__(self, cuentas):
        self.cuentas = cuentas  # Lista de objetos Cuenta
        self.turnos = deque(cuentas)
        self.historial = HistorialPagos()
        self.contador_pedidos = 1

    def solicitar_pago(self, monto):
        
        #Alterna entre cuentas con saldo suficiente para realizar el pago.
        
        for _ in range(len(self.turnos)):
            cuenta = self.turnos[0]
            if cuenta.puede_pagar(monto):
                clave = cuenta.procesar_pago(monto)
                pago = Pago(self.contador_pedidos, cuenta.token, monto)
                self.historial.agregar_pago(pago)
                print(f"{pago} - Clave usada: {clave}")
                self.contador_pedidos += 1
                self.turnos.rotate(-1)
                return
            self.turnos.rotate(-1)
        print("No hay cuentas con saldo suficiente para procesar el pago.")

    def mostrar_historial(self):
        
        #Muestra todos los pagos realizados en orden.
        
        print("\nHistorial de pagos:")
        for pago in self.historial:
            print(pago)


def main():
    
    #Función principal: ejecuta múltiples pedidos de pago.
    
    cuenta1 = Cuenta("token1", 1000)
    cuenta2 = Cuenta("token2", 2000)
    manejador = ManejadorPagos([cuenta1, cuenta2])

    for _ in range(6):  # Seis pagos de $500
        manejador.solicitar_pago(500)

    manejador.mostrar_historial()


if __name__ == "__main__":
    main()
