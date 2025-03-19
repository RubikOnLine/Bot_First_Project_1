import openai
import config
import asyncio

client = openai.OpenAI(api_key=config.OPENAI_API_KEY)  # Создаем клиент OpenAI


async def translate_text(text, target_language):
    """Отправляет текст в ChatGPT и получает перевод"""
    prompt = f"Переведи этот текст на {target_language}: {text}"

    response = await asyncio.to_thread(
        client.chat.completions.create,
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
