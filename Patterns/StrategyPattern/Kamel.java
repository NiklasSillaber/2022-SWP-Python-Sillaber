package Patterns.StrategyPattern;

public abstract class Kamel{
    private Trinkverhalten tVerhalten;
    private Laufverhalten lVerhalten;

    public void setTrinkverhalten(Trinkverhalten t){
        this.tVerhalten = t;
    }

    public void setLaufverhalten(Laufverhalten l){
        this.lVerhalten = l;
    }

    public void trinken(){
        tVerhalten.trinken();
    }

    public void laufen(){
        lVerhalten.laufen();
    }
}

class BigKamel extends Kamel{
    public BigKamel(){
        setTrinkverhalten(new VielTrinken());
        setLaufverhalten(new LangsamLaufen());
    }
}

class SmallKamel extends Kamel{
    public SmallKamel(){
        setTrinkverhalten(new WenigTrinken());
        setLaufverhalten(new SchnellLaufen());
    }
}
