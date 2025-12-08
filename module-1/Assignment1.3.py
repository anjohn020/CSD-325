def countdown(bottles):

    current = bottles
    #Loop until only 1 bottle remains
    while current > 1:
        print(f"{current} bottles of beer on the wall, {current} bottles of beer!")
        print("Take one down, pass it around,")

        next_current = current - 1

        #change the song lyric bottles to bottle
        if next_current == 1:
            print("1 bottle of beer on  the wall.\n")

        else:
            print(f"{next_current} bottles of beer on the wall.\n")

        current = next_current

    #one bottle remaining
    print("1 more bottle of beer on the wall, 1 more bottle of beer!")
    print("Take one down, pass it around,")
    print("No more bottles of beer on the wall!\n")


def main():
    bottles = int(input("How many bottles? "))

    countdown(bottles)

    print("Time to buy more beer!")

if __name__ == "__main__":
    main()