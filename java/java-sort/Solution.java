import java.util.*;

class Student implements Comparable<Student> {
    private int id;
    private String fname;
    private double cgpa;
    public Student(int id, String fname, double cgpa) {
        super();
        this.id = id;
        this.fname = fname;
        this.cgpa = cgpa;
    }
    public int getId() {
        return id;
    }
    public String getFname() {
        return fname;
    }
    public double getCgpa() {
        return cgpa;
    }

    public int compareTo(Student other) {
        if (Double.compare(other.getCgpa(), this.getCgpa()) != 0) {
            return Double.compare(other.getCgpa(), this.getCgpa());
        } else if (this.getFname().compareTo(other.getFname()) != 0) {
            return this.getFname().compareTo(other.getFname());
        } else {
            return Integer.compare(other.getId(), this.getId());
        }
    }
}

public class Solution {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());

        List<Student> studentList = new ArrayList<Student>();
        while(testCases>0){
            int id = in.nextInt();
            String fname = in.next();
            double cgpa = in.nextDouble();

            Student st = new Student(id, fname, cgpa);
            studentList.add(st);

            testCases--;
        }
        in.close();

        studentList.sort(null);
          for(Student st: studentList){
            System.out.println(st.getFname());
        }
    }
}
