import javafx.scene.control.Button;
import javafx.scene.layout.Pane;

public class CardButton extends Pane {
    Button card;
    String name;
    public CardButton(Cards aCard, int x, int y){
        Pane aPane = new Pane();
        name = aCard.type;
        card = new Button();
        card.setPrefSize(10,15);
        card.relocate(x,y);
        card.setStyle("-fx-background-color: #ffff00; ");
        aPane.getChildren().addAll(card);
        getChildren().addAll(aPane);
    }
    public void write_type(){
        card.setStyle(name);
    }
    public void erase_type(){
        card.setStyle("");
    }
}
