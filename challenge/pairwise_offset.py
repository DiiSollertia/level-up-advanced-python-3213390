def pairwise_offset(sequence: list, fillvalue: str = '*', offset: int = 0) -> tuple:
    # Func accepts all iterables
    if not isinstance(sequence, list):
        # Converted to list to prevent TypeError
        sequence = list(sequence)
    fill = [fillvalue] * offset
    return list(zip(sequence+fill, fill+sequence))
