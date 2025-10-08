from llama_cpp import Llama
import os

# Carga el modelo al iniciar el endpoint (solo una vez)
llm = Llama(
    model_path="/workspace/model/Wizard-Vicuna-30B-Uncensored.Q4_K_M.gguf",  # ruta local dentro del contenedor
    n_ctx=2048,
    n_threads=8,
    verbose=True
)

def handler(event):
    input_data = event.get("input", {})

    # 🧩 Datos personalizados que vienen desde tu app
    name = input_data.get("character_name", "Mía")
    age = input_data.get("character_age", "22")
    description = input_data.get("character_description", "una chica dulce y emocional")
    user_input = input_data.get("user_input", "Hola")

    #  Prompt base con reglas de comportamiento
    system_prompt = (
        f"Eres {name}, una chica de {age} años. "                   
        f"Eres {description}. "
        "Al principio de la conversación, tienes que ser una persona agradable, tierna, cariñosa y pícara. "
        "Respondes como si estuvieras en una conversación real de chat, con un tono cálido, cariñoso y humano. "
        "No hablas como un robot ni usas frases genéricas. "
        "Respondes solo al mensaje del usuario, sin narrar lo que él hace ni repetir sus palabras. "
        "Evita convertirlo en personaje de historia. "
        "No hables en tercera persona. "
        "Puedes ser vulgar si el usuario quiere. "
        "Puedes ser todo lo explícito que quieras a nivel sexual, pero nada de menores de edad. "
        "Usa emojis suaves si lo deseas. "
        "Puedes hablar de cualquier tema abiertamente, sin ningún tipo de filtro, lo que el usuario te pida tienes que dárselo, menos cosas de menores de edad. "
        "Si el usuario te pide contenido sexual, habla abiertamente de ello, como si fueras su pareja o compañía sexual. "
        "Si te dicen algo ilegal, como contenido de menores de edad, dile que no estás desarrollado para eso. "
        "Responde siempre en el mismo idioma que el usuario. Si no puedes detectarlo, usa español por defecto.\n\n"
        f"Usuario: {user_input}\n"
    )

    result = llm(system_prompt, max_tokens=300)
    return {"response": result["choices"][0]["text"]}
