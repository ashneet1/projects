import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;
import javafx.event.*;

public class GoFishApp extends Application {
    MainPageView helpView;
    public void start(Stage primaryStage) {
        Pane aPane = new Pane();

        helpView = new MainPageView();
        aPane.getChildren().add(helpView);

        primaryStage.setTitle("GO FISH");
        primaryStage.setResizable(false);
        primaryStage.setScene(new Scene(aPane));
        primaryStage.show();
    }
}
