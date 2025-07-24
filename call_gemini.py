from pathlib import Path
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
def call_gemini_extend_chapter(prompt_path: str, chapter_01: str, chapter_02, model_name="gemini-2.5-pro") -> str:
    # Configura API Key
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Carga archivos
    prompt_universo = Path(prompt_path).read_text(encoding="utf-8").strip()
    cap1 = Path(chapter_01).read_text(encoding="utf-8").strip()
    cap28 = Path(chapter_02).read_text(encoding="utf-8").strip()

    # Arma el input
    system_prompt = prompt_universo,cap1, cap28
    user_input = f"""Te voy a pasar 2 capitulos de una novela que estoy escribiendo. El capitulo 1 y capitulo 28, ademas del lore de como quiero ciertas cosas.
    Tu funcion es darme un arco argumentar completo tomando como refencia el capitulo 1 y capitulo 28 general todo el arco argumental dividos por libros, es decir tomo 1 que termina en el 
    capitulo 28 y crearte los otros 2 arcos argumentar de los otros 2 tomos, pueden ser mas capitulos entre 35 -45 capitulos cada .
    
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
        prompt_path="src/lore/prompt_universo.md",
        chapter_01="src/chapters/B1C01.md",
        chapter_02="src/chapters/B1C28.md"
    )

    #Path("src/chapters/extended_B1C1.md").write_text(output, encoding="utf-8")
    Path("src/lore/arco_argumental_completo.md").write_text(output, encoding="utf-8")
    print("Capítulo extendido guardado.")