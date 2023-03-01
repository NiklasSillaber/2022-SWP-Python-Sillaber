public interface Pizza {

    void backen();

    void schneiden();

    void einpacken();

}

//Berliner Pizzen

class BerlinSalami implements Pizza {

    @Override
    public void backen() {
        System.out.println( "BerlinSalami wird gebacken");
    }

    @Override
    public void schneiden(){
        System.out.println( "BerlinSalami wird geschnitten");
    }

    @Override
    public void einpacken(){
        System.out.println( "BerlinSalami wird eingepackt");
    }

}

class BerlinCalzone implements Pizza {

    @Override
    public void backen(){
        System.out.println( "BerlinCalzone wird gebacken");
    }

    @Override
    public void schneiden(){
        System.out.println( "BerlinCalzone wird geschnitten");
    }

    @Override
    public void einpacken(){
        System.out.println( "BerlinCalzone wird eingepackt");
    }

}

class BerlinHawaii implements Pizza {

    @Override
    public void backen(){
        System.out.println( "BerlinHawaii wird gebacken");
    }

    @Override
    public void schneiden(){
        System.out.println( "BerlinHawaii wird geschnitten");
    }

    @Override
    public void einpacken(){
        System.out.println( "BerlinHawaii wird eingepackt");
    }

}

//Hamburg Pizzen

class HamburgSalami implements Pizza {

    @Override
    public void backen(){
        System.out.println( "HamburgSalami wird gebacken");
    }

    @Override
    public void schneiden(){
        System.out.println( "HamburgSalami wird geschnitten");
    }

    @Override
    public void einpacken(){
        System.out.println( "HamburgSalami wird eingepackt");
    }

}

class HamburgCalzone implements Pizza {

    @Override
    public void backen(){
        System.out.println( "HamburgCalzone wird gebacken");
    }

    @Override
    public void schneiden(){
        System.out.println( "HamburgCalzone wird geschnitten");
    }

    @Override
    public void einpacken(){
        System.out.println( "HamburgCalzone wird eingepackt");
    }

}

class HamburgHawaii implements Pizza {

    @Override
    public void backen(){
        System.out.println("HamburgHawaii wird gebacken");
    }

    @Override
    public void schneiden(){
        System.out.println( "HamburgHawaii wird geschnitten");
    }

    @Override
    public void einpacken(){
        System.out.println( "HamburgHawaii wird eingepackt");
    }

}