#![allow(non_snake_case)] // fixin some shit error abt snake stuff

fn main() 
{
    // Notez
    // mut means u can change var -         let mut var: i32 = 69;
    // lack of 'mut' gives u error if u reassign var
    // int be of 2 types 'i' and 'u' and then followed by the int type like, 8, 16, 32, 64, 128 etc. u can add size to make it defaut
    // for float the same syntax but replace i/u with f
    // dividing 2 float givs exact answer... but dividing 2 floats givs math.floor()-ed answer
    // bool iz true false
    // char is depicted with '', string is depicted with ""
    // tup (tuple) iz defined az            let tup: (vartype, vartype...)=(var, var...);
    // u can get deconstruct by saying             let (x, y...) = tup    - dis gives corresponding data to x, y.. seperately
    // get val of tup by doin           tup.0           or whatever index of num
    // haz to be same var type in array; size cannot be changed - like c#... array type be written like      let var: [vartype:length] = array
    //  or u can also type (for same value of each element in array)             let var: [element_val, length]
    // access elements with [] - like c# and python
    


    //      ==========================================STUFF TO DO========================================

    //                  TF U DOIN!!! MEAK USER NUMBER THING GO UN_BRRRRRRRRRRR...   UPREESHEYATED
    
    extern crate serde;

    use std::io;        // import std.io
    use firebase_rs::Firebase;
    use serde::{Serialize, Deserialize};

    #[derive(Debug, Serialize, Deserialize)]
    
    enum General
    {
        Number(usize),
        None
    }

    let origroom = Firebase::new("https://maifurztruztprojekt-default-rtdb.firebaseio.com/roomz.json").unwrap(); // setup firebase
    let roomData = Firebase::new("https://maifurztruztprojekt-default-rtdb.firebaseio.com/roomz.json").unwrap(); // setup firebase
    let room = Firebase::new("https://maifurztruztprojekt-default-rtdb.firebaseio.com/roomz.json").unwrap();


    println!("Enter name of room: ");
    let mut roomname= String::new();
    io::stdin()                 // yeet name into str name and give error msg if error 'unaybal 3 reed laiyne'
        .read_line(&mut roomname) // Get room
        .expect("unaybal 2 reed laiyne");
    

    println!("Enter your name: ");
    let mut name= String::new();
    io::stdin()                 // Get name
        .read_line(&mut name)
        .expect("unaybal 2 reed laiyne");

    let room=room.at(&roomname).unwrap().at("players").unwrap();
    let origroom=origroom.at(&roomname).unwrap();
    let roomData=roomData.at(&roomname).unwrap().at("data").unwrap();
    let res=roomData.update("{\"PlayerTurn\":\"0\", \"TotalMoney\":\"69420\"}");
    println!("Room Data Response: {:?}", res);
    println!("{:?}", room.get().unwrap().body);
    let usernum: usize = if room.get().unwrap().body!="null"
    {
        room.get_generic::<Vec<String>>().unwrap().data.len()
    }
    else
    {
        0
    };
    
    let data = format!("{{\"{}\":\"{}\"}}", usernum, name.trim());
    let res=room.update(&data).unwrap();
    println!("Room Players Response: {:?}", res);

    print!("joined {}", roomname);


    GameLoop();

    // tmp
    leevRoom(room, origroom, usernum, name);
}

fn GameLoop()
{
    use std::io;

    println!("GameLoop");
    
    loop
    {
        let mut leavecondition= String::new();
        io::stdin()
            .read_line(&mut leavecondition)
            .expect("breh");
        let leavecondition: bool=leavecondition.trim().parse().unwrap();
        if leavecondition
        {
            break;
        }
    }
}

fn leevRoom(room: firebase_rs::Firebase, origroom:firebase_rs::Firebase, usernum: usize, name:String)
{
    let data = format!("{{\"{}\":\"{}\"}}", usernum, name.trim());
    let res = room.delete(&data);
    println!("{:?}", res);
    println!("{}",usernum);
    if usernum==0
    {
        let data = "{\"data\"}";
        let res = origroom.delete(&data);
        println!("{:?}", res);
    }

}