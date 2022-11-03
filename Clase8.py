
    #    Hacé un programa que te permita jugar a “Piedra, papel o tijera”. En primer lugar, la
    #    aplicación solicita el nombre de cada gamer, después empieza el juego. El juego consiste
    #    en pedir qué opción elije cada uno y sumar puntos al winner —si lo hay—. Definí y utilizá
    #    una función llamada cualGana con dos parámetros con las jugadas de cada uno, que
    #    devuelve 0 en caso de empate, 1 si gana el primero, 2 si gana el segundo. El juego termina
    #    cuando el primero elije “*” como indicador de final.*/]

        System.out.println("Juego piedra-papel-tijera");
        Scanner teclado = new Scanner(System.in);
        String entrada = "";
        String nombre;
        String nombreB;
        int score;
        int empate = 0;
        int jug1 = 0;
        int jug2 = 0;

        System.out.println("Ingrese su nombre Gamer 1");
        nombre = teclado.nextLine();
        System.out.println("Ingrese su nombre Gamer2");
        nombreB = teclado.nextLine();

        while( !entrada.equals("*")){
            System.out.print("Indique su seleccion [1=Piedra, 2=Papel, 3=Tijera]: ");
            int jugadaGamer1 = teclado.nextInt();
            System.out.print("Ahora el Gamer2: ");
            int jugadaGamer2 = teclado.nextInt();
            score = cualgana(jugadaGamer1,jugadaGamer2);
            if(score == 0){
                empate = empate +1;
            }else if(score == 1){
                jug1 = jug1 + 1;
            }else if(score == 2){
                jug2 = jug2 + 1;
            }
            System.out.println ("Ejecutar de nuevo?");
            System.out.println("S/*");
            entrada = teclado.next();

        }

        System.out.println("El score del "+nombre+" es: "+jug1);
        System.out.println("El score del "+nombreB+" es: "+jug2);
        System.out.println("La cantidad de empates fue: "+empate);


    }

    public static int cualgana(int jugada1, int jugada2){
        int respuesta = 0;
        switch ( jugada1 )
        {
            case 1:
                System.out.println("Piedra");
                switch ( jugada2 )
                {
                    case 1: respuesta = 0;System.out.println("Empate!"); break;
                    case 2: respuesta = 2;System.out.println("Jugador2 gana!"); break;
                    case 3: respuesta = 1;System.out.println("Jugador1 gana!"); break;
                }
                break;

            case 2:
                System.out.println("Papel");
                switch ( jugada2 )
                {
                    case 1: respuesta = 1; System.out.println("Jugador1 gana!"); break;
                    case 2: respuesta = 0; System.out.println("Empate!"); break;
                    case 3: respuesta = 2; System.out.println("Jugador2 gana!"); break;
                }
                break;

            case 3:
                System.out.println("Tijera");
                switch ( jugada2 )
                {
                    case 1: respuesta = 2; System.out.println("Jugador2 gana!"); break;
                    case 2: respuesta = 1; System.out.println("Jugador1 gana!"); break;
                    case 3: respuesta = 0; System.out.println("Empate!"); break;
                }
                break;
        }
        return respuesta;
    }
