package Patterns.StrategyPattern;

public class main {
    public static void main(String[] args) {
        Kamel big = new BigKamel();
        Kamel small = new SmallKamel();
        big.trinken();
        small.trinken();
        big.setLaufverhalten(new SchnellLaufen());
        big.laufen();
        small.laufen();
    }
}