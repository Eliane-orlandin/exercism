public class Lasagna {
    public int expectedMinutesInOven(){
        return 40; 
    } 
    public int remainingMinutesInOven(int actualMinutes) {
        return expectedMinutesInOven() - actualMinutes;    
    }
    public int preparationTimeInMinutes(int numberOfLayers){
        return  numberOfLayers * 2;
    }
    public int totalTimeInMinutes(int numberOfLayers, int actualMinutesInOven){
        int preparationTime = preparationTimeInMinutes(numberOfLayers);
        int ovenTime = actualMinutesInOven;
        return preparationTime + ovenTime;
    }
    
}
