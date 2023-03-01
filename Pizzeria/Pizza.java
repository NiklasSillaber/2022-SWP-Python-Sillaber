public interface Pizza {

    Pizza(String ort);

    String backen(){};

    String schneiden(){};

    String einpacken(){};

}

class Salamipizza implements Pizza {

    @Override
    public

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

class Calzonepizza implements Pizza {

    @Override
    public String backen(){
        return "Calzonepizza wird gebacken"
    }

    @Override
    public String schneiden(){
        return "Calzonepizza wird geschnitten"
    }

    @Override
    public String einpacken(){
        return "Calzonepizza wird eingepackt"
    }

}

class Hawaiipizza implements Pizza {

    @Override
    public String backen(){
        return "Hawaiipizza wird gebacken"
    }

    @Override
    public String schneiden(){
        return "Hawaiipizza wird geschnitten"
    }

    @Override
    public String einpacken(){
        return "Hawaiipizza wird eingepackt"
    }

}