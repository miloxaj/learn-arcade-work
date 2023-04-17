class Room:
    def __init__(self,habitacion,norte,sur,este,oeste):
        self.description=""
        self.norte= norte
        self.sur = sur
        self.este = este
        self.oeste = oeste
def main():
    room_list=[]
    room = Room("Patio", 3,None,1, None)
    room_list.append(room)
    room = Room("Te encuentras en el salón principal, donde puedes ver un gran ventanal, un sofacama y una tv ultra wide.", 4,None, 2, 0)
    room_list.append(room)
    room = Room("cocina", 5, None, None, 1)
    room_list.append(room)
    room = Room("Habitacioon principal", None, 0, 4, None)
    room_list.append(room)
    room = Room("Pasillo principal", 6, 1,5, 3)
    room_list.append(room)
    room = Room("Habitacion de los muertos ", None, 2,None,4 )
    room_list.append(room)
    room = Room("Balcon de los suicidios", None, 4, None, None)
    room_list.append(room)
    current_room=0
    print(room_list[current_room].description)
main()