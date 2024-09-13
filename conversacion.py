import random #IMPORTAMOS LA LIBRERIA RANDOM

#DICCIONARIO CON PREGUNTAS Y RESPUESTAS 
preguntas_respuestas = {
    "¿como estas?": ["Muy bien","Muy mal","Extremadamente bien"],
    "¿que haces?": ["Nada la verdad","Estudiando para mi examen","Comiendo un poco de cereal"]
}
def conversacion():
    while True:
        entrada = input("Tu: ")
        entrada = entrada.lower()
        if entrada in ("bye","adios"):
            print("Lucy: Hasta luego")
            break
        else:
            if entrada in preguntas_respuestas:
                respuestas = random.choice(preguntas_respuestas[entrada])
                print("Lucy: " + respuestas)
            else:
                print("Lucy: Lo siento mucho, no te entendi.")
if __name__ == '__main__':
    print("BIENVENIDO  A LA CONVERSACION CON LUCY. ESCRIBE UNA PREGUNTA.")
conversacion()