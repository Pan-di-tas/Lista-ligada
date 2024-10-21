import java.util.LinkedList;

class main{

    public static void main(String[] args) {
        LinkedList lista = new LinkedList<>();

        lista.add("Palabra");
        lista.add(5);
        lista.add(17);
        lista.add("Palabra 2");
        lista.add("Juancho");

        lista.removeLast();

        System.out.println("El tamaño de la lista es: "+lista.size());
        System.out.println(lista.getLast());
    }


}