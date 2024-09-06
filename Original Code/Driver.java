import java.util.ArrayList;
import java.util.Scanner;

public class Driver {
    private static ArrayList<Dog> dogList = new ArrayList<Dog>();
    private static ArrayList<Monkey> monkeyList = new ArrayList<Monkey>(); //Creating Array list for Monkey.

    public static void main(String[] args) {
		Scanner scnr = new Scanner(System.in); //Creating a Scanner for user input.
        initializeDogList();
        initializeMonkeyList();
		String usrInput;                       //Creating a placeholder string for inputs.
		
		usrInput = "";                         //Instantiating usrInput
		
		while (!usrInput.equals("q")) {        //While loop that will keep menu displayed until user presses "q"
			displayMenu();
			usrInput = scnr.next();
			
			if (usrInput.equals("1")) {         //If user inputs 1, it will invoke the intakeNewDog method.
				System.out.println("Beginning Dog Intake");
				intakeNewDog(scnr);
			}
			
			else if (usrInput.equals("2")) {    //If user inputs 2, it will invoke the intakeNewMonkey method.
				System.out.println("Beginning Monkey Intake");
				intakeNewMonkey(scnr);
			}
			
			else if (usrInput.equals("3")) {    //If user inputs 3, it will invoke the reserveAnimal method.
				System.out.println("Beginning Animal Reservation");
				reserveAnimal(scnr);
			}

			else if (usrInput.equals("4")) {    //If user inputs 4, 5, or 6 it will invoke the printAnimals method.
				System.out.println("Displaying List of dogs");
				printAnimals(1);
			}

			else if (usrInput.equals("5")) {
				System.out.println("Displaying List of monkeys");
				printAnimals(2);	
			}

			else if (usrInput.equals("6")) {
				System.out.println("Displaying List of unreserved animals");
				printAnimals(3);
			}
			
			else if (usrInput.equals("q")) {   //If user inputs "q" it will quit the loop and exit the program.
				System.out.println("Quitting.");
			}
			
			else {                             //If user inputs any other char it will respond invalid command and request a new input.
				System.out.println("Invalid command.");
			}
		}	
				
	}

    // This method prints the menu options
    public static void displayMenu() {
        System.out.println("\n\n");
        System.out.println("\t\t\t\tRescue Animal System Menu");
        System.out.println("[1] Intake a new dog");
        System.out.println("[2] Intake a new monkey");
        System.out.println("[3] Reserve an animal");
        System.out.println("[4] Print a list of all dogs");
        System.out.println("[5] Print a list of all monkeys");
        System.out.println("[6] Print a list of all animals that are not reserved");
        System.out.println("[q] Quit application");
        System.out.println();
        System.out.println("Enter a menu selection");
    }


