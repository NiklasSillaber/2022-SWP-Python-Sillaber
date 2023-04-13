package Patterns.FactoryPattern;

public class Main {

    public static void main(String []args) {
        //Hmaburg
        Pizzeria hamburgPizzeria = new HamburgPizzeria();
        Pizza HamburgCalzone = hamburgPizzeria.verarbeitePizza(Pizzasorte.CAL);

        //Berlin
        Pizzeria berlinPizzeria = new BerlinPizzeria();
        Pizza BerlinSalami = berlinPizzeria.verarbeitePizza(Pizzasorte.SAL);
    }

}