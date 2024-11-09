import random
set = [["Neck", "Calves", "Abs", "Biceps"],
    ["Thighs", "Chest", "Triceps", "Obliques", "Traps"],
    ["Forearms", "Hamstrings", "Shoulder", "Back"]]


workout_listings = [[["Side Dumbbell shrugs","Front Dumbbell shrugs"],
                [ "normal calve raises","Dumbbell outer calf raises"],
                ["Dumbbell crunch", "Dumbbell crunch reach"],
                ["Dumbbell biceps curl", "Alternating dumbbell biceps curl","Dumbbell hammer curl"]],
    [["Dumbbell squat", "Dumbbell lunge", "Dumbbell reverse lunge"],
    ["normal pushups", "military pushups", "wide arm pushups", "chest side flyes", "Dumbbell pullovers"],
    ["triceps kickbacks", "Dumbbell triceps extension"], 
    ["Dumbbell halo", "Dumbbell Russian twist", "Dumbbell side bend"], 
    ["Side Dumbbell shrugs", "Front Dumbbell shrugs"]],
                [["wrist curl", "Dumbbell hammer curl","Dumbbell zott man curl"],
                ["Dumbbell good mornings", "Dumbbell Romanian Deadlift"], 
                ["Dumbbell shoulder press", "Dumbbell Arnold press", "Dumbbell side raise", "Dumbbell front raise", "Single-arm dumbbell shoulder press"], 
                ["Dumbbell reverse-grip bent-over row", "Dumbbell reverse flye ", "Dumbbell deadlift"]]]


workout_mapping = {}

while True:
    with open("Fitnessfile.txt", "r") as fitnessfile:
         output = fitnessfile.read()
         print(f"You chose set {output} the last time.")

    workout_set = input("What set do you want to perform today: ")

    if workout_set == "1" or workout_set == "2" or workout_set == "3":
        with open("Fitnessfile.txt", "w") as fitnessfile:
             fitnessfile.write(workout_set)

        workout_set = int(workout_set)

        for i, member in enumerate(set[workout_set-1]):
                workout_mapping[member] = random.choice(workout_listings[workout_set-1][i])

        for keys, values in workout_mapping.items():
            print(f"{keys:10} : {values}")
        break                              
    else:
        print("Enter a number from 1 to 3")
