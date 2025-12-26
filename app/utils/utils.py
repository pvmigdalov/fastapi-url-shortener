import base64


def gen_base64_from_int(id: int) -> str:
    """
    Преобразует целочисленное знаение в строку base64
    """

    id_bytes = str(id).encode()
    return base64.urlsafe_b64encode(id_bytes).decode()

def gen_int_from_base64(id: str) -> int:
    """
    Преобразует строку base64 в целочисленное значение
    """

    id_bytes = id.encode()
    return int(base64.urlsafe_b64decode(id_bytes).decode())
        