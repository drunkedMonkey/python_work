from pathlib import Path


def get_word_times(word, route):
    print(route)
    try:
        path = Path(route)
    
        contents = path.read_text(encoding='utf-8')
        lines = contents.splitlines()
        count = 0
        for line in lines:
            count += line.lower().count(word) 
        
    except FileNotFoundError:
        print("El archivo no existe")
        pass
    else:
        return count   
        
        

print("Dime una palabra y te diré cuántas veces aparece en el texto")
word = input("Palabra: ")

times = get_word_times(word, './10_archivos_excepciones/text_one.txt')
print(f"La palabra '{word}' aparece {times} veces en el texto 1")

times = get_word_times(word, './10_archivos_excepciones/text_two.txt')
print(f"La palabra '{word}' aparece {times} veces en el texto 2")


