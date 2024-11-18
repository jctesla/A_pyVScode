def binary_search(list_num , to_search):
    first_index = 0
    size = len(list_num)
    last_index = size - 1
    mid_index = (first_index + last_index) // 2
    # print(mid_index)
    mid_element = list_num[mid_index]
    # print(mid_element)

    # el algoritmo de busqeda se basa en 3 ideas: si el valor q busco está en la mitad ó > mitad ó <mitad.
    is_found = True
    while is_found:
        if first_index == last_index:                                     # valido q la lista no sea vacia.
            if mid_element != to_search:
                is_found = False
                return " Does not appear in the list"

        elif mid_element == to_search:                                    # si de la mitad justo esta el valor q busco.
            return f"{mid_element} occurs in position {mid_index}"

        elif mid_element > to_search:                                     # de la mitad de la lista los valores de la izq x q los los de la
            new_position = mid_index - 1                                  # derecha son > al valor q busco.
            last_index = new_position
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"{mid_element} occurs in position {mid_index}"

        elif mid_element < to_search:                                     # de la mitad de la lista los valores de la derch x q los los de la
            new_position = mid_index + 1                                  # izq son < al valor que busco. 
            first_index = new_position
            last_index = size - 1
            mid_index = (first_index + last_index) // 2                   # de la mitad inicial, vuelvo a sacar otra subMitad de esta lista...asi sucesivamente.
            mid_element = list_num[mid_index]                             
            if mid_element == to_search:
                return f"{mid_element} occurs in position {mid_index}"



list_container = [16 , 18 , 20 , 50 , 60 , 81 , 84 , 89]                  # 1º ante TODO la lista debe ser ordenada de forma Ascendente.
print(binary_search(list_container , 81))                                 # caso en que existe en la lista.
print(binary_search(list_container , 10))                                 # caso e q no existe en la lista pero debemos encontrar la pos q le correspomde, entre q valores.                  