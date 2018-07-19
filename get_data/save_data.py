def save_data(data, name) :

    opened = open("../profils/" + name + ".dt", "a+")
    if not opened :
        return
    
    for image in data :
        for line in image :
            for pixel in line :
                opened.write(str(pixel))
                opened.write(" ")
            opened.write("\n")

    print("we got", len(data), "images :")