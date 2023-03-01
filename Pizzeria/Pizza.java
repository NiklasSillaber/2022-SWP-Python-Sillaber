public interface Pizza {

    String backen(){};

    String schneiden(){};

    String einpacken(){};

}

class Salami implements Pizza {

    @Override
    public String backen(){
        return "Salamipizza wird gebacken"
    }

    @Override
    public String schneiden(){
        return "Salamipizza wird geschnitten"
    }

    @Override
    public String einpacken(){
        return "Salamipizza wird eingepackt"
    }

}

class Calzone implements Pizza {

    @Override
    public String backen(){
        return "Calzone wird gebacken"
    }

    @Override
    public String schneiden(){
        return "Calzone wird geschnitten"
    }

    @Override
    public String einpacken(){
        return "Calzone wird eingepackt"
    }

}

class Hawaii implements Pizza {

    @Override
    public String backen(){
        return "Hawaii wird gebacken"
    }

    @Override
    public String schneiden(){
        return "Hawaii wird geschnitten"
    }

    @Override
    public String einpacken(){
        return "Hawaii wird eingepackt"
    }

}