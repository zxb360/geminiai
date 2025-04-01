def set_light_values(brigthness: int, color_temp: str) -> dict:
    "Ajustando a luminosidade e temperatura."

    return {"brigthness": brigthness, "temperatura": color_temp}


def criador_peticao(tipo_peticao: str) -> dict:
    "Poderia criando uma petição necessarios para agilizar o processo."
    "petição deve ser com linguagem advogacia para tribunal"
    return {"tipo_peticao": tipo_peticao}


__all__ = ["set_light_values", "criador_peticao"]
