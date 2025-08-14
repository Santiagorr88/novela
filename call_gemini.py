from pathlib import Path
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
def call_gemini_extend_chapter(prompt_path: str, chapter_path: str, model_name="gemini-2.5-pro") -> str:
    # Configura API Key
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Carga archivos
    prompt_universo = Path(prompt_path).read_text(encoding="utf-8").strip()
    cap1 = Path(chapter_path).read_text(encoding="utf-8").strip()

    # Arma el input
    system_prompt = f"""Este es el narrador -> {cap1} y este es el planner {prompt_universo}"""
    user_input = f"""Estoy usando un flujo de agentes para generar una novela. El caso es que tengo tanto el narrador 
    como el planner digo que tienes que escrbir el capitulo completo y que cada parte del capitulo tiene que tener entre 1800 y 2000 palabras 
    pero cuando sacar el texto cada parte tiene menos de 1200 palabras.  
    ¿Como puedo mejorar para que tu entiendas que forzosamente cada parte del capitulo tiene que tener entre 1800 y 2000 palabras.?
    
    Damelo en formato md todo lo necesario y en ingles. 
"""






    # Llama a Gemini
    model = genai.GenerativeModel(
        model_name=model_name,
        system_instruction=system_prompt
    )
    chat = model.start_chat()
    response = chat.send_message(user_input)

    return response.text

if __name__ == "__main__":
    output = call_gemini_extend_chapter(
        prompt_path="src/agents/chapter_planner.md",
        chapter_path="src/agents/narrator.md"
    )

    #Path("src/chapters/extended_B1C1.md").write_text(output, encoding="utf-8")
    Path("src/respuesta_de_gemini.md").write_text(output, encoding="utf-8")
    print("Capítulo extendido guardado.")