# First we assess the number of patients that visit the Lawrenzo Dental clinic
# and write this information to a file for proper storage

num_patients_visited = 0

while True:
    action = input("Enter 'visit' to record a patient visit or 'quit' to exit: ")

    if action == 'visit':
        num_patients_visited += 1
        print("Patient visit recorded.")
    elif action == 'quit':
        print("Exiting the loop.")
        break
    else:
        print("Invalid input. Please try again.")

print("Total patients visited:", num_patients_visited)

# Write patient visit information to a file
filename = "patient_visits.txt"

try:
    with open(filename, "w") as file:
        file.write("Number of patients visited: " + str(num_patients_visited))
    print("Patient visit information written to", filename)
except IOError:
    print("Error writing to the file.")

# Next we assess the number of patients who get treated and the number of doctors that

num_patients_treated = 0
num_doctors_on_duty = 0

# Loop to track the number of patients treated
while True:
    patients_input = input("Enter the number of patients treated (or 'quit' to exit): ")
    if patients_input == 'quit':
        break

    try:
        patients = int(patients_input)
        if patients >= 0:
            num_patients_treated += patients
        else:
            print("Invalid input. Please enter a non-negative number of patients.")
    except ValueError:
        print("Invalid input. Please enter a valid number of patients.")

# Loop to track the number of doctors on duty
num_doctors = int(input("Enter the total number of doctors on duty: "))
for _ in range(num_doctors):
    doctor_status = input("Did the doctor report for duty? (yes/no): ")
    if doctor_status == 'yes':
        num_doctors_on_duty += 1

print("Number of patients treated:", num_patients_treated)
print("Number of doctors on duty:", num_doctors_on_duty)

# Next we go on to check the number of positive and negative reviews we get from our patients

positive_reviews = 0
negative_reviews = 0

while True:
    review = input("Did the patient write a review? (yes/no): ")
    if review == 'yes':
        sentiment = input("Was the review positive or negative? (positive/negative): ")
        if sentiment == 'positive':
            positive_reviews += 1
        elif sentiment == 'negative':
            negative_reviews += 1
        else:
            print("Invalid input. Please enter 'positive' or 'negative'.")
    elif review == 'no':
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print("Number of positive reviews:", positive_reviews)
print("Number of negative reviews:", negative_reviews)
