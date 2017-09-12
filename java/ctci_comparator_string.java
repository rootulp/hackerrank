// Write your Checker class here
class Checker implements Comparator<Player> {
    public int compare(Player p1, Player p2) {
        if (p1.score != p2.score) {
            return p2.score - p1.score;
        } else {
            return p1.name.compareTo(p2.name);
        }   
    }
}
