/**
* Module Five Milestone: Monkey Class
* Author: Richard VanSkike
* Date: February 6 2021
*/

public class Monkey extends RescueAnimal{
	//Instance variables for Monkey Class
	private String species;
	private String tailLength; 
	private String height; 
	private String bodyLength;
	private String torsoLength;
	private String skullLength;
	private String neckLength;
	
	// Constructor for Monkey.
    public Monkey(String name, String species, String gender, String age, String weight, 
	String tailLength, String height, String bodyLength, String torsoLength, String skullLength, 
	String neckLength, String acquisitionDate, String acquisitionCountry,
	String trainingStatus, boolean reserved, String inServiceCountry) {
        setName(name);
        setSpecies(species);
        setGender(gender);
        setAge(age);
        setWeight(weight);
		setTailLength(tailLength);
		setHeight(height);
		setBodyLength(bodyLength);
		setTorsoLength(torsoLength);
		setSkullLength(skullLength);
		setNeckLength(neckLength);
        setAcquisitionDate(acquisitionDate);
        setAcquisitionLocation(acquisitionCountry);
        setTrainingStatus(trainingStatus);
        setReserved(reserved);
        setInServiceCountry(inServiceCountry);
	}
	
	//Getter and Setter method for species
	public String getSpecies() {
		return species;
	}
	
	public void setSpecies(String species) {
		this.species = species;
	}

	//Getter and Setter method for tailLength
	public String getTailLength() {
	   return tailLength;  
	}

	public void setTailLength(String tailLength) {
	   this.tailLength = tailLength;
	}

	//Getter and Setter method for height
	public String getHeight() {
	   return height;
	}

	public void setHeight(String height) {
	   this.height = height;
	}

	//Getter and Setter method for bodyLength
	public String getBodyLength() {
	   return bodyLength;
	}

	public void setBodyLength(String bodyLength) {
	   this.bodyLength = bodyLength;
	}

	//Getter and Setter method for torsoLength
	public String getTorsoLength() {
	   return torsoLength;
	}

	public void setTorsoLength(String torsoLength) {
	   this.torsoLength = torsoLength;
	}

	//Getter and Setter method for skullLength
	public String getSkullLength() {
	   return skullLength;
	}

	public void setSkullLength(String skullLength) {
	   this.skullLength = skullLength;
	}

	//Getter and Setter method for neckLength
	public String getNeckLength() {
	   return neckLength;
	}

	public void setNeckLength(String neckLength) {
	   this.neckLength = neckLength;
	}
}