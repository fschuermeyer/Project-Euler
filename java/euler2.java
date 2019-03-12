public class euler2 {
	public static void main(String[] args) {

        int one = 1;
        int second = 2;
        int count = 2;
        int item;
        boolean sItem = true;

        for (int i = 0; i < 100; i++) {
            if(sItem){
                sItem = false;
                one = one + second;
                item = one;
            }else{
                sItem = true;
                second = one + second;
                item = second;
            }

            if(item % 2 == 0 && count < 4000000){
                count += item;
            }
        }

        System.out.println(count);

	}
}
