#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* EffortModel
#* Programa para procesar modelos lineales mediante correlación por cuadrados mínimos
#* #* UADER - FCyT
#* Ingeniería de Software II
#*
#* Dr. Pedro E. Colla
#* copyright (c) 2023,2024
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
import numpy as np
import pandas as pd
import argparse
import statsmodels.api as sm
import sys
import os
import matplotlib.pyplot as plt

#*------------------------------------------------------------------------------------------------
#* Almacena dataset histórico
#*------------------------------------------------------------------------------------------------
data = {
    'LOC': [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    'Esfuerzo': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
}

#*------------------------------------------------------------------------------------------------
#* Inicialización del programa
#*------------------------------------------------------------------------------------------------
version="7.0"
linear=False
exponential=False
os.system('clear')

#*------------------------------------------------------------------------------------------------
#* Procesa argumentos
#*------------------------------------------------------------------------------------------------
# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-v", "--version",required=False,help="version",action="store_true")
ap.add_argument("-x", "--exponential", required=False,help="Exponential model",action="store_true")
ap.add_argument("-l", "--linear", required=False,help="Linear model",action="store_true")
args = vars(ap.parse_args())

if args['version'] == True:
   print("Program %s version %s" % (sys.argv[0],version))
   sys.exit(0)

if args['linear'] == True:
   print("Program %s version %s" % (sys.argv[0],version))
   print("Linear correlation model selected")
   linear=True

if args['exponential'] == True:
   print("Program %s version %s" % (sys.argv[0],version))
   print("Exponential correlation model selected")
   exponential=True

if linear==False and exponential==False:
   print("Program %s version %s" % (sys.argv[0],version))
   print("Debe indicar modelo lineal (-l) o exponencial (-x) o ambos")
   linear=True
   exponential=True

#*-----------------------------------------------------------------------------------------------
#* Definir dataset y procesar corrlación entre LOC (complejidad) y Esfuerzo (PM)
#*-----------------------------------------------------------------------------------------------
df = pd.DataFrame(data)
correlation = df['LOC'].corr(df['Esfuerzo'])

#*------------------------------------------------------------------------------------------------
#* Procesa modelo lineal, usa numpy polyfit()
#*------------------------------------------------------------------------------------------------
r_value_linear = 0
if linear==True:
   a, b = np.polyfit(df['LOC'], df['Esfuerzo'], 1)
   R = np.corrcoef(df['LOC'], df['Esfuerzo'])
   R2=R*R
   r_value_linear=R2[0,1]
   print("Modelo lineal E=%.6f + %.6f*LOC)" % (b,a))
   print("El R-squared=%.4f (lineal)" % (r_value_linear))
   lbl=("modelo lineal (R-Sq=%.2f)" % (r_value_linear))
   plt.plot(df['LOC'], a*df['LOC']+b,label=lbl,color='red')

#*------------------------------------------------------------------------------------------------
#* procesa modelo exponencial utiliza OLS fit()
#*------------------------------------------------------------------------------------------------
mx_rsquared_exp = 0
if exponential==True:
   df['logEsfuerzo']=np.log(df['Esfuerzo'])
   df['logLOC']=np.log(df['LOC'])

   X = df['logLOC']
   Y = df['logEsfuerzo']
   X = sm.add_constant(X)  # Añadir una constante para el intercepto

   mx= sm.OLS(Y, X).fit()
   # print(mx.summary())

   k=np.exp(mx.params['const'])
   b=mx.params['logLOC']
   mx_rsquared_exp = mx.rsquared

   print("Modelo exponencial E=%.6f*(LOC^%.6f)" % (k,b))
   print("El R-squared=%.4f (exponencial)" % (mx_rsquared_exp))

   lbl=("modelo exponencial (R-Sq=%.2f)" % (mx_rsquared_exp))
   plt.plot(df['LOC'], k*(df['LOC']**b),label=lbl,color='green')

#*------------------------------------------------------------------------------------------------
#* Determinar el mejor modelo y realizar estimaciones (punto a, b y c)
#*------------------------------------------------------------------------------------------------

if r_value_linear > mx_rsquared_exp:
    best_model = 'linear'
else:
    best_model = 'exponential'

print("\n------------------------------------------------------------------------")
print("El modelo que mejor se ajusta a los datos es el %s" % (best_model))
print("------------------------------------------------------------------------")

if best_model == 'linear':
    # Modelo lineal
    a, b = np.polyfit(df['LOC'], df['Esfuerzo'], 1)
    
    # Estimación para LOC=9100 (b)
    loc_b = 9100
    effort_b = a * loc_b + b
    print("\nEstimación de esfuerzo para LOC=%d: %.2f persona-mes" % (loc_b, effort_b))
    plt.scatter(loc_b, effort_b, color='blue', label=f'Estimación LOC={loc_b}', marker='s')
    
    # Estimación para LOC=200 (c)
    loc_c = 200
    effort_c = a * loc_c + b
    print("Estimación de esfuerzo para LOC=%d: %.2f persona-mes" % (loc_c, effort_c))
    plt.scatter(loc_c, effort_c, color='purple', label=f'Estimación LOC={loc_c}', marker='s')
    
else:
    # Modelo exponencial
    df['logEsfuerzo']=np.log(df['Esfuerzo'])
    df['logLOC']=np.log(df['LOC'])
    X = df['logLOC']
    Y = df['logEsfuerzo']
    X = sm.add_constant(X)
    mx= sm.OLS(Y, X).fit()
    k=np.exp(mx.params['const'])
    b=mx.params['logLOC']
    
    # Estimación para LOC=9100 (b)
    loc_b = 9100
    effort_b = k * (loc_b ** b)
    print("\nEstimación de esfuerzo para LOC=%d: %.2f persona-mes" % (loc_b, effort_b))
    plt.scatter(loc_b, effort_b, color='blue', label=f'Estimación LOC={loc_b}', marker='s')

    # Estimación para LOC=200 (c)
    loc_c = 200
    effort_c = k * (loc_c ** b)
    print("Estimación de esfuerzo para LOC=%d: %.2f persona-mes" % (loc_c, effort_c))
    plt.scatter(loc_c, effort_c, color='purple', label=f'Estimación LOC={loc_c}', marker='s')

#*------------------------------------------------------------------------------------------------
#* Hace plot del dataset histórico
#*------------------------------------------------------------------------------------------------
plt.scatter(df['LOC'], df['Esfuerzo'], label='Datos históricos')
plt.xlabel('Complejidad [LOC]')
plt.ylabel('Esfuerzo (persona-mes)')
plt.legend()
plt.grid(True)
plt.show()
