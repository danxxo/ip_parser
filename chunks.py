def split_list_into_chunks(list_to_split, chunk_size):
    """Разбивает список на листы с указанным размером чанка.

    Args:
    list_to_split: Список, который нужно разбить.
    chunk_size: Размер каждого чанка.

    Returns:
    Список, содержащий чанки.
    """

    # Проверяем, валидный ли размер чанка.
    if chunk_size <= 0:
        raise ValueError("Размер чанка должен быть больше 0.")

    # Вычисляем количество чанков.
    num_chunks = int(len(list_to_split) / chunk_size) + 1

    # Создаем список для хранения чанков.
    chunked_list = []

    # Разбиваем список на чанки.
    for i in range(num_chunks):
        start_index = i * chunk_size
        end_index = min((i + 1) * chunk_size, len(list_to_split))
        chunked_list.append(list_to_split[start_index:end_index])

    return chunked_list
