

public class Cards {
    String type;
    Boolean showingType;
     public Cards(String initType){
         type = initType;
         showingType = false;
     }

    public String toString() {
        return type;
    }
}
