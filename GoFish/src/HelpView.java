import javafx.scene.control.Button;
import javafx.scene.layout.Pane;
import javafx.collections.FXCollections;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.layout.Pane;
import javafx.scene.control.TextField;

public class HelpView extends Pane{
    Label label1;
    Label label2;
    Button back;
    public HelpView(){
        label1 = new Label("INSTRUCTIONS");
        label1.setStyle("-fx-font: 20 arial;");
        label1.relocate(150,10);

        back = new Button("Back");
        back.setStyle("-fx-font: 12 arial;");
        back.relocate(10,400);
        back.setPrefSize(100,50);

        getChildren().addAll(label1,back);
        setPrefSize(500,500);
    }
}
