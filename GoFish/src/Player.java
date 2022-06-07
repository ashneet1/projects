public class Player {
    private String name;
    private int chances;
    private int points;

    public Player(String initName, int initChances){
        name = initName;
        chances = initChances;
        points = 0;
    }

    public String get_name(){return name;}
    public int get_chances(){return chances;}
    public int get_points(){return points;}

    public void decrease_chances(int chances){chances -= 1;}
    public void add_points(int points){points +=1;}
}
