def set_light_values(brigthness: int, color_temp: str) -> dict:
    "Ajustando a luminosidade e temperatura."

    return {"brigthness": brigthness, "temperatura": color_temp}


def intruction_alert() -> str:
    "Instrução para o usuário."

    return {"alert": "Olá, eu sou o assistente virtual, como posso te ajudar?"}


__all__ = ["set_light_values", "instruction_alert"]
