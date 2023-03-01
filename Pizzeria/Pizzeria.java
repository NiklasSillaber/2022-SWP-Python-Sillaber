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

        return pizza;
    }

    //Erstellung spezifisch
    protected abstract Pizza erstellePizza(Pizzasorte sorte);
}

class BerlinPizzeria extends Pizzeria {

    @Override
    protected Pizza erstellePizza(Pizzasorte sorte) {
        Pizza pizza = null;
        switch(sorte) {
            case SAL:
                pizza = new BerlinSalami();
                break;
            case CAL:
                pizza = new BerlinCalzone();
                break;
            case HAW:
                pizza = new BerlinHawaii();
            //festgelegter Default-Favourit
            default:
                pizza = new BerlinSalami();
                break;
        }
         return pizza;
    }
}

class HamburgPizzeria extends Pizzeria {

    @Override
    protected Pizza erstellePizza(Pizzasorte sorte) {
        Pizza pizza = null;
        switch(sorte) {
            case SAL:
                pizza = new HamburgSalami();
                break;
            case CAL:
                pizza = new HamburgCalzone();
                break;
            case HAW:
                pizza = new HamburgHawaii();
            //festgelegter Default-Favourit
            default:
                pizza = new HamburgCalzone();
                break;
        }
        return pizza;
    }
}