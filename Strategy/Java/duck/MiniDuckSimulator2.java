package Strategy.Java.duck;
public class MiniDuckSimulator2 {
    public static void main(String[] args) {
        Duck model = new ModelDuck();
        model.performQuack();
        model.performFly();
        model.setFlyBehavior(new FlyRocketPowered());
        model.performFly();
    }
}
