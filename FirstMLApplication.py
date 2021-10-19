# My application will take known data about Tuna, Dolphins, and Sharks, and our radar similar ML application
# Will tell us which of the three is most likely approaching the boat.

# Library aka package we will use for machine learning is sklearn lib
# Also on this line, we import the tree from this library.
from sklearn import tree

# I use this to limit the amount of times I have to type print() over and over again
# It also saves valuable time

def print_text(text_to_print):
    print(text_to_print)

# Let the user know what my application is about.
def intro():
    print_text("\n\nYou just purchased a new radar for your fishing boat."
               "\nYou decide to take it out to see if you can use it to identify sea life."
               "\nThe radar can predict what kind of sea life is approaching your boat."
               "\nYou travel to a spot that has lots of large sea life, and test the radar by getting it to identify"
               "\ntuna fishes, dolphins, and sharks.")

    # User input for interaction with user
    repeat = True
    while repeat:
        ans = input("Ready to begin?  Type Y/N\n")

        if ans == "Y" or ans == "y":
            repeat = False
            predict()
        elif ans == "N" or ans == "n":
            exit()
        else:
            print_text("Please type \"Y\" or \"N\"")

def predict():
    # Training data
    # Features - length, # of fins, and MPH in that order
    features = [[83,3,23], [95,3,39],[79,3,41],[106,2,27],[96,3,33],[246,5,14], [289,5,27],[187,5,34],[277,4,18],
                [262,5,21],[59,8,28],[107,7,30],[225,8,19],[137,6,17],[184,8,8]]

    labels = ["Tuna Approaching","Tuna Approaching","Tuna Approaching","Tuna Approaching", "Tuna Approaching",
              "Dolphin Approaching","Dolphin Approaching","Dolphin Approaching", "Dolphin Approaching",
              "Dolphin Approaching", "Shark Approaching", "Shark Approaching", "Shark Approaching",
              "Shark Approaching ", "Shark Approaching"]

    # Training
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features,labels)

    # Use our AI ML app to predict what type of sea life it will be based on the data given
    print("\n\n")
    print("This should be a Tuna with a length of 63\", 3 fins, and traveling at 31 MPH.")
    print(clf.predict([[63,3,31]]))
    print("\nThis should be a Shark with a length of 57\", 8 fins, and traveling at 15 MPH.")
    print(clf.predict([[57,8,15]]))
    print("\nThis should be a Tuna with a length of 94\", 3 fins, and traveling at 42 MPH.")
    print(clf.predict([[94,3,42]]))
    print("\nThis should be a Dolphin with a length of 119\", 5 fins, and traveling at 35 MPH.")
    print(clf.predict([[119,5,35]]))
    print("\nThis should be a Dolphin with a length of 178\", 5 fins, and traveling at 10 MPH.")
    print(clf.predict([[178,5,10]]))

def main():
    intro()

# keeps the program organized
if __name__ == "__main__":
    main()



