def split_list_into_chunks(list_to_split, chunk_size):
    if chunk_size <= 0:
        raise ValueError("Размер чанка должен быть больше 0.")

    num_chunks = int(len(list_to_split) / chunk_size) + 1

    chunked_list = []

    for i in range(num_chunks):
        start_index = i * chunk_size
        end_index = min((i + 1) * chunk_size, len(list_to_split))
        chunked_list.append(list_to_split[start_index:end_index])

    return chunked_list
