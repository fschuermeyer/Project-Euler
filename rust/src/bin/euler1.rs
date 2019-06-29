fn main(){

    let mut result:u32 = 0;

    for x in 1..1000 {
        if x % 3 == 0 || x % 5 == 0 {
            result += x;
        }
    }

    println!("Antwort auf Euler 1 ist {}",result);

}