fn main(){

    let mut cs:String;
    let mut liste = Vec::new();
    let sortebel = |a: &u32,b: &u32|a.cmp(b);

    for x in 100..999{
        for b in 100..999{
            let mut c:u32 = b * x;

            cs = c.to_string();

            if reverse_string(&cs) == cs {
                liste.push(c)
            }
        }
    }

    liste.sort_by(sortebel);
    println!("{}",liste[liste.len() - 1]);
}

fn reverse_string(s:&String)-> String{
    return s.chars().rev().collect::<String>()
}