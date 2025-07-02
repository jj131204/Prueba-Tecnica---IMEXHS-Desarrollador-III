def solve_tower(n, disks):
    source = disks
    # Lista de destino
    target = []
    # Lista auxiliar
    auxiliary = []
    # Lista que guarda todos los movimientos
    moves = []

    # Verfica primero si la lista esta vacia.
    # Si no esta vacia verfica que el tamaño del disco que se quiere colocar sea menor al que ya esta y que el color no sea igual
    def verify_move(top,bottom):
        if not bottom:
            return True
        return top[0] < bottom[0][0] and top[1] != bottom[0][1]

    #funcion para mover el disco.
    def move_disk(source, target, source_label, target_label):

        # Se selecciona el ultimo elemento de la lista y se guarda en disk.
        disk = source.pop()

        # Si no se verifica que se puede mover se retorna falso sino sigue la ejecución.
        if not verify_move(disk, target):
            return False 
        

        target.append(disk)
        moves.append((disk[0], source_label, target_label))
        return True

    def recursive_function(n, source, target, auxiliary, source_label, target_label, auxiliary_label,):
        # Para cuando ya no queden discos que mover
        if n == 0:
            return True
        
        # Se pasa auxiliary como segundo parametro para mover los discos de la torre principal a la auxiliar.
        if not recursive_function(n - 1, source, auxiliary, target, source_label, auxiliary_label, target_label):
            return False

        # Mueve los discos si se puede.
        if not move_disk(source, target, source_label, target_label):
            return False

        #  Se pasa auxiliary como primer parametro y target  segundo parametro para mover los discos de la torre auxiliar a la torre final.
        if not recursive_function(n - 1, auxiliary, target, source, auxiliary_label, target_label, source_label):
            return False

        return True

    if recursive_function(n, source, target, auxiliary, "A", "C", "B"):
        return moves
    else:
        return -1


if __name__ == "__main__":
    # valores para ejecutar la funcion
    n = 3
    disks = [(3, "red"), (2, "blue"), (1, "green")]


    result = solve_tower(n, disks)
    print(result)