    // Adds dogs to a list for testing
    public static void initializeDogList() {
        Dog dog1 = new Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "intake", false, "United States");
        Dog dog2 = new Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "In service", false, "United States");
        Dog dog3 = new Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", true, "Canada");

        dogList.add(dog1);
        dogList.add(dog2);
        dogList.add(dog3);
    }


    // Adds monkeys to a list for testing
    //Optional for testing
    public static void initializeMonkeyList() {
		Monkey monkey1 = new Monkey("Chunky", "Capuchin", "male", "2", "35.6", "12", "6", "6", "1", "2", "1", "12-12-2020", "India", "in service", false, "Canada");
		Monkey monkey2 = new Monkey("Becky", "Macaque", "female", "5", "32.3", "10", "2", "3", "2", "3", "1", "01-11-2017", "China", "in service", true, "Mexico");
		
		monkeyList.add(monkey1);
		monkeyList.add(monkey2);
    }


    // Complete the intakeNewDog method
    // The input validation to check that the dog is not already in the list
    // is done for you
    public static void intakeNewDog(Scanner scanner) {
        scanner.nextLine();
    	System.out.println("What is the dog's name?");
        String name = scanner.nextLine();
        for(Dog dog: dogList) {
            if(dog.getName().equalsIgnoreCase(name)) {
                System.out.println("\n\nThis dog is already in our system\n\n");
                return; //returns to menu
            }
        }
		System.out.println("Adding Dog: " + name);                          //Print statement confirming name entered
		
		System.out.println("What is the dog's breed?");                     //Output requesting species
		String breed = scanner.nextLine();                                  //Input from User
		System.out.println("Breed: " + breed);                              //Print statement confirming species
				
		System.out.println("What is the dog's gender?");                    //Output requesting gender
		String gender = scanner.nextLine();                                 //Input from User
		System.out.println("Gender: " + gender);                            //Print statement confirming gender
			
		System.out.println("What is the dog's age?");                         //Output requesting age
		String age = scanner.nextLine();                                      //Input from User
		System.out.println("Age: " + age);                                    //Print statement confirming age
				
		System.out.println("What is the dog's weight?");                      //Output requesting weight
		String weight = scanner.nextLine();                                   //Input from User
		System.out.println("Weight: " + weight);                              //Print statement confirming weight
				
		System.out.println("When was the dog acquired? Format: mm-dd-yyyy");  //Output requesting date dog was acquired
		String acquisitionDate = scanner.nextLine();                          //Input from User
		System.out.println("Dog Acquired: " + acquisitionDate);               //Print statement confirming date acquired

		System.out.println("What Country did the dog come from?");            //Output requesting what country dog came from
		String acquisitionCountry = scanner.nextLine();                       //Input from User
		System.out.println("Country of Origin: " + acquisitionCountry);       //Print statement confirming country of origin

		System.out.print("What is the dog's training status?");                              //Output requesting training status of dog
		System.out.println("Phase I, Phase II, Phase III, Phase IV, Phase V, or In Service");//Provide options
		String trainingStatus = scanner.nextLine();                                          //Input from User
		System.out.println("Training Status: " + trainingStatus);                            //Print statement confirming training status

		System.out.println("Has this dog been reserved? (True or False)");    //Output requesting if dog has been reserved yet
		String reservedTemp = scanner.nextLine();                             //Input from User
		System.out.println("Reservation Status: " + reservedTemp);            //Print Statement confirming reservation status
		boolean reserved = Boolean.parseBoolean(reservedTemp);                //Change reservedTemp to boolean reserved

		System.out.println("What country is the dog in service?");            //Output requesting service country of dog
		String inServiceCountry = scanner.nextLine();                         //Input from User
		System.out.println("Country of Service: " + inServiceCountry);        //Print statement confirming service country
		
		//Setting data and instantiating user inputs into a new dog list.
		Dog dog4 = new Dog(name, breed, gender, age, weight, acquisitionDate, 
				acquisitionCountry, trainingStatus, reserved, inServiceCountry);
		//adding the new list created from user input into Arraylist dogList.
		dogList.add(dog4);
		System.out.println("New Dog " + name + " added!");
    }

        public static void intakeNewMonkey(Scanner scanner) {
        	scanner.nextLine();
        	System.out.println("What is the Monkey's name?");                             //Output requesting Monkey Name
        	String name = scanner.nextLine();                                             //Input from Use
    		for(Monkey monkey: monkeyList) {                                              //for loop to check against existing Monkeys in array.
    			if(monkey.getName().equalsIgnoreCase(name)) {                             //If statement checking against name of Monkey.
    				System.out.println("\n\nThis Monkey is already in our system\n\n");   //If Monkey name is already in system, output saying so and 
    				return;                                                               //Returns to previous menu
    			}
    		}
    		System.out.println("Adding Monkey: " + name);                         //Print statement confirming name entered
    		System.out.println("What is the Monkey's species?");                  //Output requesting species
    		String species = scanner.nextLine();                                  //Input from User
    		if(!(species.equalsIgnoreCase("Capuchin")) && !(species.equalsIgnoreCase("Guenon")) &&             //Added in an if statement
    				!(species.equalsIgnoreCase("Macaque")) && !(species.equalsIgnoreCase("Marmoset")) &&       //to compare species to known approved list
    				!(species.equalsIgnoreCase("Squirrel Monkey")) && !(species.equalsIgnoreCase("Tamarin"))) {//if not approved will return to main menu
    			System.out.println("This monkey species is not allowed. Please choose another.");
    			return;
    		}
    		System.out.println("Species: " + species);                            //Print statement confirming species
    				
    		System.out.println("What is the Monkey's gender?");                   //Output requesting gender
    		String gender = scanner.nextLine();                                   //Input from User
    		System.out.println("Gender: " + gender);                             //Print statement confirming gender
    			
    		System.out.println("What is the Monkey's age?");                      //Output requesting age
    		String age = scanner.nextLine();                                      //Input from User
    		System.out.println("Age: " + age);                                    //Print statement confirming age
    				
    		System.out.println("What is the Monkey's weight?");                   //Output requesting weight
    		String weight = scanner.nextLine();                                   //Input from User
    		System.out.println("Weight: " + weight);                              //Print statement confirming weight
    				
    		System.out.println("What is the Monkey's tail length?");              //Output requesting tail length
    		String tailLength = scanner.nextLine();                               //Input from User
    		System.out.println("Tail Length: " + tailLength);                     //Print statement confirming tail length
    				
    		System.out.println("What is the Monkey's height?");                   //Output requesting height
    		String height = scanner.nextLine();                                   //Input from User
    		System.out.println("Height: " + height);                              //Print statement confirming height

    		System.out.println("What is the Monkey's body length?");              //Output requesting body length
    		String bodyLength = scanner.nextLine();                               //Input from User
    		System.out.println("Body Length: " + bodyLength);                     //Print statement confirming body length
     
    		System.out.println("What is the Monkey's torso length?");             //Output requesting torso length
    		String torsoLength = scanner.nextLine();                              //Input from User
    		System.out.println("Torso Length: " + torsoLength);                   //Print statement confirming torso length

    		System.out.println("What is the Monkey's skull length?");             //Output requesting skull length
    		String skullLength = scanner.nextLine();                              //Input from User
    		System.out.println("Skull Length: " + skullLength);                   //Print statement confirming skull length

    		System.out.println("What is the Monkey's neck length?");              //Output requesting neck length
    		String neckLength = scanner.nextLine();                               //Input from User
    		System.out.println("Neck Length: " + neckLength);                     //Print statement confirming neck length

    		System.out.println("When was the Monkey Acquired? Format: mm-dd-yyyy");//Output requesting date monkey was acquired
    		String acquisitionDate = scanner.nextLine();                           //Input from User
    		System.out.println("Monkey Acquired: " + acquisitionDate);             //Print statement confirming date acquired

 			System.out.println("What Country did the Monkey come from?");         //Output requesting what country monkey came from
    		String acquisitionCountry = scanner.nextLine();                       //Input from User
    		System.out.println("Country of Origin: " + acquisitionCountry);       //Print statement confirming country of origin

    		System.out.print("What is the Monkey's training status?");                           //Output requesting training status of monkey
    		System.out.println("Phase I, Phase II, Phase III, Phase IV, Phase V, or In Service");//Provide options
    		String trainingStatus = scanner.nextLine();                                          //Input from User
    		System.out.println("Training Status: " + trainingStatus);                            //Print statement confirming training status

    		System.out.println("Has this Monkey been reserved? (True or False)"); //Output requesting if monkey has been reserved yet
    		String reservedTemp = scanner.nextLine();                             //Input from User
    		System.out.println("Reservation Status: " + reservedTemp);            //Print Statement confirming reservation status
    		boolean reserved = Boolean.parseBoolean(reservedTemp);                //Change reservedTemp to boolean reserved

    		System.out.println("What country is the Monkey in service?");         //Output requesting service country of monkey
    		String inServiceCountry = scanner.nextLine();                         //Input from User
    		System.out.println("Country of Service: " + inServiceCountry);        //Print statement confirming service country
    		
    		//Setting data and instantiating user inputs into a new monkey list.
    		Monkey monkey3 = new Monkey(name, species, gender, age, weight, tailLength, height, bodyLength, 
    				torsoLength, skullLength, neckLength, acquisitionDate, acquisitionCountry, trainingStatus, 
    				reserved, inServiceCountry);
    		//adding the new list created from user input into Arraylist monkeyList.
    		monkeyList.add(monkey3);
    		System.out.println("New Monkey " + name + " added!");
        }
        
        public static void reserveAnimal(Scanner scanner) {
        	scanner.nextLine();
        	System.out.println("Please enter the animal type you would like to reserve. (Dog or Monkey)");               //Print message requesting animal type
        	String animalType = scanner.nextLine();                                                                      //User input to gather response
        	if(animalType.equalsIgnoreCase("Monkey")) {                                                                  //Checking for monkey entry
        		System.out.println("Please enter the service country.");                                                 //Print requesting service country
        		String inServiceCountry = scanner.nextLine();                                                            //User input to gather response
        		for(Monkey monkey: monkeyList) {                                                                         //Checking against monkeyList
        			if(monkey.getInServiceLocation().equalsIgnoreCase(inServiceCountry)) {                               //Checking if there are monkeys in country
        				if (monkey.getReserved() == true) {                                                              //If there are, checking if they are reserved
        					System.out.println("\n\nThere are no monkeys available in " + inServiceCountry);             //If they are reserved print message saying so
        					return;
        				}
        				else if (monkey.getReserved() == false) {                                                           //Checking if monkeys are reserved
            				System.out.println("Monkey " + monkey.getName() + " is available in " + inServiceCountry + ".");//If they are not reserved, say as much
            				System.out.println("Would you like to reserve it? (Enter: Yes or No)");                         //Message asking if they want to reserve
            				String responseTemp = scanner.nextLine();                                                       //User input to gather response
            				if (responseTemp.equalsIgnoreCase("Yes")) {                                                     //Check if user response is yes
            					monkey.setReserved(true);                                                                   //If yes, use setReserved to set to reserved
            					System.out.println("Monkey " + monkey.getName() + " has been reserved!");                   //Print message affirming reservation
            					return;
            				}
            				else if (responseTemp.equalsIgnoreCase("No")) {                                                 //Check if user response is no
            					System.out.println("Leaving monkey " + monkey.getName() + " unreserved.");                  //If no, change nothing and confirm no change
            					return;
            				}
        				}
        			}
        		}		
        	}
        	else if(animalType.equalsIgnoreCase("Dog")) {                                                                //Checking for dog response
        		System.out.println("Please enter the service country.");                                                 //Print requesting service country
        		String inServiceCountry = scanner.nextLine();                                                            //User input to gather response  
        		for(Dog dog: dogList) {                                                                                  //Checking against monkeyList
        			if(dog.getInServiceLocation().equalsIgnoreCase(inServiceCountry)) {                                  //Checking if there are dogs in country
        				if (dog.getReserved() == true) {                                                                 //If there are, checking if they are reserved
        					System.out.println("\n\nThere are no dogs available in " + inServiceCountry);                //If they are reserved print message saying so
        					return;
        				}
        				else if (dog.getReserved() == false) {                                                           //Checking if dogs are reserved
            				System.out.println("Dog " + dog.getName() + " is available in " + inServiceCountry + ".");   //If they are not reserved, say as much
            				System.out.println("Would you like to reserve it? (Enter: Yes or No)");                      //Message asking if they want to reserve
            				String responseTemp = scanner.nextLine();                                                    //User input to gather response
            				if (responseTemp.equalsIgnoreCase("Yes")) {                                                  //Check if user response is yes
            					dog.setReserved(true);                                                                   //If yes, use setReserved to set to reserved
            					System.out.println("Dog " + dog.getName() + " has been reserved!");                      //Print message affirming reservation
            					return;
            				}
            				else if (responseTemp.equalsIgnoreCase("No")) {                                              //Check if user response is no
            					System.out.println("Leaving dog " + dog.getName() + " unreserved.");                     //If no, change nothing and confirm no change
            					return;
            				}
        				}
        			}
        		}
        	}

        }

        public static void printAnimals(int choice) {
            if(choice == 1) { 
            	System.out.println("The method printAnimals for dogs needs to be implemented"); //If user pressed 4 from displayMenu() 
            }                                                                                   //then printAnimals(1) was passed.
            else if(choice == 2) {
            	System.out.println("The method printAnimals for monkeys needs to be implemented");//If user pressed 5 from displayMenu()
            }                                                                                     //then printAnimals(2) was passed.
            else if(choice == 3) {
            	System.out.println("Getting Available Dogs:\n");                                                //If user pressed 6 from displayMenu()
            	for(Dog dog: dogList) {                                                                         //then printAnimals(2) was passed
                    if(dog.getReserved() == false && dog.getTrainingStatus().equalsIgnoreCase("In Service")) {  //if statement checking against reserved and in service
                    	System.out.println("The dog: " + dog.getName() + " is available.");                     //if in service, but not reserved
                    	System.out.println(dog.getName() + " is from: " + dog.getAcquisitionLocation());        //will print the animals information.
                    	System.out.println(dog.getName() + "'s current status is: " + dog.getTrainingStatus()); //2 instances of this process one for dog and monkey
                    	System.out.println();
                    }
            	}
                System.out.println("Getting Available Monkeys.\n");
                for(Monkey monkey: monkeyList) {
                	if(monkey.getReserved() == false && monkey.getTrainingStatus().equalsIgnoreCase("In Service")) {
                    	System.out.println("The Monkey: " + monkey.getName() + " is available.");
                    	System.out.println(monkey.getName() + " is from: " + monkey.getAcquisitionLocation());
                    	System.out.println(monkey.getName() + "'s current status is: " + monkey.getTrainingStatus());
                    	System.out.println();
                	}
                }
            }
        }
}

