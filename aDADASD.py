meme_dict = {
    "LOL": "una respuesta a algo gracioso",
    "CRINGE": "algo raro o embarazoso",
    "ROFL": "una respuesta a una broma",
    "SHEESH": "ligera desaprobación",
    "CREEPY": "aterrador, siniestro",
    "AGGRO": "ponerse agresivo/enojado"
}


print("¡Hola! Este programa te ayudará a entender algunos términos de memes.")
print("Simplemente escribe la palabra en mayUsculas y te dirE su significado.")

for i in range(5):
    word = input("Escribe una palabra que no entiendas¡con mayúsculas!): ")
    if word in meme_dict:
        print("El significado de " , word , "es:" , meme_dict[word] )
    else:
        print(word , "no está en el diccionario intenta con otra palabra")
