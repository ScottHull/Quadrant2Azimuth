import os, time, csv


home_dir_list = []
home_dir_list.append(os.getcwd())



def initialization():
    print("_____________________________________________________\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Quadrant to Azimuth Converter")
    print("Scott D. Hull, 2016\n\n")
    print("Please enter your .csv filename.")
    if "Quad2Adi_Out.csv" in os.listdir(home_dir_list[0]):
        os.remove("Quad2Adi_Out.csv")
    else:
        pass
    if "temp.csv" in os.listdir(home_dir_list[0]):
        os.remove("temp.csv")
    else:
        pass
    output_file = open("Quad2Adi_Out.csv", 'a')
    workbook = input(">>> ")
    if os.path.isfile(workbook):
        print("\n" + workbook + " has been found in the working directory!\n")
        time.sleep(0.5)
        pass
    else:
        print("\n" + workbook + " has NOT been found in the working directory!\n")
        time.sleep(0.5)
        output_file.close()
        initialization()
    raw_vals = []
    clipped_vals = []
    with open(workbook, 'r') as infile:
        reader = csv.reader(infile, delimiter=",")
        for row in reader:
            # print(row)
            raw_vals.append(row[0])
    # print(raw_vals)
    for i in raw_vals:
        try:
            clipped_vals = []
            clipped_vals.append(int(i[1:-1]))
            azimuth = []
            if "N" in i:
                if "W" in i:
                    val1 = 360 - clipped_vals[0]
                    # print(val1)
                    writethis = i + "," + str(val1)
                    print(writethis)
                    output_file.write("%s\n" % writethis)
                elif "E" in i:
                    val1 = 0 + clipped_vals[0]
                    # print(val1)
                    writethis = i + "," + str(val1)
                    print(writethis)
                    output_file.write("%s\n" % writethis)
            elif "S" in i:
                if "W" in i:
                    val1 = 180 + clipped_vals[0]
                    writethis = i + "," + str(val1)
                    print(writethis)
                    output_file.write("%s\n" % writethis)
                elif "E" in i:
                    val1 = 180 - clipped_vals[0]
                    writethis = i + "," + str(val1)
                    print(writethis)
                    output_file.write("%s\n" % writethis)
            elif "n" in i:
                if "w" in i:
                    val1 = 360 - clipped_vals[0]
                    # print(val1)
                    writethis = i + "," + str(val1)
                    print(writethis)
                    output_file.write("%s\n" % writethis)
                elif "e" in i:
                    val1 = 0 + clipped_vals[0]
                    # print(val1)
                    writethis = i + "," + str(val1)
                    print(writethis)
                    output_file.write("%s\n" % writethis)
            elif "s" in i:
                if "w" in i:
                    val1 = 180 + clipped_vals[0]
                    writethis = i + "," + str(val1)
                    print(writethis)
                    output_file.write("%s\n" % writethis)
                elif "e" in i:
                    val1 = 180 - clipped_vals[0]
                    writethis = i + "," + str(val1)
                    print(writethis)
                    output_file.write("%s\n" % writethis)
            else:
                print("\nThere was an error reading: " + i + "!\n")
                writethis = i + ",ERROR"
                output_file.write("%s\n" % writethis)
        except:
            print("Error with attitude: " + str(i) + " ...")
            pass
    output_file.close()
    print("\nDone converting quadrant to azimuth!")
    print("Please see '" + home_dir_list[0] + "' for the output file!\n")
    time.sleep(1)
    print("_____________________________________________________\n")



initialization()

