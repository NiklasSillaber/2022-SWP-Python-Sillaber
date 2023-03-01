enum Pizzasorte {
    CAL, SAL, HAW 
}

public abstract class Pizzeria {

    public Pizza verarbeitePizza(Pizzasorte sorte) {
        //Erstellen
        Pizza pizza = erstellePizza(sorte);
        //Verarbeiten immer gleich
        pizza.backen();
        pizza.schneiden();
        pizza.einpacken();
    }

    //Erstellung spezifisch
    protected abstract Pizza erstellePizza(Pizzasorte sorte);
}

class BerlinPizzeria extends Pizzeria {

    @Override
    protected Pizza erstellePizza(Pizzasorte sorte) {
        switch(sorte) {
            
        }
    }
}