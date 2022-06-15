import java.util.ArrayList;

public class GoFish {

    private ArrayList<Cards> allCards;
    String[] typeCard;

    public GoFish() {
        allCards = new ArrayList<Cards>();
        typeCard = new String[]{ "King","Queen","Jack","1","2","3","4","5","6","7","8","9","10" };
    }
    public ArrayList<Cards> make_cards(int amount){
        for (int i = 0; i < amount*2; i++) {
            int no = (int) Math.floor(Math.random() * typeCard.length);
            Cards aCard = new Cards(typeCard[no]);
            Cards bCard = new Cards(typeCard[no]);
            allCards.add(aCard);
            allCards.add(bCard);
        }
        return allCards;
    }


}
