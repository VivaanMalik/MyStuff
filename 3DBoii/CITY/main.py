import grid
import buildboii
def main():
    confirm='n'
    while confirm=='n':
        sizex=int(input('Size X:\n'))
        sizey=int(input('Size Y:\n'))
        Grid=grid.gengrid((sizex, sizey), (0,0), view=True)
        # Sends grid coords shit to da marker.py to mark them for 3d mooodeeell boiz
        confirm=input('Is dis okay??? [y/n]\n')
if __name__ == '__main__':
    main()